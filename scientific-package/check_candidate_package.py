#!/usr/bin/env python3
"""Fail-closed integrity and replay checker for the candidate research package."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path, PurePosixPath
from typing import Any


sys.dont_write_bytecode = True


SCHEMA = "cyclicity-open-problems-candidate-manifest-v1"
RECEIPT_SCHEMA = "cyclicity-open-problems-candidate-integrity-v1"
NON_REPLAY_BOUNDARY = (
    "byte-identical computational replay was not requested or executed in this run"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def canonical_hash(value: object) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_claim_boundary(
    *,
    replay_requested: bool,
    replay_records: list[dict[str, object]],
    command_execution_count: int,
) -> dict[str, object]:
    """Describe only the assurance actually established by this checker run."""

    established = (
        "exact package-member identity, internal receipt integrity, and "
        "claim-boundary presence"
    )
    not_established = [
        "independent validity of the reconstructed support theorem",
        "historical novelty or priority",
        "independent review, peer review, or publication readiness",
        "independent status for any simulated referee report",
        "authorization to publish or deploy",
    ]
    if replay_requested:
        require(command_execution_count > 0, (
            "replay was requested but no replay command executed"
        ))
        require(replay_records, (
            "replay was requested but no replay artifact comparison was recorded"
        ))
        require(all(record.get("byte_identical") is True for record in replay_records), (
            "replay claim requires every retained artifact comparison to be byte-identical"
        ))
        established += (
            f", and byte-identical replay of {len(replay_records)} retained artifacts "
            f"from {command_execution_count} executed commands"
        )
    else:
        require(command_execution_count == 0, (
            "non-replay mode recorded an executed replay command"
        ))
        require(not replay_records, (
            "non-replay mode recorded a replay artifact comparison"
        ))
        not_established.insert(0, NON_REPLAY_BOUNDARY)
    return {
        "established": established,
        "not_established": not_established,
    }


def verify_replay_claim_consistency(receipt: dict[str, object]) -> None:
    """Fail closed if receipt prose and replay evidence disagree."""

    replay_requested = receipt.get("replay_requested")
    command_execution_count = receipt.get("command_execution_count")
    artifact_comparison_count = receipt.get("artifact_comparison_count")
    replay_records = receipt.get("replays")
    claim_boundary = receipt.get("claim_boundary")
    require(isinstance(replay_requested, bool), "receipt replay flag is invalid")
    require(isinstance(command_execution_count, int), (
        "receipt replay command count is invalid"
    ))
    require(isinstance(artifact_comparison_count, int), (
        "receipt replay artifact count is invalid"
    ))
    require(isinstance(replay_records, list), "receipt replay records are invalid")
    require(artifact_comparison_count == len(replay_records), (
        "receipt replay artifact count differs from its records"
    ))
    require(isinstance(claim_boundary, dict), "receipt claim boundary is invalid")
    established = claim_boundary.get("established")
    not_established = claim_boundary.get("not_established")
    require(isinstance(established, str), "receipt established claim is invalid")
    require(
        isinstance(not_established, list)
        and all(isinstance(item, str) for item in not_established),
        "receipt non-established claims are invalid",
    )

    if replay_requested:
        require(command_execution_count > 0 and artifact_comparison_count > 0, (
            "replay assurance requires executed commands and artifact comparisons"
        ))
        require("byte-identical replay" in established, (
            "executed replay is missing from the established claim"
        ))
        require(NON_REPLAY_BOUNDARY not in not_established, (
            "executed replay is incorrectly listed as not established"
        ))
    else:
        require(command_execution_count == 0 and artifact_comparison_count == 0, (
            "non-replay receipt contains replay execution evidence"
        ))
        require("replay" not in established.lower(), (
            "non-replay receipt must not claim replay"
        ))
        require(NON_REPLAY_BOUNDARY in not_established, (
            "non-replay receipt must disclose that replay was not executed"
        ))


def safe_member(root: Path, relative_text: str) -> Path:
    relative = Path(relative_text)
    require(relative_text == relative.as_posix(), f"non-canonical path: {relative_text}")
    require(not relative.is_absolute(), f"absolute path: {relative_text}")
    require(relative.parts and all(part not in {"", ".", ".."} for part in relative.parts), (
        f"unsafe path: {relative_text}"
    ))
    target = root.joinpath(relative)
    require(target.parent.resolve().is_relative_to(root.resolve()), (
        f"path escapes package root: {relative_text}"
    ))
    require(target.exists(), f"manifest member is missing: {relative_text}")
    require(target.is_file() and not target.is_symlink(), (
        f"manifest member must be a regular non-symlink file: {relative_text}"
    ))
    return target


def verify_embedded_digest(path: Path, field: str) -> str:
    value = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(value, dict), f"JSON receipt is not an object: {path.name}")
    supplied = value.get(field)
    require(isinstance(supplied, str), f"missing {field}: {path.name}")
    unhashed = dict(value)
    unhashed.pop(field, None)
    require(canonical_hash(unhashed) == supplied, f"invalid {field}: {path.name}")
    require(value.get("status") == "pass", f"non-passing receipt: {path.name}")
    return supplied


def verify_manifest(root: Path, manifest_path: Path) -> tuple[dict[str, Any], list[str]]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    require(isinstance(manifest, dict), "manifest must be a JSON object")
    require(set(manifest) == {
        "atlas_upstream_package_sha256",
        "claim_ceiling",
        "entries",
        "package_allowlist",
        "review_target_hashes",
        "schema",
    }, "manifest has missing or unknown top-level fields")
    require(manifest.get("schema") == SCHEMA, "unexpected manifest schema")
    require(
        isinstance(manifest.get("atlas_upstream_package_sha256"), str)
        and len(manifest["atlas_upstream_package_sha256"]) == 64,
        "invalid Atlas archive SHA-256",
    )
    require(isinstance(manifest.get("claim_ceiling"), str), "claim ceiling is missing")
    entries = manifest.get("entries")
    require(isinstance(entries, list) and entries, "manifest entries are missing")

    paths: list[str] = []
    for entry in entries:
        require(isinstance(entry, dict), "manifest entry must be an object")
        require(set(entry) == {"path", "sha256", "size_bytes"}, (
            "manifest entry has missing or unknown fields"
        ))
        relative_text = entry.get("path")
        expected_sha = entry.get("sha256")
        expected_size = entry.get("size_bytes")
        require(isinstance(relative_text, str), "manifest entry path is missing")
        require(isinstance(expected_sha, str) and len(expected_sha) == 64, (
            f"invalid SHA-256 for {relative_text}"
        ))
        require(isinstance(expected_size, int) and expected_size >= 0, (
            f"invalid size for {relative_text}"
        ))
        target = safe_member(root, relative_text)
        require(target.stat().st_size == expected_size, f"size mismatch: {relative_text}")
        require(file_sha256(target) == expected_sha, f"SHA-256 mismatch: {relative_text}")
        paths.append(relative_text)

    require(paths == sorted(paths), "manifest entries are not path-sorted")
    require(len(paths) == len(set(paths)), "manifest contains duplicate paths")

    declared = manifest.get("package_allowlist")
    require(declared == paths, "package allowlist differs from entry paths")
    require("PACKAGE_MANIFEST.json" not in paths, "manifest may not hash itself")
    from build_candidate_manifest import PACKAGE_FILES  # noqa: PLC0415
    require(paths == PACKAGE_FILES, (
        "manifest allowlist differs from the canonical package builder"
    ))

    entry_hashes = {
        entry["path"]: entry["sha256"]
        for entry in entries
    }
    review_targets = manifest.get("review_target_hashes")
    require(isinstance(review_targets, dict) and review_targets, (
        "review target hashes are missing"
    ))
    require(list(review_targets) == sorted(review_targets), (
        "review target hashes are not path-sorted"
    ))
    for name, expected_sha in review_targets.items():
        require(isinstance(name, str) and isinstance(expected_sha, str), (
            "invalid review target entry"
        ))
        require(entry_hashes.get(name) == expected_sha, (
            f"review target differs from manifest entry: {name}"
        ))
    return manifest, paths


def verify_exact_root(root: Path, paths: list[str]) -> None:
    """Reject every object outside the two documented release-stage sets."""

    actual: set[str] = set()
    for member in root.iterdir():
        require(member.is_file() and not member.is_symlink(), (
            f"unexpected non-regular package-root object: {member.name}"
        ))
        actual.add(member.name)
    base = set(paths) | {"PACKAGE_MANIFEST.json"}
    require(frozenset(actual) in {
        frozenset(base),
        frozenset(base | {"PACKAGE_INTEGRITY_RECEIPT.json"}),
    }, (
        "package root contains undeclared or missing release members"
    ))


def extract_verified_atlas(
    archive: Path,
    expected_sha256: str,
    destination: Path,
) -> Path:
    """Verify and safely extract the frozen Atlas archive."""

    require(archive.is_file() and not archive.is_symlink(), (
        f"Atlas archive is missing or unsafe: {archive}"
    ))
    require(file_sha256(archive) == expected_sha256, (
        "Atlas archive SHA-256 differs from the manifest"
    ))
    destination.mkdir(parents=True, exist_ok=False)
    with zipfile.ZipFile(archive) as handle:
        seen_members: set[str] = set()
        for info in handle.infolist():
            relative = PurePosixPath(info.filename)
            require(
                info.filename == relative.as_posix()
                and not relative.is_absolute()
                and relative.parts
                and all(part not in {"", ".", ".."} for part in relative.parts),
                f"unsafe Atlas archive member: {info.filename}",
            )
            require(info.filename not in seen_members, (
                f"duplicate Atlas archive member: {info.filename}"
            ))
            seen_members.add(info.filename)
            mode = info.external_attr >> 16
            require((mode & 0o170000) != 0o120000, (
                f"Atlas archive symlink is forbidden: {info.filename}"
            ))
            target = destination.joinpath(*relative.parts)
            require(target.resolve().is_relative_to(destination.resolve()), (
                f"Atlas archive member escapes extraction root: {info.filename}"
            ))
            if info.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            with handle.open(info) as source, target.open("wb") as sink:
                shutil.copyfileobj(source, sink)

    candidates = [
        candidate.parent.parent
        for candidate in destination.rglob("src/amplitude_support.py")
    ]
    require(len(candidates) == 1, (
        "verified Atlas archive must contain exactly one src/amplitude_support.py"
    ))
    return candidates[0]


def run_and_compare(
    command: list[str],
    *,
    root: Path,
    generated: Path,
    expected: Path,
    reported_replacements: dict[str, str] | None = None,
) -> dict[str, object]:
    completed = subprocess.run(
        command,
        cwd=root,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        check=False,
        capture_output=True,
        text=True,
    )
    require(completed.returncode == 0, (
        f"replay failed ({completed.returncode}): {' '.join(command)}\n"
        f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}"
    ))
    require(generated.read_bytes() == expected.read_bytes(), (
        f"replay bytes differ: {expected.name}"
    ))
    replacements = {
        str(generated): "<REPLAY_OUTPUT>",
        sys.executable: "<PYTHON>",
    }
    replacements.update(reported_replacements or {})
    reported_command = [replacements.get(argument, argument) for argument in command]
    return {
        "expected_path": expected.name,
        "expected_sha256": file_sha256(expected),
        "command": reported_command,
        "byte_identical": True,
    }


def replay_receipts(
    root: Path,
    atlas_archive: Path,
    atlas_sha256: str,
) -> tuple[list[dict[str, object]], int]:
    records: list[dict[str, object]] = []
    with tempfile.TemporaryDirectory(prefix="cyclicity-package-replay-") as temporary:
        replay_root = Path(temporary)
        atlas_root = extract_verified_atlas(
            atlas_archive,
            atlas_sha256,
            replay_root / "verified-atlas",
        )
        reported_replacements = {
            str(root): "<PACKAGE_ROOT>",
            str(atlas_root): "<VERIFIED_ATLAS_ROOT>",
            str(atlas_archive): "<ATLAS_ARCHIVE>",
        }
        jobs = [
            (
                [
                    sys.executable,
                    "check_support_rank_reconstruction.py",
                    "--depth",
                    "48",
                    "--output",
                    str(replay_root / "support-rank.json"),
                ],
                replay_root / "support-rank.json",
                root / "support_rank_reconstruction_receipt.json",
            ),
            (
                [
                    sys.executable,
                    "-O",
                    "check_support_rank_reconstruction.py",
                    "--depth",
                    "48",
                    "--output",
                    str(replay_root / "support-rank-optimized.json"),
                ],
                replay_root / "support-rank-optimized.json",
                root / "support_rank_reconstruction_receipt.json",
            ),
            (
                [
                    sys.executable,
                    "check_dickson_amplitude.py",
                    "--atlas-root",
                    str(atlas_root),
                    "--maximum-degree",
                    "9",
                    "--output",
                    str(replay_root / "dickson.json"),
                ],
                replay_root / "dickson.json",
                root / "dickson_amplitude_receipt.json",
            ),
            (
                [
                    sys.executable,
                    "check_exceptional_amplitudes.py",
                    "--atlas-root",
                    str(atlas_root),
                    "--output",
                    str(replay_root / "exceptional.json"),
                ],
                replay_root / "exceptional.json",
                root / "exceptional_amplitude_receipt.json",
            ),
            (
                [
                    sys.executable,
                    "check_exceptional_channel_independence.py",
                    "--max-coefficient-degree",
                    "6",
                    "--output",
                    str(replay_root / "channels.json"),
                ],
                replay_root / "channels.json",
                root / "exceptional_channel_independence_receipt.json",
            ),
            (
                [
                    sys.executable,
                    "check_bautin_content_bridge.py",
                    "--output",
                    str(replay_root / "bautin-content-bridge.json"),
                ],
                replay_root / "bautin-content-bridge.json",
                root / "bautin_content_bridge_receipt.json",
            ),
            (
                [
                    sys.executable,
                    "check_general_bautin_bound.py",
                    "--output",
                    str(replay_root / "general-bautin.json"),
                ],
                replay_root / "general-bautin.json",
                root / "general_bautin_bound_receipt.json",
            ),
            (
                [
                    sys.executable,
                    "check_package_mutations.py",
                    "--root",
                    str(root),
                    "--atlas-archive",
                    str(atlas_archive),
                    "--output",
                    str(replay_root / "package-mutations.json"),
                ],
                replay_root / "package-mutations.json",
                root / "package_mutation_receipt.json",
            ),
            (
                [
                    sys.executable,
                    "screen_power_bautin_uniform.py",
                    "--output",
                    str(replay_root / "power-bautin.json"),
                ],
                replay_root / "power-bautin.json",
                root / "power_bautin_uniform_receipt.json",
            ),
            (
                [
                    sys.executable,
                    "check_amplitude_order_oracle.py",
                    "--atlas-root",
                    str(atlas_root),
                    "--output",
                    str(replay_root / "producer.json"),
                ],
                replay_root / "producer.json",
                root / "amplitude_order_oracle_receipt.json",
            ),
            (
                [
                    sys.executable,
                    "check_standalone_weighted_order_oracle.py",
                    "--producer-receipt",
                    "amplitude_order_oracle_receipt.json",
                    "--output",
                    str(replay_root / "standalone.json"),
                ],
                replay_root / "standalone.json",
                root / "standalone_weighted_order_receipt.json",
            ),
            (
                [
                    sys.executable,
                    "-O",
                    "check_standalone_weighted_order_oracle.py",
                    "--producer-receipt",
                    "amplitude_order_oracle_receipt.json",
                    "--output",
                    str(replay_root / "standalone-optimized.json"),
                ],
                replay_root / "standalone-optimized.json",
                root / "standalone_weighted_order_receipt.json",
            ),
        ]
        for command, generated, expected in jobs:
            records.append(run_and_compare(
                command,
                root=root,
                generated=generated,
                expected=expected,
                reported_replacements=reported_replacements,
            ))

        preprint_root = replay_root / "preprint"
        preprint_command = ["bash", "build_preprint.sh", str(preprint_root)]
        completed = subprocess.run(
            preprint_command,
            cwd=root,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            check=False,
            capture_output=True,
            text=True,
        )
        require(completed.returncode == 0, (
            f"preprint replay failed ({completed.returncode})\n"
            f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}"
        ))
        for name in ["CANDIDATE_PREPRINT.tex", "CANDIDATE_PREPRINT.pdf"]:
            generated = preprint_root / name
            expected = root / name
            require(generated.read_bytes() == expected.read_bytes(), (
                f"preprint replay bytes differ: {name}"
            ))
            records.append({
                "expected_path": name,
                "expected_sha256": file_sha256(expected),
                "command": ["bash", "build_preprint.sh", "<REPLAY_OUTPUT_DIR>"],
                "byte_identical": True,
            })
    return records, len(jobs) + 1


def check_package(
    root: Path,
    *,
    replay: bool,
    atlas_archive: Path | None,
    exact_root: bool,
) -> dict[str, object]:
    manifest_path = root / "PACKAGE_MANIFEST.json"
    manifest, paths = verify_manifest(root, manifest_path)
    if exact_root:
        verify_exact_root(root, paths)

    receipt_fields = {
        "amplitude_order_oracle_receipt.json": "receipt_sha256",
        "dickson_amplitude_receipt.json": "receipt_sha256",
        "exceptional_amplitude_receipt.json": "receipt_sha256",
        "exceptional_channel_independence_receipt.json": "receipt_sha256",
        "bautin_content_bridge_receipt.json": "receipt_sha256",
        "general_bautin_bound_receipt.json": "receipt_sha256",
        "package_mutation_receipt.json": "receipt_sha256",
        "power_bautin_uniform_receipt.json": "receipt_sha256",
        "standalone_weighted_order_receipt.json": "receipt_sha256",
        "support_rank_reconstruction_receipt.json": "receipt_sha256",
    }
    embedded = {
        name: verify_embedded_digest(root / name, field)
        for name, field in receipt_fields.items()
    }

    required_phrases = {
        "CANDIDATE_MANUSCRIPT.md": [
            "**Candidate version:** 2026-08-28-r2",
            "**Author:** Anonymous",
            "Theorem 2.1 (polynomial-amplitude support identity)",
            "Lemma 2.2 (equivariant span and generic specialization)",
            "Lemma 2.3 (standard-ray flat family and Fourier pairing)",
            "[6, Theorems 2.2(1) and 2.3(1)]",
            "is nonintegral",
            "whole falling-factorial matrix",
            "leading matrix has full rank",
            "No generic-individual-period claim is made",
            "Theorem C (ordinary coefficient Bautin bound)",
            "Proposition 6.1 (content equals the local Taylor-coefficient ideal)",
            "source-style coefficient ideal",
            "arbitrary fixed degree",
            "b_{\\mathrm{coeff}}(m)\\le m-1",
        ],
        "EDITORIAL_DISPOSITION.json": [
            "MAJOR_REVISION_HOLD_FOR_REPAIR",
            "internal_model_mediated_editorial_review",
            "implementation_complete_pending_rebuild_and_preflight",
        ],
        "ENVIRONMENT.txt": [
            "locale=C.UTF-8",
            "sympy=1.14.0",
            "toolchain_class=recorded-host-not-hermetic-container",
        ],
        "LICENSES.md": [
            "CC0-1.0",
            "Reference-only",
            "NOASSERTION",
        ],
        "PUBLIC_RELEASE_UNIT.md": [
            "whole-history public release unit",
            "explicit top-level allowlist",
            "does not prove",
        ],
        "REPLAY_INPUTS.json": [
            "AUTHORIZED_UNMODIFIED_SEPARATE_RELEASE_ASSET",
            "separate_release_asset",
            "3a132530f31c1af3870de7af7a13d41389ffbf051ab2760b3c0110173c268e8a",
        ],
        "REVIEW_RESPONSE_MATRIX.md": [
            "R1 — root-span/monodromy equivalence",
            "R9 — reader/accessibility layer",
            "No further ordinary model-review round is",
        ],
        "SOURCE_CONVENTION_AUDIT.md": [
            "ordinary parameter-content",
            "conditional on the source intending",
            "forbids an unconditional statement",
        ],
        "SOURCE_PROVENANCE.json": [
            "AUTHORIZED_REFERENCE_ONLY_NOT_REDISTRIBUTED",
            "arxiv-1108.4508v2-source",
            "arxiv-1301.4313v2-source",
        ],
        "BAUTIN_HOSTILE_REVIEW.md": [
            "PROOF SURVIVES",
            "full degree box",
            "monodromy-injectivity",
            "independent specialist review",
        ],
        "STATUS.md": [
            "no independent human specialist review has occurred",
            "explicitly anonymous unrefereed candidate only",
            "b_coeff(m) <= m-1",
        ],
        "BILINGUAL_ABSTRACT.md": [
            "candidate presentation material",
            "ordinary local Taylor-coefficient ideal",
            "繁體中文",
        ],
        "NOVELTY_GATE_REPORT.md": [
            "BOUNDED UNCERTAINTY",
            "BRIDGE",
            "COLLISION",
            "Forbidden wording",
        ],
        "REFEREE_CONFIGURATION.md": [
            "panel authorized",
            "Reports generated:** five simulated perspectives",
            "not independent validation",
        ],
        "PANEL_REVIEW_SYNTHESIS.md": [
            "MAJOR REVISION",
            "The exercise is not independent human",
            "HOLD FROM RELEASE",
        ],
    }
    for name, phrases in required_phrases.items():
        content = (root / name).read_text(encoding="utf-8")
        for phrase in phrases:
            require(phrase in content, f"required claim boundary missing in {name}: {phrase}")

    forbidden_phrases = {
        "CANDIDATE_MANUSCRIPT.md": [
            "**Authors:**",
            "Fa" "ble",
            "Author " "contributions",
            "## 13. " "Fund" "ing",
            "Competing " "interests",
            "AI-assistance",
        ],
        "CANDIDATE_PREPRINT.tex": [
            "Anonymous manuscript for review",
            "Fa" "ble",
            "\\section{Author " "contributions}",
            "\\section{" "Fund" "ing}",
            "\\section{Competing " "interests}",
            r"\section{AI-assistance",
        ],
    }
    for name, phrases in forbidden_phrases.items():
        content = (root / name).read_text(encoding="utf-8")
        for phrase in phrases:
            require(phrase not in content, (
                f"forbidden publication text present in {name}: {phrase}"
            ))

    text_suffixes = {".json", ".lua", ".md", ".py", ".sh", ".tex", ".txt", ".yaml"}
    public_forbidden = [
        "Fa" "ble",
        "Author " "contributions",
        "Competing " "interests",
        "AI-Assistance " "Disclosure",
    ]
    for relative in paths:
        path = root / relative
        if path.suffix.lower() not in text_suffixes and path.name not in {"LICENSE"}:
            continue
        content = path.read_text(encoding="utf-8")
        for phrase in public_forbidden:
            require(phrase not in content, (
                f"forbidden public-package text present in {relative}: {phrase}"
            ))

    replay_records: list[dict[str, object]] = []
    command_execution_count = 0
    if replay:
        require(atlas_archive is not None, "--atlas-archive is required with --replay")
        replay_records, command_execution_count = replay_receipts(
            root,
            atlas_archive,
            manifest["atlas_upstream_package_sha256"],
        )

    result: dict[str, object] = {
        "schema": RECEIPT_SCHEMA,
        "status": "pass",
        "manifest_sha256": file_sha256(manifest_path),
        "manifest_entry_count": len(paths),
        "package_allowlist_verified": True,
        "exact_release_root_verified": exact_root,
        "embedded_receipt_digests": embedded,
        "replay_requested": replay,
        "artifact_comparison_count": len(replay_records),
        "command_execution_count": command_execution_count,
        "replays": replay_records,
        "claim_boundary": build_claim_boundary(
            replay_requested=replay,
            replay_records=replay_records,
            command_execution_count=command_execution_count,
        ),
    }
    verify_replay_claim_consistency(result)
    result["receipt_sha256"] = canonical_hash(result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--replay", action="store_true")
    parser.add_argument("--atlas-archive", type=Path)
    parser.add_argument("--exact-root", action="store_true")
    parser.add_argument("--verify-stored-receipt", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    root = args.root.resolve()
    result = check_package(
        root,
        replay=args.replay,
        atlas_archive=args.atlas_archive,
        exact_root=args.exact_root,
    )
    if args.verify_stored_receipt:
        stored_path = root / "PACKAGE_INTEGRITY_RECEIPT.json"
        require(stored_path.is_file() and not stored_path.is_symlink(), (
            "stored package-integrity receipt is missing or unsafe"
        ))
        stored = json.loads(stored_path.read_text(encoding="utf-8"))
        require(stored == result, "stored package-integrity receipt is stale")
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=args.output.parent,
            prefix=f".{args.output.name}.",
            delete=False,
        ) as handle:
            handle.write(encoded)
            temporary = Path(handle.name)
        os.replace(temporary, args.output)
    else:
        print(encoded, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
