#!/usr/bin/env python3
"""Assemble an exact public candidate package in a new directory."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from build_candidate_manifest import PACKAGE_FILES
from check_candidate_package import verify_exact_root, verify_manifest


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=Path,
        default=Path(__file__).resolve().parent,
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    source = args.source.resolve()
    output = args.output.resolve()
    require(source.is_dir(), "source package directory is missing")
    require(not output.exists(), "staging output already exists")
    require(not output.is_relative_to(source), (
        "staging output may not be inside the development package"
    ))

    _manifest, paths = verify_manifest(source, source / "PACKAGE_MANIFEST.json")
    require(paths == PACKAGE_FILES, "manifest differs from canonical package files")

    output.mkdir(parents=True, exist_ok=False)
    for relative in paths:
        source_path = source / relative
        target_path = output / relative
        target_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source_path, target_path)
    shutil.copyfile(
        source / "PACKAGE_MANIFEST.json",
        output / "PACKAGE_MANIFEST.json",
    )
    verify_exact_root(output, paths)
    print(
        f"staged {len(paths)} manifest members plus PACKAGE_MANIFEST.json "
        f"at {output}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
