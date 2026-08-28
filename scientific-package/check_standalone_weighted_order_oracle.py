#!/usr/bin/env python3
"""Cross-check the standalone weighted oracle against producer receipts."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

from standalone_weighted_order_oracle import (
    canonical_hash,
    certificate_for,
    verify_certificate,
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--producer-receipt", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    producer = json.loads(args.producer_receipt.read_text(encoding="utf-8"))
    require(
        producer.get("schema") == "polynomial-amplitude-order-oracle-test-receipt-v1",
        "unexpected producer receipt schema",
    )
    records: list[dict[str, object]] = []
    certificates: list[dict[str, object]] = []
    for expected in producer["records"]:
        certificate = certificate_for(expected["phase"], expected["amplitude"])
        certificates.append(certificate)
        operator = certificate["operator"]
        require(operator["order"] == expected["order"], (
            f"order disagreement: {expected['label']}"
        ))
        require(operator["coefficients"] == expected["operator_coefficients"], (
            f"operator disagreement: {expected['label']}"
        ))
        verification = verify_certificate(certificate)
        require(verification["status"] == "pass", (
            f"replay failed: {expected['label']}"
        ))
        records.append({
            "label": expected["label"],
            "phase": expected["phase"],
            "amplitude": expected["amplitude"],
            "order": operator["order"],
            "operator_coefficients": operator["coefficients"],
            "producer_operator_agrees": True,
            "standalone_certificate_sha256": certificate["certificate_sha256"],
        })

    mutated = copy.deepcopy(certificates[0])
    mutated["operator"]["coefficients"][0] = "2"
    mutated.pop("certificate_sha256")
    mutated["certificate_sha256"] = canonical_hash(mutated)
    mutation_rejected = False
    try:
        verify_certificate(mutated)
    except RuntimeError:
        mutation_rejected = True
    require(mutation_rejected, "rehashed semantic mutation was accepted")

    receipt: dict[str, object] = {
        "schema": "standalone-weighted-period-order-crosscheck-v1",
        "status": "pass",
        "producer_receipt_name": args.producer_receipt.name,
        "producer_receipt_file_sha256": file_sha256(args.producer_receipt),
        "case_count": len(records),
        "records": records,
        "producer_operator_agreement_count": len(records),
        "semantic_mutations_rejected": 1,
        "claim_boundary": {
            "established": (
                "second-program exact reconstruction and coefficient-level "
                "agreement for every producer test case"
            ),
            "not_established": [
                "independent human or institutional reproduction",
                "novelty, specialist review, or publication readiness",
            ],
        },
    }
    receipt["receipt_sha256"] = canonical_hash(receipt)
    encoded = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
    else:
        print(encoded, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
