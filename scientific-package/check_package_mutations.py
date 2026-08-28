#!/usr/bin/env python3
"""Deterministic negative controls for the candidate package verifier."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import tempfile
from collections.abc import Callable
from pathlib import Path

from check_candidate_package import (
    extract_verified_atlas,
    file_sha256,
    verify_embedded_digest,
    verify_exact_root,
    verify_manifest,
)


SCHEMA = "cyclicity-open-problems-package-mutations-v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def expect_failure(
    label: str,
    action: Callable[[], object],
    diagnostic: str,
) -> dict[str, object]:
    try:
        action()
    except RuntimeError as error:
        require(diagnostic in str(error), (
            f"{label} failed for the wrong reason: {error}"
        ))
        return {
            "label": label,
            "rejected": True,
            "expected_diagnostic": diagnostic,
        }
    raise RuntimeError(f"mutation was not rejected: {label}")


def copy_exact_package(source: Path, destination: Path, paths: list[str]) -> None:
    destination.mkdir(parents=True, exist_ok=False)
    for relative in paths:
        shutil.copyfile(source / relative, destination / relative)
    shutil.copyfile(
        source / "PACKAGE_MANIFEST.json",
        destination / "PACKAGE_MANIFEST.json",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent,
    )
    parser.add_argument("--atlas-archive", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    root = args.root.resolve()
    atlas_archive = args.atlas_archive.resolve()
    manifest, paths = verify_manifest(root, root / "PACKAGE_MANIFEST.json")
    atlas_sha256 = manifest["atlas_upstream_package_sha256"]
    require(file_sha256(atlas_archive) == atlas_sha256, (
        "input Atlas archive does not match the package manifest"
    ))

    records: list[dict[str, object]] = []
    with tempfile.TemporaryDirectory(prefix="cyclicity-package-mutations-") as temporary:
        temporary_root = Path(temporary)
        mutated_root = temporary_root / "package"
        copy_exact_package(root, mutated_root, paths)
        verify_exact_root(mutated_root, paths)

        target_name = "CANDIDATE_MANUSCRIPT.md"
        target = mutated_root / target_name
        original_target = target.read_bytes()
        target.write_bytes(original_target + b"\nMUTATION\n")
        records.append(expect_failure(
            "manifest-member-byte-mutation",
            lambda: verify_manifest(
                mutated_root,
                mutated_root / "PACKAGE_MANIFEST.json",
            ),
            "size mismatch",
        ))
        target.write_bytes(original_target)

        undeclared = mutated_root / "UNDECLARED_MUTATION.txt"
        undeclared.write_text("undeclared\n", encoding="utf-8")
        records.append(expect_failure(
            "undeclared-root-member",
            lambda: verify_exact_root(mutated_root, paths),
            "undeclared or missing release members",
        ))
        undeclared.unlink()

        manifest_path = mutated_root / "PACKAGE_MANIFEST.json"
        original_manifest = manifest_path.read_bytes()
        manifest_value = json.loads(original_manifest)
        manifest_value["unexpected_field"] = True
        manifest_path.write_text(
            json.dumps(manifest_value, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        records.append(expect_failure(
            "unknown-manifest-field",
            lambda: verify_manifest(mutated_root, manifest_path),
            "unknown top-level fields",
        ))
        manifest_path.write_bytes(original_manifest)

        receipt_name = "support_rank_reconstruction_receipt.json"
        receipt_path = mutated_root / receipt_name
        receipt_value = json.loads(receipt_path.read_text(encoding="utf-8"))
        receipt_value["status"] = "mutated"
        receipt_path.write_text(
            json.dumps(receipt_value, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        records.append(expect_failure(
            "embedded-receipt-digest-mutation",
            lambda: verify_embedded_digest(receipt_path, "receipt_sha256"),
            "invalid receipt_sha256",
        ))

        mutated_archive = temporary_root / "mutated-atlas.zip"
        shutil.copyfile(atlas_archive, mutated_archive)
        archive_bytes = bytearray(mutated_archive.read_bytes())
        require(archive_bytes, "Atlas archive is empty")
        archive_bytes[-1] ^= 1
        mutated_archive.write_bytes(archive_bytes)
        records.append(expect_failure(
            "atlas-archive-byte-mutation",
            lambda: extract_verified_atlas(
                mutated_archive,
                atlas_sha256,
                temporary_root / "mutated-atlas-extraction",
            ),
            "Atlas archive SHA-256 differs",
        ))

    receipt: dict[str, object] = {
        "schema": SCHEMA,
        "status": "pass",
        "mutation_count": len(records),
        "records": records,
        "claim_boundary": {
            "established": (
                "the package verifier rejects the five declared mutation "
                "classes for this exact implementation"
            ),
            "not_established": [
                "proof correctness",
                "exhaustive verifier security",
                "independent reproduction",
                "novelty, peer review, or publication readiness",
            ],
        },
    }
    receipt["receipt_sha256"] = canonical_hash(receipt)
    encoded = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
    else:
        print(encoded, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
