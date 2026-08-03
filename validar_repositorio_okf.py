#!/usr/bin/env python3
"""
Valida la estructura básica y los enlaces locales de un repositorio OKF.

Uso desde la carpeta raíz del repositorio:

    py validar_repositorio_okf.py

Comprobaciones:
- existe index.md en la raíz;
- el índice raíz declara okf_version;
- los index.md de subcarpetas no contienen frontmatter YAML;
- los enlaces Markdown locales apuntan a archivos existentes.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote


FRONTMATTER_RE = re.compile(
    r"\A(?:\ufeff)?---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)",
    re.DOTALL,
)

MARKDOWN_LINK_RE = re.compile(
    r"(?<!!)\[[^\]]*\]\(([^)]+)\)"
)


def read_utf8(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def get_frontmatter(text: str) -> str | None:
    match = FRONTMATTER_RE.match(text)
    return match.group(1) if match else None


def normalise_link_target(raw_target: str) -> str | None:
    target = raw_target.strip()

    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()

    if " " in target and not target.startswith(("http://", "https://")):
        # Permite el título opcional de Markdown:
        # (archivo.md "Título")
        target = target.split(" ", 1)[0]

    lower = target.lower()

    if (
        not target
        or target.startswith("#")
        or lower.startswith(("http://", "https://", "mailto:", "tel:", "data:"))
    ):
        return None

    target = target.split("#", 1)[0].split("?", 1)[0]
    return unquote(target).replace("\\", "/")


def resolve_local_target(source: Path, target: str) -> Path:
    candidate = (source.parent / target).resolve()

    if candidate.is_dir():
        return candidate / "index.md"

    return candidate


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Valida la estructura y los enlaces locales de un repositorio OKF."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Carpeta raíz del repositorio. Por defecto: carpeta actual.",
    )
    args = parser.parse_args()

    root = args.root.expanduser().resolve()

    if not root.is_dir():
        print(f"ERROR: no existe la carpeta: {root}", file=sys.stderr)
        return 2

    errors: list[str] = []
    warnings: list[str] = []

    root_index = root / "index.md"

    if not root_index.is_file():
        errors.append("No existe index.md en la raíz.")
    else:
        try:
            root_text = read_utf8(root_index)
        except UnicodeDecodeError:
            errors.append("index.md no puede leerse como UTF-8.")
        else:
            frontmatter = get_frontmatter(root_text)
            if frontmatter is None:
                errors.append("El index.md raíz no contiene frontmatter YAML.")
            elif not re.search(
                r"(?m)^[ \t]*okf_version[ \t]*:[ \t]*['\"]?0\.2['\"]?[ \t]*$",
                frontmatter,
            ):
                errors.append(
                    'El index.md raíz no declara exactamente okf_version: "0.2".'
                )

    markdown_files = sorted(root.rglob("*.md"))

    for path in markdown_files:
        try:
            text = read_utf8(path)
        except UnicodeDecodeError:
            errors.append(
                f"No puede leerse como UTF-8: {path.relative_to(root)}"
            )
            continue

        if path.name.lower() == "index.md" and path.resolve() != root_index.resolve():
            if get_frontmatter(text) is not None:
                errors.append(
                    f"Index de subcarpeta con frontmatter: {path.relative_to(root)}"
                )

        for raw_target in MARKDOWN_LINK_RE.findall(text):
            target = normalise_link_target(raw_target)
            if target is None:
                continue

            resolved = resolve_local_target(path, target)

            try:
                resolved.relative_to(root)
            except ValueError:
                warnings.append(
                    f"Enlace fuera del repositorio en {path.relative_to(root)}: "
                    f"{raw_target}"
                )
                continue

            if not resolved.exists():
                errors.append(
                    f"Enlace roto en {path.relative_to(root)}: "
                    f"{raw_target} -> {resolved.relative_to(root)}"
                )

    print(f"Archivos Markdown revisados: {len(markdown_files)}")

    if warnings:
        print()
        print(f"ADVERTENCIAS: {len(warnings)}")
        for warning in warnings:
            print(f"  - {warning}")

    if errors:
        print()
        print(f"ERRORES: {len(errors)}")
        for error in errors:
            print(f"  - {error}")
        return 1

    print()
    print("OK: la estructura básica y los enlaces locales son correctos.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
