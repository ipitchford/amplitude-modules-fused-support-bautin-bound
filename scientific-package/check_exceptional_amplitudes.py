#!/usr/bin/env python3
"""Falsification battery for low-rank amplitudes of (x^4+x)^3.

The proposed C[P]-module decomposition uses Q=x^4+x and P=Q^3:

    C[x] = C[Q] direct_sum M0 direct_sum M1 direct_sum M2,

where

    M0 = C[P] <x, x^7+7x^4/4, x^10-5x^4/2>,
    M1 = C[P] <x^2, x^5, x^11+11x^8/4>,
    M2 = C[P] <x^3, x^6, x^9>.

The predicted non-trace supports are {4,8} for C[Q]/C[P] and the
three disjoint triples {1,7,10}, {2,5,11}, {3,6,9} for M0, M1, M2.
Consequently a primitive has induced rank at most three exactly when, modulo
C[P], it lies in C[Q]/C[P] or in one Mi alone.

This script attacks the prediction with exact Atlas Krylov and inverse-series
calculations.  It is not a proof of the module decomposition or novelty.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

import sympy as sp


x = sp.Symbol("x")
Q = x**4 + x
P = sp.expand(Q**3)

SUPPORT_Q = {4, 8}
SUPPORTS = (
    {1, 7, 10},
    {2, 5, 11},
    {3, 6, 9},
)

M0 = (x, x**7 + sp.Rational(7, 4) * x**4, x**10 - sp.Rational(5, 2) * x**4)
M1 = (x**2, x**5, x**11 + sp.Rational(11, 4) * x**8)
M2 = (x**3, x**6, x**9)
MODULES = (M0, M1, M2)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def analyse_case(analyse_amplitude, primitive: sp.Expr, support: set[int], label: str) -> dict[str, object]:
    primitive = sp.expand(primitive)
    amplitude = sp.diff(primitive, x)
    result = analyse_amplitude(sp.sstr(P), sp.sstr(amplitude))
    observed = set(result["primitive_inverse_at_infinity"]["support"])
    rank = result["theorem_identity"]["twisted_amplitude_cyclic_rank"]
    require(result["theorem_identity"]["all_equal"] is True, f"identity failed: {label}")
    require(observed == support, f"support failed: {label}: {observed}")
    require(rank == len(support), f"rank failed: {label}: {rank}")
    return {
        "label": label,
        "primitive": sp.sstr(primitive),
        "expected_support": sorted(support),
        "observed_support": sorted(observed),
        "observed_rank": rank,
        "atlas_certificate_sha256": result["certificate_sha256"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--atlas-root", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    source_root = args.atlas_root / "src"
    require(source_root.is_dir(), "Atlas src directory is missing")
    sys.path.insert(0, str(source_root))
    from amplitude_support import analyse_amplitude  # noqa: PLC0415

    records: list[dict[str, object]] = []

    # Canonical generators and deterministic within-module combinations.
    for module_index, (module, support) in enumerate(zip(MODULES, SUPPORTS, strict=True)):
        for generator_index, generator in enumerate(module):
            records.append(
                analyse_case(
                    analyse_amplitude,
                    generator,
                    support,
                    f"M{module_index}:generator-{generator_index}",
                )
            )
        combinations = (
            module[0] + 2 * module[1] - module[2],
            (P + 1) * module[0] + (2 * P - 3) * module[1] + 5 * module[2],
        )
        for combination_index, primitive in enumerate(combinations):
            records.append(
                analyse_case(
                    analyse_amplitude,
                    primitive,
                    support,
                    f"M{module_index}:combination-{combination_index}",
                )
            )

    # The proper-composition summand has the two singleton channels generated
    # by Q and Q^2.  Polynomial coefficients in P preserve those residues.
    records.append(analyse_case(analyse_amplitude, Q, {4}, "C[Q]:Q"))
    records.append(analyse_case(analyse_amplitude, Q**2, {8}, "C[Q]:Q^2"))
    records.append(
        analyse_case(
            analyse_amplitude,
            (P + 2) * Q + (2 * P - 1) * Q**2,
            SUPPORT_Q,
            "C[Q]:two-channel-combination",
        )
    )

    # Cross-summand attacks must add disjoint supports, hence exceed rank 3.
    cross_cases = (
        (M0[0] + M1[0], SUPPORTS[0] | SUPPORTS[1], "M0+M1"),
        (M0[1] + M2[1], SUPPORTS[0] | SUPPORTS[2], "M0+M2"),
        (M1[2] + M2[2], SUPPORTS[1] | SUPPORTS[2], "M1+M2"),
        (M0[0] + Q, SUPPORTS[0] | {4}, "M0+Q"),
        (M1[0] + Q**2, SUPPORTS[1] | {8}, "M1+Q^2"),
    )
    for primitive, support, label in cross_cases:
        records.append(analyse_case(analyse_amplitude, primitive, support, label))

    # The displayed twelve generators have distinct leading degrees 0,...,11,
    # so their coefficient matrix over Q[P] is triangular and invertible.
    basis = (sp.Integer(1), Q, Q**2, *M0, *M1, *M2)
    degrees = sorted(sp.Poly(value, x).degree() for value in basis)
    require(degrees == list(range(12)), f"unexpected generator degrees: {degrees}")

    receipt: dict[str, object] = {
        "schema": "exceptional-ritt-amplitude-falsification-v1",
        "status": "pass",
        "phase": sp.sstr(P),
        "inner_quartic": sp.sstr(Q),
        "basis_degrees": degrees,
        "case_count": len(records),
        "records": records,
        "claim_boundary": {
            "established": "bounded exact agreement with Atlas Krylov and inverse-support calculations",
            "not_established": [
                "the all-amplitude iff classification",
                "irreducibility of each displayed fused summand",
                "independent implementation",
                "novelty, priority, review, or publication readiness",
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

