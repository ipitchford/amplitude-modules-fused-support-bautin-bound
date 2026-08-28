#!/usr/bin/env python3
"""Regression and mutation controls for the amplitude order oracle."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

from amplitude_order_oracle import (
    amplitude_order_certificate,
    load_atlas,
    verify_amplitude_order_certificate,
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--atlas-root", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    atlas = load_atlas(args.atlas_root)
    cases = (
        ("x**7", "1", 1, {1}, "power seed"),
        ("x**7", "7*x**6", 0, set(), "rank-zero exact amplitude"),
        ("x**5-5*x**3+5*x", "1", 2, {1, 4}, "Dickson seed"),
        ("(x**4+x)**3", "4*x**3", 4, {1, 4, 7, 10}, "rank-four exceptional amplitude"),
        ("(x**4+x)**3", "7*x**6+7*x**3", 3, {1, 7, 10}, "fused exceptional amplitude"),
        ("(x**4+x)**3", "4*x**3+1", 1, {4}, "quartic-factor amplitude"),
        ("(x+2)**4+(x+2)", "1", 3, {1, 2, 3}, "affine transport"),
    )

    records: list[dict[str, object]] = []
    certificates: list[dict[str, object]] = []
    for phase, amplitude, expected_order, expected_support, label in cases:
        certificate = amplitude_order_certificate(phase, amplitude, args.atlas_root, atlas)
        certificates.append(certificate)
        order = certificate["scalar_operator_for_original_inputs"]["order"]
        support = set(certificate["order_prediction"]["primitive_inverse_support"])
        require(order == expected_order, f"order failed: {label}: {order}")
        require(support == expected_support, f"support failed: {label}: {support}")
        verification = verify_amplitude_order_certificate(certificate, args.atlas_root, atlas)
        require(verification["status"] == "pass", f"verification failed: {label}")
        records.append(
            {
                "label": label,
                "phase": phase,
                "amplitude": amplitude,
                "order": order,
                "support": sorted(support),
                "operator_coefficients": certificate["scalar_operator_for_original_inputs"]["coefficients"],
                "certificate_sha256": certificate["certificate_sha256"],
            }
        )

    # Recompute the outer digest after corrupting an operator coefficient.  A
    # verifier that checked only byte integrity would accept this mutation;
    # exact recomputation must reject it.
    mutated = copy.deepcopy(certificates[0])
    mutated["scalar_operator_for_original_inputs"]["coefficients"][0] = "2"
    mutated.pop("certificate_sha256")
    mutated["certificate_sha256"] = atlas["canonical_hash"](mutated)
    mutation_rejected = False
    try:
        verify_amplitude_order_certificate(mutated, args.atlas_root, atlas)
    except RuntimeError:
        mutation_rejected = True
    require(mutation_rejected, "rehashed operator mutation was not rejected")

    receipt: dict[str, object] = {
        "schema": "polynomial-amplitude-order-oracle-test-receipt-v1",
        "status": "pass",
        "case_count": len(records),
        "records": records,
        "semantic_mutations_rejected": 1,
        "claim_boundary": {
            "established": "exact same-programme operator construction, residual checks, replay, and mutation rejection",
            "not_established": [
                "independent implementation",
                "individual-cycle minimality",
                "novelty, priority, specialist review, or publication readiness",
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

