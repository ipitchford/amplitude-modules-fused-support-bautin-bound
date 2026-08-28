#!/usr/bin/env python3
"""Independent-of-Atlas falsification checks for the support/rank theorem.

The rank side uses the local standalone twisted-quotient reducer.  The
support side constructs the normalized inverse at infinity from its defining
coefficient recursion and inspects exact nonzero Laurent coefficients.  No
Atlas source is imported.

Seeing as many distinct residue channels as the exact Krylov rank is strong
falsification evidence, but a finite inverse-series window does not certify
that every unobserved channel vanishes forever.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

from standalone_weighted_order_oracle import (
    parse_rational_polynomial,
    weighted_krylov_matrix,
    x,
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_hash(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def multiply_truncated(
    left: list[sp.Rational],
    right: list[sp.Rational],
    degree: int,
) -> list[sp.Rational]:
    result = [sp.Rational(0) for _ in range(degree + 1)]
    for left_index, left_value in enumerate(left[: degree + 1]):
        if left_value == 0:
            continue
        maximum_right = degree - left_index
        for right_index, right_value in enumerate(right[: maximum_right + 1]):
            if right_value != 0:
                result[left_index + right_index] += left_value * right_value
    return result


def power_truncated(
    coefficients: list[sp.Rational],
    power: int,
    degree: int,
) -> list[sp.Rational]:
    result = [sp.Rational(1)] + [sp.Rational(0) for _ in range(degree)]
    for _ in range(power):
        result = multiply_truncated(result, coefficients, degree)
    return result


def normalized_inverse_factor(phase: sp.Poly, depth: int) -> list[sp.Rational]:
    """Return F(y) through y^depth where xi(t)=t*F(t^-1)."""

    degree = phase.degree()
    require(phase.LC() == 1, "phase must be monic")
    require(phase.nth(degree - 1) == 0, "phase must be centred")
    coefficients = [sp.Rational(1)] + [sp.Rational(0) for _ in range(depth)]
    for index in range(1, depth + 1):
        # With the new coefficient temporarily zero, the coefficient of y^index
        # in F^d is the known remainder; the omitted contribution is d*a_index.
        remainder = power_truncated(coefficients, degree, index)[index]
        for source_power in range(degree):
            phase_coefficient = phase.nth(source_power)
            shift = degree - source_power
            if phase_coefficient == 0 or shift > index:
                continue
            remainder += phase_coefficient * power_truncated(
                coefficients,
                source_power,
                index - shift,
            )[index - shift]
        coefficients[index] = sp.Rational(-remainder, degree)

    # Fail closed on the defining equation through the requested depth.
    residual = power_truncated(coefficients, degree, depth)
    residual[0] -= 1
    for source_power in range(degree):
        phase_coefficient = phase.nth(source_power)
        shift = degree - source_power
        if phase_coefficient == 0 or shift > depth:
            continue
        contribution = power_truncated(
            coefficients,
            source_power,
            depth - shift,
        )
        for index, value in enumerate(contribution):
            residual[index + shift] += phase_coefficient * value
    require(all(value == 0 for value in residual), "inverse recursion residual is nonzero")
    return coefficients


def observed_primitive_support(
    phase: sp.Poly,
    primitive: sp.Poly,
    depth: int,
) -> tuple[list[int], dict[int, tuple[int, str]]]:
    degree = phase.degree()
    inverse_factor = normalized_inverse_factor(phase, depth)
    minimum_complete_exponent = primitive.degree() - depth
    laurent_coefficients: dict[int, sp.Rational] = {}
    for source_power in range(primitive.degree() + 1):
        primitive_coefficient = primitive.nth(source_power)
        if primitive_coefficient == 0:
            continue
        expansion = power_truncated(inverse_factor, source_power, depth)
        for inverse_index, inverse_coefficient in enumerate(expansion):
            coefficient = primitive_coefficient * inverse_coefficient
            if coefficient == 0:
                continue
            exponent = source_power - inverse_index
            if exponent < minimum_complete_exponent:
                continue
            laurent_coefficients[exponent] = (
                laurent_coefficients.get(exponent, sp.Rational(0)) + coefficient
            )
    channel_witnesses: dict[int, tuple[int, str]] = {}
    for exponent, coefficient in sorted(laurent_coefficients.items(), reverse=True):
        if coefficient == 0:
            continue
        residue = exponent % degree
        if residue != 0 and residue not in channel_witnesses:
            channel_witnesses[residue] = (exponent, sp.sstr(coefficient))
    return sorted(channel_witnesses), channel_witnesses


def dickson_polynomial(degree: int) -> sp.Expr:
    values = [sp.Integer(2), x]
    for _ in range(2, degree + 1):
        values.append(sp.expand(x * values[-1] - values[-2]))
    return values[degree]


def cases() -> list[tuple[str, str, str]]:
    values: list[tuple[str, str, str]] = [
        ("generic-cubic", "x**3+x+1", "x"),
        ("generic-quartic", "x**4+x**2+x+1", "x"),
        ("generic-quintic", "x**5+2*x**3-x+1", "x"),
        ("generic-sextic", "x**6+x**4+x+1", "x"),
        ("generic-septic", "x**7+x**5+2*x**2+1", "x"),
        ("composition-one", "(x**2-1/4)**3", "x**2-1/4"),
        ("composition-two", "(x**2-1/4)**3", "(x**2-1/4)**2"),
        (
            "composition-mixed",
            "(x**2-1/4)**3",
            "(x**2-1/4)+(x**2-1/4)**2",
        ),
    ]
    for degree in range(3, 8):
        values.extend([
            (f"power-{degree}-single", f"x**{degree}", "x"),
            (f"power-{degree}-mixed", f"x**{degree}", "x+x**2"),
            (f"power-{degree}-trace", f"x**{degree}", f"x**{degree}"),
            (
                f"dickson-{degree}",
                sp.sstr(dickson_polynomial(degree)),
                sp.sstr(dickson_polynomial(1) + dickson_polynomial(degree - 1)),
            ),
        ])
    return values


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--depth", type=int, default=48)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    require(16 <= args.depth <= 96, "depth is outside the bounded control range")

    records: list[dict[str, object]] = []
    for label, phase_text, primitive_text in cases():
        phase = parse_rational_polynomial(phase_text, minimum_degree=2)
        require(phase.LC() != 0, f"zero leading coefficient: {label}")
        phase = sp.Poly(phase.monic().as_expr(), x, domain=sp.QQ)
        require(phase.nth(phase.degree() - 1) == 0, f"phase is not centred: {label}")
        primitive = parse_rational_polynomial(primitive_text)
        amplitude = primitive.diff()
        matrix = weighted_krylov_matrix(phase, amplitude)
        rank = int(sp.polys.matrices.DomainMatrix.from_Matrix(matrix).rank())
        support, witnesses = observed_primitive_support(phase, primitive, args.depth)
        require(len(support) == rank, (
            f"support/rank disagreement through depth {args.depth}: {label}: "
            f"support={support}, rank={rank}"
        ))
        records.append({
            "label": label,
            "phase": sp.sstr(phase.as_expr()),
            "primitive": sp.sstr(primitive.as_expr()),
            "twisted_krylov_rank": rank,
            "observed_support": support,
            "channel_witnesses": {
                str(residue): {
                    "highest_observed_t_exponent": exponent,
                    "coefficient": coefficient,
                }
                for residue, (exponent, coefficient) in sorted(witnesses.items())
            },
        })

    receipt: dict[str, object] = {
        "schema": "support-rank-reconstruction-falsification-v1",
        "status": "pass",
        "atlas_source_imported": False,
        "inverse_series_depth": args.depth,
        "case_count": len(records),
        "records": records,
        "claim_boundary": {
            "established": (
                "exact twisted-Krylov ranks and exact nonzero inverse-series "
                "coefficients witnessing the same number of channels in every case"
            ),
            "not_established": [
                "vanishing of every unobserved channel beyond the finite series window",
                "the all-degree support theorem",
                "independent human or institutional reproduction",
                "novelty, peer review, or publication readiness",
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
