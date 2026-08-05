#!/usr/bin/env python3
"""
Validador OKF v2 para la base de conocimiento del CAU del CEPRUD.

Amplía el validador original con las comprobaciones que la auditoría de agosto
de 2026 identificó como necesarias. Mantiene la filosofía permisiva de OKF: lo
que la especificación exige es ERROR; lo que es criterio propio del proyecto es
AVISO, salvo que se ejecute con --estricto.

Uso:
    python validar_repositorio_okf_v2.py
    python validar_repositorio_okf_v2.py --root . --estricto
    python validar_repositorio_okf_v2.py --json informe.json

Comprobaciones de CONFORMIDAD OKF v0.1 (errores):
  §9.1  todo .md no reservado tiene frontmatter YAML parseable;
  §9.2  todo frontmatter tiene un campo `type` no vacío;
  §9.3  los index.md de subcarpeta no llevan frontmatter;
  §11   el index.md raíz declara una okf_version conocida.

Comprobaciones de CALIDAD del proyecto (avisos):
  - vocabulario controlado de type, service, status, confidentiality, audience;
  - campos obligatorios del proyecto presentes;
  - title del frontmatter == encabezado de nivel 1;
  - un solo encabezado de nivel 1 por documento;
  - enlaces locales resueltos (absolutos de bundle y relativos);
  - referencias sin enlazar en secciones de «relacionados»;
  - etiquetas fuera del vocabulario y exceso de etiquetas;
  - review_date vencida;
  - texto de enlace divergente para un mismo destino;
  - patrones sensibles: tokens, claves, IP, rutas, SQL;
  - documentos huérfanos.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path
from urllib.parse import unquote

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERROR: se requiere PyYAML (pip install pyyaml)", file=sys.stderr)
    raise SystemExit(2)


# --------------------------------------------------------------------------- #
# Configuración del proyecto
# --------------------------------------------------------------------------- #

VERSIONES_OKF_CONOCIDAS = {"0.1"}
RESERVADOS = {"index.md", "log.md"}

TYPES = {
    "Concept", "Rule", "Procedure", "TicketCategory", "DecisionTree",
    "ResponseTemplate", "SpaceType", "UserType", "Role", "UserState",
    "OperationalParameters", "ErrorMessage", "Unit", "Glossary",
    "Reference", "Governance", "FAQ",
}
TYPES_OBSOLETOS = {"KnowledgeDocument"}

SERVICES = {"PRADO", "ABIERTA UGR", "E-CAMPUS", "OCW", "FORMACIÓN", "TRANSVERSAL", "CEPRUD"}
STATUS = {"placeholder", "draft", "reviewed", "deprecated"}
CONFIDENTIALITY = {"publico", "uso-interno", "restringido", "confidencial"}
AUDIENCE = {"personal-cau", "personal-tecnico", "usuario-final", "gestor"}
LANGUAGES = {"es", "en"}

CAMPOS_OBLIGATORIOS = [
    "type", "title", "description", "status", "language", "tags",
]
CAMPOS_RECOMENDADOS = [
    "service", "audience", "confidentiality", "owner",
    "timestamp", "last_reviewed", "review_date",
]

MAX_TAGS = 6

# Patrones que nunca deberían aparecer en el repositorio.
PATRONES_SENSIBLES = [
    (r"token=[0-9a-fA-F-]{8,}", "token de acceso en una URL"),
    (r"(?i)\b(api[_-]?key|secret|passwd|password)\s*[:=]\s*\S+", "credencial en texto"),
    (r"\b(?:10|172|192)\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", "dirección IP privada"),
    (r"(?i)\b(select|insert|update|delete)\s+.{0,40}\bfrom\b", "consulta SQL"),
    (r"[A-Za-z]:\\\\[A-Za-z0-9_\\\\-]+", "ruta de sistema de ficheros"),
    (r"(?i)jdbc:[a-z]+:", "cadena de conexión"),
]

FRONTMATTER_RE = re.compile(
    r"\A(?:﻿)?---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", re.DOTALL
)
LINK_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)]+)\)")
H1_RE = re.compile(r"^# (.+)$", re.M)
HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.*?)[ \t]*$", re.M)
SECCION_RELACIONADOS_RE = re.compile(r"relacionad|categor[íi]as de iris|temas relacionados", re.I)


class Informe:
    def __init__(self) -> None:
        self.errores: list[str] = []
        self.avisos: list[str] = []
        self.info: list[str] = []

    def error(self, msg: str) -> None:
        self.errores.append(msg)

    def aviso(self, msg: str) -> None:
        self.avisos.append(msg)


# --------------------------------------------------------------------------- #
# Utilidades
# --------------------------------------------------------------------------- #

def leer(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def frontmatter_bruto(texto: str) -> str | None:
    m = FRONTMATTER_RE.match(texto)
    return m.group(1) if m else None


def normalizar_destino(bruto: str) -> str | None:
    t = bruto.strip()
    if t.startswith("<") and t.endswith(">"):
        t = t[1:-1].strip()
    if " " in t and not t.startswith(("http://", "https://")):
        t = t.split(" ", 1)[0]
    low = t.lower()
    if not t or t.startswith("#") or low.startswith(
        ("http://", "https://", "mailto:", "tel:", "data:")
    ):
        return None
    t = t.split("#", 1)[0].split("?", 1)[0]
    if not t:
        return None
    return unquote(t).replace("\\", "/")


def resolver(origen: Path, destino: str, raiz: Path) -> Path:
    """Resuelve enlaces absolutos de bundle (§5.1) y relativos (§5.2)."""
    if destino.startswith("/"):
        cand = (raiz / destino.lstrip("/")).resolve()
    else:
        cand = (origen.parent / destino).resolve()
    return cand / "index.md" if cand.is_dir() else cand


def excluido(rel: Path) -> bool:
    return any(p.startswith((".", "_")) for p in rel.parts)


# --------------------------------------------------------------------------- #
# Comprobaciones
# --------------------------------------------------------------------------- #

def comprobar_indice_raiz(raiz: Path, inf: Informe) -> None:
    idx = raiz / "index.md"
    if not idx.is_file():
        inf.error("No existe index.md en la raíz del bundle.")
        return
    fm = frontmatter_bruto(leer(idx))
    if fm is None:
        inf.error("§11 index.md raíz: no declara frontmatter con okf_version.")
        return
    m = re.search(r"(?m)^[ \t]*okf_version[ \t]*:[ \t]*['\"]?([0-9]+\.[0-9]+)['\"]?", fm)
    if not m:
        inf.error("§11 index.md raíz: no declara okf_version.")
    elif m.group(1) not in VERSIONES_OKF_CONOCIDAS:
        inf.error(
            f"§11 index.md raíz: okf_version \"{m.group(1)}\" no corresponde a ninguna "
            f"versión publicada de OKF (conocidas: {', '.join(sorted(VERSIONES_OKF_CONOCIDAS))})."
        )


def comprobar_documento(path: Path, raiz: Path, texto: str, inf: Informe,
                        titulos: dict[str, str]) -> dict | None:
    rel = path.relative_to(raiz)
    nombre = path.name.lower()
    fm_bruto = frontmatter_bruto(texto)

    # --- archivos reservados ------------------------------------------------
    if nombre in RESERVADOS:
        es_raiz = path.resolve() == (raiz / "index.md").resolve()
        if nombre == "index.md" and not es_raiz and fm_bruto is not None:
            inf.error(f"§11 {rel}: index.md de subcarpeta con frontmatter.")
        if nombre == "log.md":
            if fm_bruto is not None:
                inf.error(f"§7 {rel}: log.md no admite frontmatter.")
            if re.search(r"(?m)^\\", texto):
                inf.error(
                    f"§7 {rel}: contiene caracteres escapados con barra invertida. "
                    f"El archivo no es Markdown válido."
                )
            if "&#x" in texto:
                inf.error(f"§7 {rel}: contiene entidades HTML escapadas.")
            fechas = re.findall(r"(?m)^##[ \t]+(\d{4}-\d{2}-\d{2})[ \t]*$", texto)
            if not fechas:
                inf.error(f"§7 {rel}: no contiene encabezados de fecha ISO 8601 (## AAAA-MM-DD).")
        return None

    # --- conformidad §9.1 y §9.2 -------------------------------------------
    if fm_bruto is None:
        inf.error(f"§9.1 {rel}: documento de concepto sin frontmatter YAML.")
        return None
    try:
        fm = yaml.safe_load(fm_bruto) or {}
    except yaml.YAMLError as exc:
        inf.error(f"§9.1 {rel}: frontmatter YAML no parseable ({exc.__class__.__name__}).")
        return None
    if not isinstance(fm, dict):
        inf.error(f"§9.1 {rel}: el frontmatter no es un mapa YAML.")
        return None

    tipo = fm.get("type")
    if not tipo or not str(tipo).strip():
        inf.error(f"§9.2 {rel}: falta el campo obligatorio `type`.")
    elif tipo in TYPES_OBSOLETOS:
        inf.aviso(f"{rel}: `type: {tipo}` es un tipo genérico suprimido. Asigne un tipo real.")
    elif tipo not in TYPES:
        inf.aviso(f"{rel}: `type: {tipo}` fuera del vocabulario controlado.")

    # --- campos del proyecto ------------------------------------------------
    for campo in CAMPOS_OBLIGATORIOS:
        if campo not in fm or fm[campo] in (None, "", []):
            inf.aviso(f"{rel}: falta el campo obligatorio del proyecto `{campo}`.")
    for campo in CAMPOS_RECOMENDADOS:
        if campo not in fm or fm[campo] in (None, "", []):
            inf.aviso(f"{rel}: falta el campo recomendado `{campo}`.")

    for campo, permitidos in (
        ("service", SERVICES), ("status", STATUS),
        ("confidentiality", CONFIDENTIALITY), ("audience", AUDIENCE),
        ("language", LANGUAGES),
    ):
        val = fm.get(campo)
        if val is not None and val not in permitidos:
            inf.aviso(f"{rel}: `{campo}: {val}` fuera del vocabulario controlado.")

    if fm.get("confidentiality") == "confidencial":
        inf.error(f"{rel}: marcado como `confidencial`; no debe residir en este repositorio.")

    if fm.get("owner") in (None, "", "por-definir"):
        inf.aviso(f"{rel}: sin responsable asignado (`owner`).")

    tags = fm.get("tags") or []
    if isinstance(tags, list) and len(tags) > MAX_TAGS:
        inf.aviso(f"{rel}: {len(tags)} etiquetas; el máximo del proyecto es {MAX_TAGS}.")

    # --- vigencia -----------------------------------------------------------
    rd = fm.get("review_date")
    if rd:
        try:
            venc = rd if isinstance(rd, date) else date.fromisoformat(str(rd))
            if venc < date.today():
                inf.aviso(f"{rel}: `review_date` vencida el {venc.isoformat()}.")
        except ValueError:
            inf.aviso(f"{rel}: `review_date` no tiene formato ISO 8601.")

    # --- title vs encabezado de nivel 1 ------------------------------------
    h1s = H1_RE.findall(texto)
    if not h1s:
        inf.aviso(f"{rel}: sin encabezado de nivel 1.")
    else:
        if len(h1s) > 1:
            inf.aviso(
                f"{rel}: {len(h1s)} encabezados de nivel 1. Un documento con varios H1 "
                f"no sobrevive al fragmentado; divídalo."
            )
        titulo = str(fm.get("title", "")).strip()
        if titulo and h1s[0].strip() != titulo:
            inf.aviso(f"{rel}: `title` ({titulo!r}) no coincide con el H1 ({h1s[0].strip()!r}).")

    for m in re.finditer(r"(?m)^#{1,6} .*[ \t]+$", texto):
        inf.aviso(f"{rel}: encabezado con espacio final: {m.group(0)!r}")

    # --- patrones sensibles -------------------------------------------------
    for patron, desc in PATRONES_SENSIBLES:
        m = re.search(patron, texto)
        if m:
            inf.error(f"{rel}: posible {desc} -> {m.group(0)[:60]!r}")

    if fm.get("title"):
        titulos[str(rel).replace("\\", "/")] = str(fm["title"]).strip()
    return fm


def comprobar_enlaces(archivos: list[Path], raiz: Path, inf: Informe,
                      titulos: dict[str, str]) -> None:
    entrantes: dict[str, int] = defaultdict(int)
    etiquetas: dict[str, set[str]] = defaultdict(set)
    titulos_norm = {t.lower(): r for r, t in titulos.items()}

    for path in archivos:
        rel = path.relative_to(raiz)
        texto = leer(path)

        for etiqueta, bruto in LINK_RE.findall(texto):
            destino = normalizar_destino(bruto)
            if destino is None:
                continue
            resuelto = resolver(path, destino, raiz)
            try:
                rel_dest = resuelto.relative_to(raiz)
            except ValueError:
                inf.aviso(f"{rel}: enlace fuera del bundle -> {bruto}")
                continue
            if not resuelto.exists():
                inf.error(f"{rel}: enlace roto -> {bruto} (resuelto en {rel_dest})")
                continue
            clave = str(rel_dest).replace("\\", "/")
            entrantes[clave] += 1
            if path.name.lower() != "log.md":
                # El historial es prosa: no cuenta para la coherencia del texto de enlace.
                etiquetas[clave].add(etiqueta.strip())
            if not destino.startswith("/"):
                inf.info.append(f"{rel}: enlace relativo -> {bruto} (§5.1 recomienda la forma absoluta)")

        # referencias sin enlazar en secciones de «relacionados»
        en_seccion = False
        for linea in texto.split("\n"):
            if linea.startswith("#"):
                en_seccion = bool(SECCION_RELACIONADOS_RE.search(linea))
                continue
            if en_seccion and linea.strip().startswith("- "):
                item = linea.strip()[2:].strip()
                if item.startswith("["):
                    continue
                candidato = titulos_norm.get(item.lower().rstrip("."))
                if candidato:
                    inf.aviso(
                        f"{rel}: referencia sin enlazar «{item}»; el documento existe "
                        f"en {candidato}."
                    )

    for destino, etiqs in sorted(etiquetas.items()):
        # La convención admite la forma en minúscula cuando el enlace va integrado en
        # una frase, así que las variantes de capitalización no cuentan como divergencia.
        # Se ignoran las etiquetas entre acentos graves: marcan el nombre literal de una
        # categoría de IRIS, no una forma alternativa de citar el documento.
        distintas = {e.lower() for e in etiqs if e and not e.startswith("`")}
        if len(distintas) > 2:
            inf.aviso(
                f"{destino}: citado con {len(distintas)} textos de enlace distintos "
                f"({sorted(distintas)[:4]}...). Use siempre el `title` del destino."
            )

    for path in archivos:
        rel = str(path.relative_to(raiz)).replace("\\", "/")
        if path.name.lower() in RESERVADOS:
            continue
        if entrantes.get(rel, 0) == 0:
            inf.aviso(f"{rel}: documento huérfano, sin ningún enlace entrante.")


# --------------------------------------------------------------------------- #
# Programa principal
# --------------------------------------------------------------------------- #

def main() -> int:
    ap = argparse.ArgumentParser(description="Validador OKF v2 del CAU del CEPRUD.")
    ap.add_argument("--root", type=Path, default=Path.cwd())
    ap.add_argument("--estricto", action="store_true",
                    help="Los avisos cuentan como errores.")
    ap.add_argument("--json", type=Path, help="Vuelca el informe en JSON.")
    ap.add_argument("--incluir-ocultos", action="store_true",
                    help="No excluir rutas que empiecen por '.' o '_'.")
    args = ap.parse_args()

    raiz = args.root.expanduser().resolve()
    if not raiz.is_dir():
        print(f"ERROR: no existe la carpeta {raiz}", file=sys.stderr)
        return 2

    inf = Informe()
    comprobar_indice_raiz(raiz, inf)

    archivos = sorted(
        p for p in raiz.rglob("*.md")
        if args.incluir_ocultos or not excluido(p.relative_to(raiz))
    )

    titulos: dict[str, str] = {}
    for path in archivos:
        try:
            texto = leer(path)
        except UnicodeDecodeError:
            inf.error(f"{path.relative_to(raiz)}: no puede leerse como UTF-8.")
            continue
        comprobar_documento(path, raiz, texto, inf, titulos)

    comprobar_enlaces(archivos, raiz, inf, titulos)

    print(f"Archivos Markdown revisados: {len(archivos)}")
    print(f"Errores de conformidad: {len(inf.errores)}")
    print(f"Avisos de calidad:      {len(inf.avisos)}")
    print(f"Notas informativas:     {len(inf.info)}")

    if inf.errores:
        print("\n=== ERRORES ===")
        for e in inf.errores:
            print(f"  - {e}")
    if inf.avisos:
        print("\n=== AVISOS ===")
        for a in inf.avisos[:200]:
            print(f"  - {a}")
        if len(inf.avisos) > 200:
            print(f"  ... y {len(inf.avisos) - 200} avisos más.")

    if args.json:
        args.json.write_text(json.dumps({
            "archivos": len(archivos),
            "errores": inf.errores,
            "avisos": inf.avisos,
            "info": inf.info,
        }, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\nInforme JSON escrito en {args.json}")

    if inf.errores or (args.estricto and inf.avisos):
        return 1
    print("\nOK: el bundle es conformante con OKF v0.1.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
