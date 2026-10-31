#!/usr/bin/env python3
"""Empacota a Agent Skill comum em um arquivo ZIP portátil."""

import argparse
import os
import re
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = Path("skills/meds-suite")


def skill_version(skill):
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    match = re.search(r'^  version: "(\d+\.\d+\.\d+)"\s*$', text, re.MULTILINE)
    if not match:
        raise ValueError("versão semântica ausente no frontmatter da skill")
    return match.group(1)


def package(output, root=ROOT, overwrite=False):
    source = root / SKILL
    if not (source / "SKILL.md").is_file():
        raise FileNotFoundError(f"skill ausente: {source / 'SKILL.md'}")
    output = Path(output).expanduser().resolve()
    if output.exists() and not overwrite:
        raise FileExistsError(f"arquivo já existe: {output} (use --overwrite para substituir)")
    if output.is_relative_to(source.resolve()):
        raise ValueError("o arquivo ZIP não pode ser criado dentro da fonte da skill")

    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=output.parent) as temporary:
        staged = Path(temporary) / output.name
        with zipfile.ZipFile(staged, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for path in sorted(source.rglob("*")):
                if not path.is_file():
                    continue
                relative = path.relative_to(source).as_posix()
                info = zipfile.ZipInfo(f"meds-suite/{relative}", date_time=(1980, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, path.read_bytes())
        with zipfile.ZipFile(staged) as archive:
            invalid = archive.testzip()
            if invalid:
                raise zipfile.BadZipFile(f"arquivo ZIP inválido em {invalid}")
        os.replace(staged, output)
    return output


def main():
    version = skill_version(ROOT / SKILL)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="destino do arquivo ZIP")
    parser.add_argument("--overwrite", action="store_true", help="substitui o destino se já existir")
    args = parser.parse_args()
    try:
        output = package(args.output, overwrite=args.overwrite)
    except (FileNotFoundError, FileExistsError, ValueError, zipfile.BadZipFile) as exc:
        parser.error(str(exc))
    print(f"Skill v{version} empacotada em {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
