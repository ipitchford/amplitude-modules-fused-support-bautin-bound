#!/usr/bin/env python3
"""Standalone exact ODE certificates for weighted polynomial periods.

For trusted P,A in Q[x], reduce

    A, P*A, P^2*A, ...

in Q(s)[x] dx modulo (d/dx+s*P')Q(s)[x] dx.  The first exact dependence
gives a scalar differential operator for every rapid-decay period of
A(x)exp(sP(x))dx.  This implementation imports no Atlas code.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Iterable

import sympy as sp


x, s = sp.symbols("x s")
K = sp.QQ.frac_field(s)
SCHEMA = "standalone-weighted-period-order-certificate-v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_expr(value: sp.Expr) -> str:
    return sp.sstr(sp.factor(sp.cancel(value)))


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def parse_rational_polynomial(text: str, *, minimum_degree: int | None = None) -> sp.Poly:
    require(isinstance(text, str), "polynomial input must be a string")
    expression = sp.expand(sp.sympify(text, locals={"x": x}))
    require(expression.free_symbols <= {x}, "input must lie in Q[x]")
    try:
        polynomial = sp.Poly(expression, x, domain=sp.QQ)
    except (sp.PolynomialError, sp.CoercionFailed) as error:
        raise RuntimeError("input must lie in Q[x]") from error
    if minimum_degree is not None:
        require(polynomial.degree() >= minimum_degree, (
            f"polynomial degree must be at least {minimum_degree}"
        ))
    return polynomial


def reduce_by_parts_with_witness(
    polynomial: sp.Poly,
    phase: sp.Poly,
    *,
    track_witness: bool = True,
) -> tuple[sp.Poly, sp.Poly]:
    """Reduce exactly and retain a total-derivative witness.

    If P'=p*x^(d-1)+L, the quotient relation is

        x^(k+d-1) = -k*x^(k-1)/(s*p) - x^k*L/p.

    Each replacement lowers degree, so the algorithm terminates with the
    unique representative R of degree below d-1.  It also returns C with

        polynomial = R + C' + s*P'*C.
    """

    phase_k = sp.Poly(phase.as_expr(), x, domain=K)
    derivative = phase_k.diff()
    top_degree = phase.degree() - 1
    top_coefficient = derivative.LC()
    lower = derivative - sp.Poly(
        top_coefficient * x**top_degree,
        x,
        domain=K,
    )
    remainder = sp.Poly(polynomial.as_expr(), x, domain=K)
    witness = sp.Poly(0, x, domain=K)

    while not remainder.is_zero and remainder.degree() >= top_degree:
        degree = remainder.degree()
        coefficient = remainder.LC()
        shift = degree - top_degree
        remainder -= sp.Poly(coefficient * x**degree, x, domain=K)
        if track_witness:
            witness += sp.Poly(
                coefficient * x**shift / (s * top_coefficient),
                x,
                domain=K,
            )
        if shift:
            remainder += sp.Poly(
                -coefficient * shift * x ** (shift - 1) / (s * top_coefficient),
                x,
                domain=K,
            )
        remainder += sp.Poly(
            -coefficient * x**shift * lower.as_expr() / top_coefficient,
            x,
            domain=K,
        )
    if track_witness:
        reconstructed = sp.Poly(
            remainder.as_expr()
            + sp.diff(witness.as_expr(), x)
            + s * derivative.as_expr() * witness.as_expr(),
            x,
            domain=K,
        )
        require(
            reconstructed == sp.Poly(polynomial.as_expr(), x, domain=K),
            "reduction witness failed exact reconstruction",
        )
    return remainder, witness


def reduce_by_parts(polynomial: sp.Poly, phase: sp.Poly) -> sp.Poly:
    """Return the unique reduced representative and discard its witness."""

    remainder, _witness = reduce_by_parts_with_witness(
        polynomial,
        phase,
        track_witness=False,
    )
    return remainder


def coordinate_vector(polynomial: sp.Poly, phase: sp.Poly) -> sp.Matrix:
    ambient_rank = phase.degree() - 1
    reduced = reduce_by_parts(polynomial, phase)
    return sp.Matrix([
        sp.cancel(reduced.nth(power))
        for power in range(ambient_rank)
    ])


def weighted_krylov_matrix(phase: sp.Poly, amplitude: sp.Poly) -> sp.Matrix:
    """Return [A],...,[P^(d-1)A], including at least one dependence."""

    ambient_rank = phase.degree() - 1
    phase_k = sp.Poly(phase.as_expr(), x, domain=K)
    iterate = sp.Poly(amplitude.as_expr(), x, domain=K)
    columns: list[sp.Matrix] = []
    for _ in range(ambient_rank + 1):
        columns.append(coordinate_vector(iterate, phase))
        iterate *= phase_k
    return sp.Matrix.hstack(*columns)


def first_relation(matrix: sp.Matrix) -> tuple[int, list[sp.Expr]]:
    """Return the first dependent index and coefficients ending in one."""

    for width in range(1, matrix.cols + 1):
        prefix = matrix[:, :width]
        if prefix.rank() == width:
            continue
        order = width - 1
        nullspace = prefix.nullspace()
        require(len(nullspace) == 1, "first dependence is not one-dimensional")
        relation = nullspace[0]
        require(relation[-1] != 0, "first dependence lost its final column")
        normalized = [
            sp.cancel(value / relation[-1])
            for value in relation
        ]
        residual = prefix * sp.Matrix(normalized)
        require(
            all(sp.cancel(value) == 0 for value in residual),
            "first dependence has a nonzero residual",
        )
        return order, normalized
    raise RuntimeError("Krylov matrix did not contain a dependence")


def polynomial_denominator_lcm(expressions: Iterable[sp.Expr]) -> sp.Poly:
    common = sp.Poly(1, s, domain=sp.QQ)
    for expression in expressions:
        _numerator, denominator = sp.fraction(sp.cancel(expression))
        common = sp.lcm(common, sp.Poly(denominator, s, domain=sp.QQ))
    return common


def primitive_integer_coefficients(expressions: list[sp.Expr]) -> list[sp.Expr]:
    """Clear denominators, polynomial gcd, integer content, and sign."""

    denominator = polynomial_denominator_lcm(expressions)
    polynomials = [
        sp.Poly(
            sp.cancel(denominator.as_expr() * expression),
            s,
            domain=sp.QQ,
        )
        for expression in expressions
    ]
    nonzero = [polynomial for polynomial in polynomials if not polynomial.is_zero]
    require(nonzero, "zero differential operator")

    common_factor = nonzero[0]
    for polynomial in nonzero[1:]:
        common_factor = sp.gcd(common_factor, polynomial)
    divided = [
        sp.Poly(
            sp.cancel(polynomial.as_expr() / common_factor.as_expr()),
            s,
            domain=sp.QQ,
        )
        for polynomial in polynomials
    ]

    scalar_denominator = 1
    for polynomial in divided:
        for coefficient in polynomial.all_coeffs():
            scalar_denominator = sp.ilcm(
                scalar_denominator,
                int(sp.Rational(coefficient).q),
            )
    integer_expressions = [
        sp.expand(scalar_denominator * polynomial.as_expr())
        for polynomial in divided
    ]
    content = 0
    for expression in integer_expressions:
        for coefficient in sp.Poly(expression, s, domain=sp.ZZ).all_coeffs():
            content = math.gcd(content, abs(int(coefficient)))
    require(content >= 1, "failed to determine integer content")
    primitive = [sp.expand(expression / content) for expression in integer_expressions]
    if sp.Poly(primitive[-1], s, domain=sp.ZZ).LC() < 0:
        primitive = [-expression for expression in primitive]
    return primitive


def matrix_sha256(matrix: sp.Matrix) -> str:
    return canonical_hash([canonical_expr(value) for value in matrix])


def certificate_for(phase_text: str, amplitude_text: str) -> dict[str, object]:
    phase = parse_rational_polynomial(phase_text, minimum_degree=2)
    amplitude = parse_rational_polynomial(amplitude_text)
    matrix = weighted_krylov_matrix(phase, amplitude)
    order, rational_relation = first_relation(matrix)

    if order == 0:
        require(
            all(sp.cancel(value) == 0 for value in matrix[:, 0]),
            "rank-zero seed column is nonzero",
        )
        coefficients = [sp.Integer(1)]
        pivot_rows: list[int] = []
    else:
        coefficients = primitive_integer_coefficients(rational_relation)
        basis = matrix[:, :order]
        pivot_rows = list(basis.T.rref()[1])
        require(len(pivot_rows) == order, "failed to select independence minor")
        minor = basis.extract(pivot_rows, range(order)).det()
        require(minor != 0, "independence minor vanished")

    residual = sp.zeros(matrix.rows, 1)
    for derivative_order, coefficient in enumerate(coefficients):
        residual += matrix[:, derivative_order] * coefficient
    require(
        all(sp.cancel(value) == 0 for value in residual),
        "primitive operator has a nonzero exact residual",
    )

    phase_k = sp.Poly(phase.as_expr(), x, domain=K)
    iterate = sp.Poly(amplitude.as_expr(), x, domain=K)
    operator_integrand = sp.Poly(0, x, domain=K)
    for coefficient in coefficients:
        operator_integrand += sp.Poly(
            coefficient * iterate.as_expr(),
            x,
            domain=K,
        )
        iterate *= phase_k
    integrand_remainder, telescoping_witness = reduce_by_parts_with_witness(
        operator_integrand,
        phase,
    )
    require(integrand_remainder.is_zero, "operator integrand is not twisted exact")
    witness_text = canonical_expr(telescoping_witness.as_expr())

    coefficient_strings = [canonical_expr(value) for value in coefficients]
    result: dict[str, object] = {
        "schema": SCHEMA,
        "status": "pass",
        "input": {"phase": phase_text, "amplitude": amplitude_text},
        "input_sha256": canonical_hash({
            "phase": phase_text,
            "amplitude": amplitude_text,
        }),
        "phase_degree": phase.degree(),
        "ambient_twisted_rank": phase.degree() - 1,
        "operator": {
            "order": order,
            "independent_variable": "s",
            "derivation_symbol": "D_s",
            "coefficient_order": "low_derivative_to_high_derivative",
            "coefficients": coefficient_strings,
            "equation": (
                "I(s) = 0"
                if order == 0
                else "sum_j coefficients[j] * I^(j)(s) = 0"
            ),
            "pivot_rows_zero_based": pivot_rows,
            "exact_krylov_residual_zero": True,
            "weighted_krylov_matrix_sha256": matrix_sha256(matrix),
            "telescoping_witness_C": witness_text,
            "telescoping_witness_sha256": canonical_hash(witness_text),
            "telescoping_identity": "sum_j c_j*P^j*A = dC/dx + s*P'(x)*C",
            "exact_telescoping_identity_verified": True,
        },
        "claim_boundary": {
            "established": (
                "exact twisted-quotient order, primitive Z[s] operator, "
                "zero residual, and an exact total-derivative witness for "
                "the supplied trusted Q[x] inputs"
            ),
            "requires_theorem": (
                "identification of this order with inverse support and "
                "minimality for the complete rapid-decay period system"
            ),
            "not_established": [
                "rapid decay of an arbitrary contour",
                "minimality for every individual cycle",
                "novelty, independent review, or publication readiness",
            ],
        },
    }
    result["certificate_sha256"] = canonical_hash(result)
    return result


def verify_certificate(certificate: dict[str, object]) -> dict[str, object]:
    require(isinstance(certificate, dict), "certificate must be a JSON object")
    require(certificate.get("schema") == SCHEMA, "unknown certificate schema")
    supplied_digest = certificate.get("certificate_sha256")
    require(isinstance(supplied_digest, str), "certificate digest is missing")
    unhashed = dict(certificate)
    unhashed.pop("certificate_sha256", None)
    require(canonical_hash(unhashed) == supplied_digest, "certificate digest mismatch")
    inputs = certificate.get("input")
    require(isinstance(inputs, dict), "certificate inputs are missing")
    phase = inputs.get("phase")
    amplitude = inputs.get("amplitude")
    require(
        isinstance(phase, str) and isinstance(amplitude, str),
        "certificate inputs are invalid",
    )
    require(
        certificate_for(phase, amplitude) == certificate,
        "certificate differs from exact recomputation",
    )
    return {
        "schema": "standalone-weighted-period-order-verification-v1",
        "status": "pass",
        "certificate_sha256": supplied_digest,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--phase")
    action.add_argument("--verify-certificate", type=Path)
    parser.add_argument("--amplitude")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.verify_certificate:
        supplied = json.loads(args.verify_certificate.read_text(encoding="utf-8"))
        result = verify_certificate(supplied)
    else:
        require(isinstance(args.amplitude, str), "--amplitude is required with --phase")
        result = certificate_for(args.phase, args.amplitude)
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
    else:
        print(encoded, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
