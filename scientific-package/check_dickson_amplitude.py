#!/usr/bin/env python3
"""Exact falsification battery for the Dickson amplitude-module conjecture.

For the monic Dickson phase P = D_d(x, a), with a nonzero rational parameter,
the proposed decomposition says that a nonzero primitive in

    Q[P] D_j + Q[P] D_{d-j}

has primitive inverse support {j, d-j}.  When d is even and j=d/2, the module
is rank one and its support is {d/2}.  Distinct unordered residue pairs have
disjoint support, so their contributions add.

The script compares this structural prediction with both exact calculations
already exposed by the Atlas: twisted-de-Rham Krylov rank and inverse-series
support.  Passing is regression evidence, not a proof or novelty result.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

import sympy as sp


x = sp.Symbol("x")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def dickson_polynomials(maximum: int, parameter: sp.Rational) -> list[sp.Expr]:
    require(maximum >= 1, "Dickson degree must be positive")
    values = [sp.Integer(2), x]
    for _degree in range(2, maximum + 1):
        values.append(sp.expand(x * values[-1] - parameter * values[-2]))
    return values


def expected_pair(degree: int, residue: int) -> set[int]:
    partner = degree - residue
    return {residue} if residue == partner else {residue, partner}


def analyse_case(
    analyse_amplitude,
    phase: sp.Expr,
    primitive: sp.Expr,
    expected_support: set[int],
    label: str,
) -> dict[str, object]:
    amplitude = sp.diff(primitive, x)
    result = analyse_amplitude(sp.sstr(phase), sp.sstr(amplitude))
    observed_support = set(result["primitive_inverse_at_infinity"]["support"])
    observed_rank = result["theorem_identity"]["twisted_amplitude_cyclic_rank"]
    require(result["theorem_identity"]["all_equal"] is True, f"identity failed: {label}")
    require(observed_support == expected_support, f"support failed: {label}: {observed_support}")
    require(observed_rank == len(expected_support), f"rank failed: {label}: {observed_rank}")
    return {
        "label": label,
        "phase": sp.sstr(phase),
        "primitive": sp.sstr(primitive),
        "expected_support": sorted(expected_support),
        "observed_support": sorted(observed_support),
        "observed_rank": observed_rank,
        "atlas_certificate_sha256": result["certificate_sha256"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--atlas-root", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--maximum-degree", type=int, default=9)
    args = parser.parse_args()

    source_root = args.atlas_root / "src"
    require(source_root.is_dir(), "Atlas src directory is missing")
    sys.path.insert(0, str(source_root))
    from amplitude_support import analyse_amplitude  # noqa: PLC0415

    require(3 <= args.maximum_degree <= 14, "maximum degree is outside the bounded battery")
    parameter_values = (
        sp.Rational(1),
        sp.Rational(2),
        sp.Rational(-1, 2),
    )
    records: list[dict[str, object]] = []
    for parameter in parameter_values:
        for degree in range(3, args.maximum_degree + 1):
            dickson = dickson_polynomials(degree, parameter)
            phase = dickson[degree]

            # Exercise both generators of every canonical pair module and a
            # deterministic nonconstant Q[P]-linear combination.
            for residue in range(1, (degree // 2) + 1):
                partner = degree - residue
                support = expected_pair(degree, residue)
                records.append(
                    analyse_case(
                        analyse_amplitude,
                        phase,
                        dickson[residue],
                        support,
                        f"a={parameter}:d={degree}:D_{residue}",
                    )
                )
                if partner != residue:
                    records.append(
                        analyse_case(
                            analyse_amplitude,
                            phase,
                            dickson[partner],
                            support,
                            f"a={parameter}:d={degree}:D_{partner}",
                        )
                    )
                    mixed = sp.expand(
                        (phase + 2) * dickson[residue]
                        + (2 * phase - 1) * dickson[partner]
                    )
                    records.append(
                        analyse_case(
                            analyse_amplitude,
                            phase,
                            mixed,
                            support,
                            f"a={parameter}:d={degree}:mixed-pair-{residue}-{partner}",
                        )
                    )

            # A sum from two distinct pair modules must have the union support.
            pair_representatives = list(range(1, (degree // 2) + 1))
            if len(pair_representatives) >= 2:
                first, second = pair_representatives[:2]
                primitive = sp.expand(
                    dickson[first] + (phase + 1) * dickson[second]
                )
                union = (
                    expected_pair(degree, first)
                    | expected_pair(degree, second)
                )
                records.append(
                    analyse_case(
                        analyse_amplitude,
                        phase,
                        primitive,
                        union,
                        f"a={parameter}:d={degree}:two-pair-union",
                    )
                )

    degenerate = dickson_polynomials(5, sp.Rational(0))
    degenerate_record = analyse_case(
        analyse_amplitude,
        degenerate[5],
        degenerate[1],
        {1},
        "a=0:d=5:excluded-power-degeneration",
    )
    require(degenerate_record["observed_rank"] == 1, (
        "a=0 control did not lose the paired channel"
    ))

    receipt: dict[str, object] = {
        "schema": "dickson-amplitude-module-falsification-v2",
        "status": "pass",
        "nonzero_parameters": [sp.sstr(value) for value in parameter_values],
        "degree_range": [3, args.maximum_degree],
        "case_count": len(records),
        "records": records,
        "excluded_a_zero_control": degenerate_record,
        "claim_boundary": {
            "established": "bounded exact agreement with Atlas Krylov and inverse-support calculations",
            "not_established": [
                "the all-degree theorem",
                "independent implementation",
                "novelty or priority",
                "external review or publication readiness",
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
