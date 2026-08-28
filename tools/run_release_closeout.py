#!/usr/bin/env python3
"""Validate confirmation conditions and emit a deterministic closeout receipt."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path


sys.dont_write_bytecode = True


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


class StructureParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.h1 = 0
        self.main = 0
        self.math = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "h1":
            self.h1 += 1
        elif tag == "main":
            self.main += 1
        elif tag == "math":
            self.math += 1


def load_json(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(value, dict), f"expected JSON object: {path}")
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--recorded-at", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output.resolve()
    require(root.is_dir(), "public release root is missing")
    require(not output.exists(), "refusing to overwrite closeout receipt")

    binding = load_json(root / "RELEASE_BINDING.json")
    require(binding.get("schema") == "evidence-press-release-binding-v1", "release binding schema differs")
    require(binding["editorial_closeout"]["final_disposition"] == "accepted_for_anonymous_unrefereed_candidate", "final disposition differs")
    require(binding["editorial_closeout"]["further_model_review_used"] is False, "unexpected further review")

    expected_hashes = {
        "release-assets/amplitude-modules-fused-support-bautin-bound-v0.1.0-candidate-r2.zip": "aa1e73f62ccb89bae6ff00aaee844721172eca515d4da64c4c41539e51977b13",
        "release-assets/CANDIDATE_PREPRINT.html": "b9e4a0751cab2fe05fc121dc255e0d3bc7a345c8b4cea1988ef4693ce9db5277",
        "scientific-package/CANDIDATE_PREPRINT.pdf": "5a4c00f34873e9a0c691ce375a40f78449b671b9fe2bdfcfe1ea7deead4ebb99",
        "scientific-package/PACKAGE_MANIFEST.json": "699e07bf26cfbc4d4c4f6a9ed21cb3bee3b543d5a331d3fbecdc4d4301b4c186",
        "scientific-package/PACKAGE_INTEGRITY_RECEIPT.json": "979e976b1f57220d86cdc56ae7334bf5755ea5b64308870d085f987ec93b10a0",
        "evidence/junit/ordinary.xml": "627092c7a57eaf32d5bd6b79420e5a96f6314688208e882b6cdcd88e458c2882",
        "evidence/junit/optimized.xml": "29320033cdee706a27fd3e4076eede9890fd5cf169c42e61e9715c85c2afa94a",
        "evidence/junit/junit-parity.json": "4b6e51616a935e6b22073a3065d562878d5a19b13931180791e4fbfc6997cddb",
        "evidence/editorial/07_CONFIRMATION_R2.md": "05a876e92465ef6b628b1913ec4fb56a66727ed24715ced28601972239713d0e",
        "evidence/deterministic/amplitude-modules-r2-fast-gates.json": "10c7c449fbd6f865166c23a888da4b6eaebb4747a779dc3a189c6effb5044920",
        "evidence/deterministic/amplitude-modules-r2-fast-gates-receipt.json": "519a14c21672d8ab987f061ad7861b92130ea436ac08f34c919dc5468a8c1583"
    }
    for relative, digest in expected_hashes.items():
        require(sha256(root / relative) == digest, f"release asset digest differs: {relative}")

    parity = load_json(root / "evidence/junit/junit-parity.json")
    require(parity.get("status") == "pass", "JUnit parity receipt did not pass")
    require(parity.get("aggregate") == {"errors": 0, "failures": 0, "skipped": 0, "tests": 9}, "JUnit aggregate differs")
    require(len(parity.get("testcase_inventory", [])) == 9, "JUnit testcase inventory differs")

    html = (root / "release-assets/CANDIDATE_PREPRINT.html").read_text(encoding="utf-8")
    structure = StructureParser()
    structure.feed(html)
    require(structure.h1 == 1 and structure.main == 1 and structure.math > 0, "accessible HTML structure differs")
    required_phrases = [
        "Anonymous unrefereed theorem candidate",
        "no independent specialist review",
        "does not claim that three historically posed open problems have been solved",
    ]
    require(all(phrase in html for phrase in required_phrases), "accessible HTML assurance language differs")

    for optimize in [False, True]:
        command = [sys.executable]
        if optimize:
            command.append("-O")
        command.extend(["scientific-package/check_candidate_package.py", "--root", "scientific-package", "--exact-root"])
        completed = subprocess.run(command, cwd=root, check=False, capture_output=True, text=True)
        require(completed.returncode == 0, completed.stderr[-1000:])
        receipt = json.loads(completed.stdout)
        require(receipt.get("status") == "pass" and receipt.get("replay_requested") is False, "package semantics check differs")

    status_text = (root / "STATUS.md").read_text(encoding="utf-8")
    licence_text = (root / "LICENSES.md").read_text(encoding="utf-8")
    require("accepted for publication as an anonymous unrefereed Evidence Press" in status_text, "release status is not reconciled")
    require("CC0-1.0" in licence_text and "MIT" in licence_text, "licence map is incomplete")

    receipt = {
        "case_id": binding["case_id"],
        "checks": {
            "accessible_html": "pass",
            "asset_hashes": "pass",
            "claim_ceiling": "pass",
            "junit_parity": "pass",
            "licence_and_status": "pass",
            "ordinary_package_semantics": "pass",
            "optimized_package_semantics": "pass",
            "release_binding": "pass"
        },
        "claim_id": binding["claim_id"],
        "content_commit": binding["public_content"]["content_commit"],
        "content_tree": binding["public_content"]["content_tree"],
        "recorded_at": args.recorded_at,
        "schema": "evidence-press-release-closeout-v1",
        "status": "pass",
        "target_sha256": binding["review_target"]["reviewed_archive_sha256"]
    }
    encoded = (json.dumps(receipt, indent=2, sort_keys=True) + "\n").encode("utf-8")
    receipt["receipt_sha256"] = hashlib.sha256(encoded).hexdigest()
    encoded = (json.dumps(receipt, indent=2, sort_keys=True) + "\n").encode("utf-8")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="wb", dir=output.parent, prefix=f".{output.name}.", delete=False) as handle:
        handle.write(encoded)
        temporary = Path(handle.name)
    os.replace(temporary, output)
    print(f"status=pass receipt_sha256={sha256(output)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
