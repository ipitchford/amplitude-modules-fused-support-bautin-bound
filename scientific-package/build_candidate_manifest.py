#!/usr/bin/env python3
"""Build the deterministic allowlist manifest for the candidate package."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
from pathlib import Path


SCHEMA = "cyclicity-open-problems-candidate-manifest-v1"
ATLAS_SHA256 = "3a132530f31c1af3870de7af7a13d41389ffbf051ab2760b3c0110173c268e8a"

PACKAGE_FILES = sorted([
    "BAUTIN_HOSTILE_REVIEW.md",
    "BILINGUAL_ABSTRACT.md",
    "CANDIDATE_MANUSCRIPT.md",
    "CANDIDATE_PREPRINT.pdf",
    "CANDIDATE_PREPRINT.tex",
    "EDITORIAL_01_EDITOR_IN_CHIEF.md",
    "EDITORIAL_02_METHODOLOGY_SPECIALIST.md",
    "EDITORIAL_03_DOMAIN_SPECIALIST.md",
    "EDITORIAL_04_APPLICATIONS_SPECIALIST.md",
    "EDITORIAL_05_DEVILS_ADVOCATE.md",
    "EDITORIAL_06_SYNTHESIS.md",
    "EDITORIAL_DISPOSITION.json",
    "ENVIRONMENT.txt",
    "LICENSE",
    "LICENSE-CODE",
    "LICENSES.md",
    "NOVELTY_AUDIT.md",
    "NOVELTY_GATE_REPORT.md",
    "NOVELTY_GATE_TARGETS.yaml",
    "PANEL_REVIEW_SYNTHESIS.md",
    "PROBLEM_SELECTION_GATE.md",
    "PUBLIC_DOMAIN.md",
    "PUBLIC_RELEASE_UNIT.md",
    "README.md",
    "REFEREE_CONFIGURATION.md",
    "REFEREE_PACKET.md",
    "REPLAY_INPUTS.json",
    "REPLAY_REQUIREMENTS.txt",
    "REPRODUCIBILITY_ENVIRONMENT.md",
    "RESULT_PACKAGE_A.md",
    "RESULT_PACKAGE_B.md",
    "RESULT_PACKAGE_C.md",
    "RESULT_PACKAGE_ZERO_CYCLE_BAUTIN.md",
    "REVIEW_RESPONSE_MATRIX.md",
    "SOURCE_CONVENTION_AUDIT.md",
    "SOURCE_PROVENANCE.json",
    "STATUS.md",
    "SUPPLEMENT_BINOMIAL_LAURENT.md",
    "THEOREM_0_MONODROMY_BLOCKS.md",
    "THEOREM_A_DICKSON.md",
    "THEOREM_B_EXCEPTIONAL_RITT.md",
    "THEOREM_C_WEIGHTED_ORDER.md",
    "THEOREM_D_BAUTIN_BOUND.md",
    "THEOREM_H_SUPPORT_RANK.md",
    "amplitude_order_oracle.py",
    "amplitude_order_oracle_receipt.json",
    "bautin_content_bridge_receipt.json",
    "build_candidate_manifest.py",
    "build_preprint.sh",
    "check_amplitude_order_oracle.py",
    "check_bautin_content_bridge.py",
    "check_candidate_package.py",
    "check_dickson_amplitude.py",
    "check_exceptional_amplitudes.py",
    "check_exceptional_channel_independence.py",
    "check_general_bautin_bound.py",
    "check_package_mutations.py",
    "check_standalone_weighted_order_oracle.py",
    "check_support_rank_reconstruction.py",
    "dickson_amplitude_receipt.json",
    "exceptional_amplitude_receipt.json",
    "exceptional_channel_independence_receipt.json",
    "general_bautin_bound_receipt.json",
    "preprint_filter.lua",
    "preprint_header.tex",
    "power_bautin_uniform_receipt.json",
    "package_mutation_receipt.json",
    "screen_power_bautin_uniform.py",
    "stage_candidate_package.py",
    "standalone_weighted_order_oracle.py",
    "standalone_weighted_order_receipt.json",
    "support_rank_reconstruction_receipt.json",
])

REVIEW_TARGETS = sorted([
    "BAUTIN_HOSTILE_REVIEW.md",
    "CANDIDATE_MANUSCRIPT.md",
    "EDITORIAL_01_EDITOR_IN_CHIEF.md",
    "EDITORIAL_02_METHODOLOGY_SPECIALIST.md",
    "EDITORIAL_03_DOMAIN_SPECIALIST.md",
    "EDITORIAL_04_APPLICATIONS_SPECIALIST.md",
    "EDITORIAL_05_DEVILS_ADVOCATE.md",
    "EDITORIAL_06_SYNTHESIS.md",
    "EDITORIAL_DISPOSITION.json",
    "ENVIRONMENT.txt",
    "LICENSE",
    "LICENSE-CODE",
    "LICENSES.md",
    "NOVELTY_AUDIT.md",
    "NOVELTY_GATE_REPORT.md",
    "NOVELTY_GATE_TARGETS.yaml",
    "PANEL_REVIEW_SYNTHESIS.md",
    "PUBLIC_DOMAIN.md",
    "PUBLIC_RELEASE_UNIT.md",
    "REPLAY_INPUTS.json",
    "REVIEW_RESPONSE_MATRIX.md",
    "SOURCE_CONVENTION_AUDIT.md",
    "SOURCE_PROVENANCE.json",
    "SUPPLEMENT_BINOMIAL_LAURENT.md",
    "THEOREM_0_MONODROMY_BLOCKS.md",
    "THEOREM_A_DICKSON.md",
    "THEOREM_B_EXCEPTIONAL_RITT.md",
    "THEOREM_C_WEIGHTED_ORDER.md",
    "THEOREM_D_BAUTIN_BOUND.md",
    "THEOREM_H_SUPPORT_RANK.md",
    "amplitude_order_oracle.py",
    "amplitude_order_oracle_receipt.json",
    "bautin_content_bridge_receipt.json",
    "check_bautin_content_bridge.py",
    "check_exceptional_channel_independence.py",
    "check_general_bautin_bound.py",
    "check_package_mutations.py",
    "check_support_rank_reconstruction.py",
    "exceptional_channel_independence_receipt.json",
    "general_bautin_bound_receipt.json",
    "power_bautin_uniform_receipt.json",
    "package_mutation_receipt.json",
    "screen_power_bautin_uniform.py",
    "standalone_weighted_order_oracle.py",
    "standalone_weighted_order_receipt.json",
    "support_rank_reconstruction_receipt.json",
])


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_manifest(root: Path) -> dict[str, object]:
    require(PACKAGE_FILES == sorted(set(PACKAGE_FILES)), (
        "package file list must be sorted and unique"
    ))
    require(REVIEW_TARGETS == sorted(set(REVIEW_TARGETS)), (
        "review target list must be sorted and unique"
    ))
    require(set(REVIEW_TARGETS).issubset(PACKAGE_FILES), (
        "every review target must be a package file"
    ))

    entries: list[dict[str, object]] = []
    hashes: dict[str, str] = {}
    for relative in PACKAGE_FILES:
        path = root / relative
        require(path.is_file() and not path.is_symlink(), (
            f"missing or unsafe package member: {relative}"
        ))
        digest = file_sha256(path)
        hashes[relative] = digest
        entries.append({
            "path": relative,
            "sha256": digest,
            "size_bytes": path.stat().st_size,
        })

    return {
        "atlas_upstream_package_sha256": ATLAS_SHA256,
        "claim_ceiling": (
            "local theorem-candidate package; not independent review, peer "
            "review, publication, or deployment authorization"
        ),
        "entries": entries,
        "package_allowlist": PACKAGE_FILES,
        "review_target_hashes": {
            name: hashes[name]
            for name in REVIEW_TARGETS
        },
        "schema": SCHEMA,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--replace",
        action="store_true",
        help="explicitly replace a differing existing manifest",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    output = (args.output or root / "PACKAGE_MANIFEST.json").resolve()
    require(output.parent == root, "manifest output must be in the package root")

    encoded = (
        json.dumps(build_manifest(root), indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")
    if output.exists():
        if output.read_bytes() == encoded:
            print(f"manifest unchanged: {file_sha256(output)}")
            return 0
        require(args.replace, (
            "manifest differs; rerun with --replace after reviewing package changes"
        ))

    with tempfile.NamedTemporaryFile(
        mode="wb",
        dir=root,
        prefix=".PACKAGE_MANIFEST.",
        delete=False,
    ) as handle:
        handle.write(encoded)
        temporary = Path(handle.name)
    os.replace(temporary, output)
    print(f"manifest written: {file_sha256(output)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
