#!/usr/bin/env python3
"""Exact cross-interface checks for the coefficient-Bautin proof.

The case is deliberately outside the power-phase and square degree regimes:

    f=x^2+x,  C=x_1-x_2,  x_2=-1-x_1,
    g=a_0+...+a_4 x^4.

Thus deg(g)>deg(f).  The checker compares:

1. direct implicit-root displacement coefficients with the all-order
   Lagrange--Bürmann formula;
2. parameter-content ideals before and after the order-dependent
   t-derivative; and
3. basis-coordinate content with finite local Taylor jets at t=f(1).

It is an exact finite falsifier.  It does not prove the universal theorem,
historical novelty, or independent validation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
from pathlib import Path

import sympy as sp


x = sp.Symbol("x")
epsilon = sp.Symbol("epsilon")
parameters = sp.symbols("a0:5")
phase = x**2 + x
other_root = -1 - x
perturbation = sum(parameter * x**degree for degree, parameter in enumerate(parameters))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def d_t(expression: sp.Expr) -> sp.Expr:
    """Differentiate a branch expression with respect to t=f(x)."""

    return sp.cancel(sp.diff(expression, x) / sp.diff(phase, x))


def iterate_d_t(expression: sp.Expr, count: int) -> sp.Expr:
    for _ in range(count):
        expression = d_t(expression)
    return sp.cancel(expression)


def implicit_root_shift(order: int) -> sp.Expr:
    """Return z(epsilon)-x for f(z)+epsilon*g(z)=f(x)."""

    shift = sp.Integer(0)
    phase_derivative = sp.diff(phase, x)
    for degree in range(1, order + 1):
        unknown = sp.Symbol(f"root_coefficient_{degree}")
        trial = shift + unknown * epsilon**degree
        equation = sp.series(
            phase.subs(x, x + trial)
            - phase
            + epsilon * perturbation.subs(x, x + trial),
            epsilon,
            0,
            degree + 1,
        ).removeO()
        coefficient = sp.expand(equation).coeff(epsilon, degree)
        solved = sp.cancel(-coefficient.subs(unknown, 0) / phase_derivative)
        shift += solved * epsilon**degree
    return shift


def normalized_groebner(generators: list[sp.Expr]) -> sp.GroebnerBasis:
    nonzero = [sp.expand(generator) for generator in generators if generator != 0]
    require(nonzero, "content ideal unexpectedly has no generators")
    return sp.groebner(nonzero, *parameters, order="grevlex", domain=sp.QQ)


def ideals_equal(left: list[sp.Expr], right: list[sp.Expr]) -> bool:
    left_basis = normalized_groebner(left)
    right_basis = normalized_groebner(right)
    left_contains_right = all(
        sp.expand(left_basis.reduce(generator)[1]) == 0 for generator in right
    )
    right_contains_left = all(
        sp.expand(right_basis.reduce(generator)[1]) == 0 for generator in left
    )
    return left_contains_right and right_contains_left


def content_generators(expression: sp.Expr) -> list[sp.Expr]:
    """Return parameter content using the independent basis x^k/denominator."""

    numerator, denominator = sp.fraction(sp.together(expression))
    require(not any(denominator.has(parameter) for parameter in parameters), (
        "a denominator depends on a perturbation parameter"
    ))
    polynomial = sp.Poly(sp.expand(numerator), x, domain=sp.EX)
    return [
        sp.expand(coefficient)
        for coefficient in polynomial.all_coeffs()
        if coefficient != 0
    ]


def finite_jet_generators(expression: sp.Expr, jet_count: int) -> list[sp.Expr]:
    """Return Taylor coefficients at the regular point x=1, t=2."""

    current = expression
    jets: list[sp.Expr] = []
    for order in range(jet_count):
        value = sp.cancel(current.subs(x, 1) / sp.factorial(order))
        require(not any(sp.denom(value).has(parameter) for parameter in parameters), (
            "a Taylor coefficient has a parameter-dependent denominator"
        ))
        jets.append(sp.expand(value))
        current = d_t(current)
    return jets


def coefficient_span_record(expression: sp.Expr) -> dict[str, int | bool]:
    """Measure dependence among parameter-monomial coefficient functions."""

    polynomial = sp.Poly(sp.expand(expression), *parameters, domain=sp.EX)
    function_coefficients = [sp.cancel(coefficient) for _, coefficient in polynomial.terms()]
    common_denominator = sp.Integer(1)
    for coefficient in function_coefficients:
        common_denominator = sp.lcm(
            common_denominator,
            sp.denom(coefficient),
        )
    numerators = [
        sp.Poly(
            sp.cancel(coefficient * common_denominator),
            x,
            domain=sp.QQ,
        )
        for coefficient in function_coefficients
    ]
    maximum_degree = max(int(numerator.degree()) for numerator in numerators)
    columns = [
        [
            numerator.nth(degree)
            for degree in range(maximum_degree + 1)
        ]
        for numerator in numerators
    ]
    rank = int(sp.Matrix(columns).T.rank())
    raw_count = len(function_coefficients)
    return {
        "parameter_monomial_count": raw_count,
        "coefficient_function_span_dimension": rank,
        "has_dependent_coefficient_functions": rank < raw_count,
    }


def verify_order(
    order: int,
    direct_displacement: sp.Expr,
    maximum_jets: int,
) -> dict[str, object]:
    power_moment = sp.expand(
        perturbation**order
        - perturbation.subs(x, other_root)**order
    )
    predicted = sp.cancel(
        sp.Rational((-1) ** order, sp.factorial(order))
        * iterate_d_t(power_moment, order - 1)
    )
    direct = sp.cancel(
        sp.expand(direct_displacement).coeff(epsilon, order)
    )
    require(sp.cancel(direct - predicted) == 0, (
        f"direct/Lagrange--Bürmann mismatch at order {order}"
    ))

    moment_content = content_generators(power_moment)
    melnikov_content = content_generators(predicted)
    require(ideals_equal(moment_content, melnikov_content), (
        f"content changed under differentiation at order {order}"
    ))

    first_sufficient_jet_count: int | None = None
    for jet_count in range(1, maximum_jets + 1):
        if ideals_equal(
            melnikov_content,
            finite_jet_generators(predicted, jet_count),
        ):
            first_sufficient_jet_count = jet_count
            break
    require(first_sufficient_jet_count is not None, (
        f"Taylor jets did not recover content at order {order}"
    ))

    return {
        "order": order,
        "direct_identity_residual_is_zero": True,
        "moment_content_equals_melnikov_content": True,
        "local_taylor_ideal_equals_content": True,
        "first_sufficient_jet_count": first_sufficient_jet_count,
        "content_groebner_basis": [
            sp.sstr(polynomial.as_expr())
            for polynomial in normalized_groebner(melnikov_content).polys
        ],
        "coefficient_span": coefficient_span_record(predicted),
    }


def write_receipt(path: Path, encoded: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="wb",
        dir=path.parent,
        prefix=f".{path.name}.",
        delete=False,
    ) as handle:
        handle.write(encoded)
        temporary = Path(handle.name)
    os.replace(temporary, path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--maximum-order", type=int, default=3)
    parser.add_argument("--maximum-jets", type=int, default=12)
    args = parser.parse_args()
    require(2 <= args.maximum_order <= 4, "maximum order must lie from two to four")
    require(args.maximum_jets >= 4, "maximum jets must be at least four")

    shift = implicit_root_shift(args.maximum_order - 1)
    first_root = x + shift
    second_root = other_root + shift.subs(x, other_root)
    direct_displacement = sp.series(
        -epsilon
        * (
            perturbation.subs(x, first_root)
            - perturbation.subs(x, second_root)
        ),
        epsilon,
        0,
        args.maximum_order + 1,
    ).removeO()

    order_checks = [
        verify_order(order, direct_displacement, args.maximum_jets)
        for order in range(1, args.maximum_order + 1)
    ]
    require(any(
        check["coefficient_span"]["has_dependent_coefficient_functions"]
        for check in order_checks
    ), "the battery did not exercise a dependent coefficient span")

    cumulative_first = content_generators(
        perturbation - perturbation.subs(x, other_root)
    )
    for order in range(2, args.maximum_order + 1):
        moment = sp.expand(
            perturbation**order
            - perturbation.subs(x, other_root)**order
        )
        melnikov = sp.cancel(
            sp.Rational((-1) ** order, sp.factorial(order))
            * iterate_d_t(moment, order - 1)
        )
        require(ideals_equal(
            cumulative_first,
            cumulative_first + content_generators(melnikov),
        ), f"quadratic cutoff ideal grew at order {order}")

    receipt: dict[str, object] = {
        "schema": "bautin-content-bridge-falsification-v1",
        "status": "pass",
        "case": {
            "phase": "x^2+x",
            "phase_degree": 2,
            "cycle": "x_1-x_2 with x_2=-1-x_1",
            "perturbation": "a0+a1*x+a2*x^2+a3*x^3+a4*x^4",
            "perturbation_degree": 4,
            "regular_jet_base_point": "x=1, t=2",
        },
        "order_checks": order_checks,
        "quadratic_cutoff_content_stable_through_order": args.maximum_order,
        "claim_boundary": {
            "established_by_this_check": [
                "direct implicit-root and Lagrange--Bürmann coefficients agree",
                "parameter content survives the required derivatives",
                "finite local Taylor jets recover parameter content",
                "the d-1 cutoff survives in one non-power case with deg(g)>deg(f)",
                "at least one dependent coefficient-function span is exercised",
            ],
            "not_established": [
                "the all-degree theorem",
                "historical novelty",
                "independent review or publication readiness",
            ],
        },
    }
    receipt["receipt_sha256"] = canonical_hash(receipt)
    encoded = (json.dumps(receipt, indent=2, sort_keys=True) + "\n").encode("utf-8")
    if args.output:
        write_receipt(args.output.resolve(), encoded)
    else:
        print(encoded.decode("utf-8"), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
