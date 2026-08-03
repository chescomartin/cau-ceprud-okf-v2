#!/usr/bin/env python3
"""
Detecta y elimina el frontmatter YAML de los index.md situados
por debajo de la raíz de un bundle OKF.

Uso desde la carpeta raíz del repositorio:

    py corregir_indices_okf.py
    py corregir_indices_okf.py --apply

Sin --apply solo informa de los archivos afectados.
Con --apply crea una copia .bak y corrige cada archivo.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path


FRONTMATTER_RE = re.compile(
    r"\A(?:\ufeff)?---[ \t]*\r?\n.*?\r?\n---[ \t]*(?:\r?\n|\Z)",
    re.DOTALL,
)


def find_non_root_indexes(root: Path) -> list[Path]:
    root_index = (root / "index.md").resolve()
    return sorted(
        path
        for path in root.rglob("index.md")
        if path.resolve() != root_index
    )


def has_frontmatter(text: str) -> bool:
    return FRONTMATTER_RE.match(text) is not None


def remove_frontmatter(text: str) -> str:
    corrected = FRONTMATTER_RE.sub("", text, count=1)
    return corrected.lstrip("\r\n")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Comprueba o elimina el frontmatter de los index.md "
            "que no están en la raíz del bundle OKF."
        )
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Carpeta raíz del bundle. Por defecto: carpeta actual.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Aplica las correcciones. Sin esta opción solo realiza la comprobación.",
    )
    args = parser.parse_args()

    root = args.root.expanduser().resolve()

    if not root.is_dir():
        print(f"ERROR: no existe la carpeta: {root}", file=sys.stderr)
        return 2

    root_index = root / "index.md"
    if not root_index.is_file():
        print(
            f"ERROR: no se encuentra el índice raíz: {root_index}",
            file=sys.stderr,
        )
        return 2

    affected: list[Path] = []

    for path in find_non_root_indexes(root):
        try:
            text = path.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError:
            print(f"ERROR: no se puede leer como UTF-8: {path}", file=sys.stderr)
            return 2

        if has_frontmatter(text):
            affected.append(path)

    if not affected:
        print("OK: ningún index.md de subcarpeta contiene frontmatter YAML.")
        return 0

    print(f"Se han encontrado {len(affected)} index.md de subcarpetas con frontmatter:")
    for path in affected:
        print(f"  - {path.relative_to(root)}")

    if not args.apply:
        print()
        print("Comprobación terminada. No se ha modificado ningún archivo.")
        print("Para corregirlos, ejecuta:")
        print("  py corregir_indices_okf.py --apply")
        return 0

    print()
    for path in affected:
        text = path.read_text(encoding="utf-8-sig")
        corrected = remove_frontmatter(text)

        backup = path.with_name(path.name + ".bak")
        if not backup.exists():
            shutil.copy2(path, backup)

        path.write_text(corrected, encoding="utf-8", newline="\n")
        print(f"CORREGIDO: {path.relative_to(root)}")
        print(f"  Copia:    {backup.relative_to(root)}")

    print()
    print("Corrección terminada.")
    print("El index.md de la raíz no se ha modificado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
