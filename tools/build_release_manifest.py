#!/usr/bin/env python3
"""Build or verify a sorted SHA-256 manifest for the public release unit."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import tempfile
from pathlib import Path


LINE = re.compile(r"^([0-9a-f]{64})  (.+)$")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def inventory(root: Path, output: Path) -> list[Path]:
    files = []
    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.relative_to(root).parts:
            continue
        if path == output or path.name in {".DS_Store"} or "__pycache__" in path.parts:
            continue
        files.append(path)
    return sorted(files, key=lambda path: path.relative_to(root).as_posix())


def build(root: Path, output: Path) -> None:
    require(not output.exists(), "refusing to overwrite release manifest")
    lines = [f"{sha256(path)}  {path.relative_to(root).as_posix()}" for path in inventory(root, output)]
    encoded = ("\n".join(lines) + "\n").encode("utf-8")
    with tempfile.NamedTemporaryFile(mode="wb", dir=root, prefix=".manifest.", delete=False) as handle:
        handle.write(encoded)
        temporary = Path(handle.name)
    os.replace(temporary, output)
    print(f"files={len(lines)} manifest_sha256={sha256(output)}")


def verify(root: Path, output: Path) -> None:
    require(output.is_file(), "release manifest is missing")
    records: dict[str, str] = {}
    for line in output.read_text(encoding="utf-8").splitlines():
        match = LINE.fullmatch(line)
        require(match is not None, "malformed manifest line")
        digest, relative = match.groups()
        require(relative not in records, f"duplicate manifest path: {relative}")
        records[relative] = digest
    expected = [path.relative_to(root).as_posix() for path in inventory(root, output)]
    require(list(records) == expected, "release manifest inventory differs from public unit")
    for relative, digest in records.items():
        require(sha256(root / relative) == digest, f"release manifest digest differs: {relative}")
    print(f"files={len(records)} status=pass manifest_sha256={sha256(output)}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--mode", choices=["build", "verify"], required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output.resolve()
    require(root.is_dir(), "public release root is missing")
    require(output.parent == root, "release manifest must be at repository root")
    if args.mode == "build":
        build(root, output)
    else:
        verify(root, output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
