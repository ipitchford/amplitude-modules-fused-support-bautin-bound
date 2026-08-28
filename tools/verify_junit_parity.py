#!/usr/bin/env python3
"""Verify ordinary/optimized JUnit inventory and emit a parity receipt."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def inventory(path: Path) -> tuple[dict[str, int], list[str], dict[str, str]]:
    root = ET.parse(path).getroot()
    require(root.tag == "testsuite", f"invalid JUnit root: {path.name}")
    counts = {key: int(root.get(key, "-1")) for key in ["tests", "failures", "errors", "skipped"]}
    names = [f"{case.get('classname')}::{case.get('name')}" for case in root.findall("testcase")]
    require(len(names) == len(set(names)), f"duplicate testcase identity: {path.name}")
    properties = {item.get("name", ""): item.get("value", "") for item in root.findall("./properties/property")}
    return counts, names, properties


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ordinary", type=Path, required=True)
    parser.add_argument("--optimized", type=Path, required=True)
    parser.add_argument("--target-sha", required=True)
    parser.add_argument("--recorded-at", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    ordinary = args.ordinary.resolve()
    optimized = args.optimized.resolve()
    output = args.output.resolve()
    require(not output.exists(), "refusing to overwrite parity receipt")
    ordinary_counts, ordinary_names, ordinary_properties = inventory(ordinary)
    optimized_counts, optimized_names, optimized_properties = inventory(optimized)
    require(ordinary_counts == optimized_counts, "ordinary/optimized aggregate counts differ")
    require(ordinary_names == optimized_names, "ordinary/optimized testcase inventories differ")
    require(ordinary_counts == {"tests": 9, "failures": 0, "errors": 0, "skipped": 0}, "JUnit aggregate is not all-passing")
    require(ordinary_properties.get("execution_mode") == "ordinary", "ordinary execution mode missing")
    require(optimized_properties.get("execution_mode") == "optimized", "optimized execution mode missing")
    require(ordinary_properties.get("target_sha256") == args.target_sha, "ordinary target binding differs")
    require(optimized_properties.get("target_sha256") == args.target_sha, "optimized target binding differs")
    require(ordinary_properties.get("manifest_sha256") == optimized_properties.get("manifest_sha256"), "manifest bindings differ")

    receipt = {
        "aggregate": ordinary_counts,
        "manifest_sha256": ordinary_properties["manifest_sha256"],
        "optimized_junit_sha256": sha256(optimized),
        "ordinary_junit_sha256": sha256(ordinary),
        "recorded_at": args.recorded_at,
        "schema": "evidence-press-junit-parity-v1",
        "status": "pass",
        "target_sha256": args.target_sha,
        "testcase_inventory": ordinary_names,
    }
    encoded = (json.dumps(receipt, indent=2, sort_keys=True) + "\n").encode("utf-8")
    receipt["receipt_sha256"] = hashlib.sha256(encoded).hexdigest()
    encoded = (json.dumps(receipt, indent=2, sort_keys=True) + "\n").encode("utf-8")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="wb", dir=output.parent, prefix=f".{output.name}.", delete=False) as handle:
        handle.write(encoded)
        temporary = Path(handle.name)
    os.replace(temporary, output)
    print(f"tests={ordinary_counts['tests']} status=pass sha256={sha256(output)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
