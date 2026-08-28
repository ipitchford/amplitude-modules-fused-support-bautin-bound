#!/usr/bin/env python3
"""Target hidden channel cancellations for P=(x^4+x)^3.

This is a standalone exact calculation: it does not import Atlas code.  It
first verifies the Newton-trace filter that proves the forbidden quartic
trace channel is absent at every C[P]-coefficient degree.  For
the inverse branch x=t*phi(t^-3) of x^4+x=t^4, Lagrange inversion gives

    [z^n] phi(z)^j = -j/(4n) * binomial((3n-j)/4-1, n-1),  n >= 1.

The script uses that formula to search for a C[P]-linear combination of the
three generators of any proposed fused module whose entire residue channel
vanishes.  Full column rank proves absence of such a relation up to the
declared coefficient-degree bound; it is falsification evidence, not the
unbounded theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


x = sp.Symbol("x")
y = sp.Symbol("y")

MODULES = (
    (x, x**7 + sp.Rational(7, 4) * x**4, x**10 - sp.Rational(5, 2) * x**4),
    (x**2, x**5, x**11 + sp.Rational(11, 4) * x**8),
    (x**3, x**6, x**9),
)
CHANNELS = (
    (1, 7, 10),
    (2, 5, 11),
    (3, 6, 9),
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def inverse_power_coefficient(power: int, index: int) -> sp.Rational:
    """Return [z^index] phi(z)^power for phi^4+z*phi=1."""

    require(power >= 0 and index >= 0, "power and index must be nonnegative")
    if index == 0:
        return sp.Rational(1)
    if power == 0:
        return sp.Rational(0)
    value = -sp.Rational(power, 4 * index) * sp.binomial(
        sp.Rational(3 * index - power, 4) - 1,
        index - 1,
    )
    return sp.Rational(sp.factor(value))


def quartic_power_sums(maximum_power: int) -> list[sp.Expr]:
    """Return p_j=sum_{u^4+u=y}u^j from Newton's recurrence."""

    require(maximum_power >= 3, "maximum power must be at least three")
    sums: list[sp.Expr] = [sp.Integer(4), sp.Integer(0), sp.Integer(0), -sp.Integer(3)]
    for power in range(4, maximum_power + 1):
        sums.append(sp.expand(y * sums[power - 4] - sums[power - 3]))
    return sums


def quartic_trace(poly: sp.Expr, power_sums: list[sp.Expr]) -> sp.Expr:
    """Return the fibre trace for Q=x^4+x by linearity in monomials."""

    total = sp.Integer(0)
    for (power,), coefficient in sp.Poly(poly, x, domain=sp.QQ).terms():
        require(power < len(power_sums), "power-sum table is too short")
        total += coefficient * power_sums[power]
    return sp.expand(total)


def inverse_coefficient(poly: sp.Expr, exponent: int) -> sp.Rational:
    """Return [t^exponent] poly(xi(t)) exactly."""

    total = sp.Rational(0)
    for (power,), coefficient in sp.Poly(poly, x, domain=sp.QQ).terms():
        difference = power - exponent
        if difference < 0 or difference % 3:
            continue
        total += coefficient * inverse_power_coefficient(power, difference // 3)
    return sp.Rational(sp.factor(total))


def channel_top_exponent(poly: sp.Expr, residue: int) -> int:
    degree = int(sp.degree(poly, x))
    exponent = degree - ((degree - residue) % 12)
    for _ in range(100):
        if inverse_coefficient(poly, exponent) != 0:
            return exponent
        exponent -= 12
    raise RuntimeError("failed to locate a channel-leading coefficient")


def relation_matrix(
    module: tuple[sp.Expr, sp.Expr, sp.Expr],
    residue: int,
    coefficient_degree: int,
) -> tuple[sp.Matrix, list[tuple[int, int]], list[int]]:
    """Build coefficient equations for sum H_g(t^12) g(xi(t))=0."""

    columns = [
        (generator_index, power)
        for generator_index in range(3)
        for power in range(coefficient_degree + 1)
    ]
    tops = [channel_top_exponent(generator, residue) for generator in module]
    global_top = max(top + 12 * coefficient_degree for top in tops)
    rows: list[list[sp.Rational]] = []
    exponents: list[int] = []
    max_rows = 8 * len(columns) + 24
    for level in range(max_rows):
        exponent = global_top - 12 * level
        row = [
            inverse_coefficient(module[generator_index], exponent - 12 * power)
            for generator_index, power in columns
        ]
        rows.append(row)
        exponents.append(exponent)
        matrix = sp.Matrix(rows)
        if matrix.rank() == len(columns):
            return matrix, columns, exponents
    return sp.Matrix(rows), columns, exponents


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-coefficient-degree", type=int, default=6)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    require(args.max_coefficient_degree >= 0, "degree bound must be nonnegative")

    power_sums = quartic_power_sums(11)
    expected_power_sums = {
        1: 0,
        2: 0,
        3: -3,
        4: 4 * y,
        5: 0,
        6: 3,
        7: -7 * y,
        8: 4 * y**2,
        9: -3,
        10: 10 * y,
        11: -11 * y**2,
    }
    for power, expected in expected_power_sums.items():
        require(sp.expand(power_sums[power] - expected) == 0, (
            f"unexpected quartic power sum p_{power}: {power_sums[power]}"
        ))

    generator_traces = [
        [quartic_trace(generator, power_sums) for generator in module]
        for module in MODULES
    ]
    require(generator_traces[0] == [0, 0, 0], "M0 is not trace-free")
    require(generator_traces[1] == [0, 0, 0], "M1 is not trace-free")
    require(generator_traces[2] == [-3, 3, -3], "unexpected M2 traces")

    records: list[dict[str, object]] = []
    for module_index, (module, residues) in enumerate(
        zip(MODULES, CHANNELS, strict=True)
    ):
        for residue in residues:
            generator_tops = [
                channel_top_exponent(generator, residue) for generator in module
            ]
            degree_records: list[dict[str, object]] = []
            for degree in range(args.max_coefficient_degree + 1):
                matrix, columns, exponents = relation_matrix(module, residue, degree)
                rank = matrix.rank()
                require(rank == len(columns), (
                    f"candidate cancellation found in M{module_index}, "
                    f"channel {residue}, degree {degree}"
                ))
                pivot_rows = list(matrix.T.rref()[1])
                require(len(pivot_rows) == len(columns), "failed to select full minor")
                minor = matrix.extract(pivot_rows, range(len(columns))).det()
                require(minor != 0, "selected channel-independence minor vanished")
                matrix_payload = [sp.sstr(value) for value in matrix]
                degree_records.append({
                    "coefficient_degree_bound": degree,
                    "unknown_count": len(columns),
                    "equation_count": matrix.rows,
                    "rank": rank,
                    "highest_t_exponent": int(exponents[0]),
                    "lowest_t_exponent": int(exponents[-1]),
                    "minor_is_nonzero": True,
                    "minor_sha256": canonical_hash(sp.sstr(sp.factor(minor))),
                    "matrix_sha256": canonical_hash(matrix_payload),
                })
            records.append({
                "module": f"M{module_index}",
                "channel": residue,
                "generator_top_exponents": generator_tops,
                "degree_checks": degree_records,
            })

    receipt: dict[str, object] = {
        "schema": "exceptional-channel-independence-falsification-v2",
        "status": "pass",
        "phase": "(x**4 + x)**3",
        "coefficient_field": "Q",
        "maximum_C_P_coefficient_degree": args.max_coefficient_degree,
        "lagrange_formula": (
            "[z^n]phi(z)^j=-j/(4*n)*binomial((3*n-j)/4-1,n-1)"
        ),
        "quartic_trace_filter": {
            "power_sum_recurrence": "p_j=y*p_(j-4)-p_(j-3)",
            "power_sums": {
                str(power): sp.sstr(value)
                for power, value in expected_power_sums.items()
            },
            "generator_traces": [
                [sp.sstr(value) for value in traces]
                for traces in generator_traces
            ],
            "C_P_stability": "tr_Q(F(P)R)=F(y**3)*tr_Q(R)",
            "status": "pass",
        },
        "records": records,
        "claim_boundary": {
            "established": (
                "exact Newton-trace identities underlying the all-degree forbidden-"
                "channel filter, plus absence of a remaining-channel cancellation "
                "through the declared C[P]-coefficient degree bound"
            ),
            "not_established": [
                "the exceptional all-amplitude rank formula by computation alone",
                "novelty, independent review, or publication readiness",
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
