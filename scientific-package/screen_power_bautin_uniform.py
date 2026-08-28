#!/usr/bin/env python3
"""Exact falsification screens for the power-phase Bautin theorem.

For f=x^d, write a perturbation g=sum_{j=0}^{n} a_j x^j, with no
restriction n<=d, and reduce powers of g in

    R[u,x]/(x^d-u),  R=Q[a_0,...,a_{d-1}].

The accompanying theorem uses Cayley--Hamilton to show that every active
Fourier coordinate of g^mu for mu >= d is generated, coefficientwise over R,
by the coordinates at orders 1,...,d-1.  This script checks the matrix
identity in small symbolic degrees, checks representative coefficient ideals
past the proposed cutoff, and audits the distinction between integer and
complex cycle sharpness witnesses.

The run is exact but finite.  It is a falsifier and replay artifact, not a
replacement for the general proof.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import tempfile
from dataclasses import dataclass
from pathlib import Path

import sympy as sp


x = sp.Symbol("x")
u = sp.Symbol("u")
z = sp.Symbol("z")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def least_prime_divisor(value: int) -> int:
    require(value >= 2, "degree must be at least two")
    for candidate in range(2, math.isqrt(value) + 1):
        if value % candidate == 0:
            return candidate
    return value


def multiplication_matrix(
    degree: int,
    perturbation_degree: int,
) -> tuple[sp.Matrix, tuple[sp.Symbol, ...]]:
    """Return multiplication by generic g in the basis 1,x,...,x^(d-1)."""

    require(degree >= 2, "degree must be at least two")
    require(perturbation_degree >= 0, "perturbation degree must be nonnegative")
    parameters = sp.symbols(f"a0:{perturbation_degree + 1}")
    matrix = sp.zeros(degree)
    for column in range(degree):
        for exponent, parameter in enumerate(parameters):
            total = exponent + column
            quotient, residue = divmod(total, degree)
            matrix[residue, column] += parameter * u**quotient
    return matrix, parameters


def verify_cayley_hamilton(
    degree: int,
    perturbation_degree: int,
) -> dict[str, object]:
    matrix, parameters = multiplication_matrix(degree, perturbation_degree)
    characteristic = matrix.charpoly().as_poly()
    coefficients = characteristic.all_coeffs()
    require(len(coefficients) == degree + 1 and coefficients[0] == 1, (
        f"unexpected characteristic polynomial in degree {degree}"
    ))

    identity = sp.eye(degree)
    evaluated = sp.zeros(degree)
    for coefficient in coefficients:
        evaluated = evaluated * matrix + coefficient * identity
    residuals = [sp.expand(entry) for entry in evaluated]
    require(all(entry == 0 for entry in residuals), (
        f"Cayley--Hamilton residual is nonzero in degree {degree}"
    ))
    return {
        "degree": degree,
        "perturbation_degree": perturbation_degree,
        "matrix_shape": [degree, degree],
        "parameter_count": len(parameters),
        "characteristic_polynomial_sha256": canonical_hash(
            sp.sstr(characteristic.as_expr())
        ),
        "all_matrix_residuals_zero": True,
    }


def active_coefficients(
    polynomial: sp.Expr,
    degree: int,
    active_residues: tuple[int, ...],
) -> list[sp.Expr]:
    expanded = sp.Poly(sp.expand(polynomial), x)
    return [
        coefficient
        for (exponent,), coefficient in expanded.terms()
        if exponent % degree in active_residues
    ]


@dataclass(frozen=True)
class IdealScreen:
    name: str
    degree: int
    perturbation_degree: int
    active_residues: tuple[int, ...]
    cutoff: int
    checked_through: int


def verify_ideal_screen(screen: IdealScreen) -> dict[str, object]:
    parameters = sp.symbols(f"a0:{screen.perturbation_degree + 1}")
    perturbation = sum(
        parameters[exponent] * x**exponent
        for exponent in range(screen.perturbation_degree + 1)
    )
    generators_by_order: dict[int, list[sp.Expr]] = {}
    cutoff_generators: list[sp.Expr] = []
    for order in range(1, screen.checked_through + 1):
        generators = active_coefficients(
            perturbation**order,
            screen.degree,
            screen.active_residues,
        )
        generators_by_order[order] = generators
        if order <= screen.cutoff:
            cutoff_generators.extend(generators)

    require(cutoff_generators, f"{screen.name}: cutoff ideal has no generators")
    basis = sp.groebner(cutoff_generators, *parameters, order="grevlex")
    reductions: list[dict[str, object]] = []
    for order in range(screen.cutoff + 1, screen.checked_through + 1):
        residuals = [
            sp.expand(basis.reduce(generator)[1])
            for generator in generators_by_order[order]
        ]
        require(all(residual == 0 for residual in residuals), (
            f"{screen.name}: generator survives the cutoff at order {order}"
        ))
        reductions.append({
            "order": order,
            "generator_count": len(generators_by_order[order]),
            "all_reduce_to_zero": True,
        })

    return {
        "case": screen.name,
        "degree": screen.degree,
        "perturbation_degree": screen.perturbation_degree,
        "active_residues": list(screen.active_residues),
        "cutoff": screen.cutoff,
        "checked_through": screen.checked_through,
        "groebner_basis": [sp.sstr(poly.as_expr()) for poly in basis.polys],
        "higher_order_reductions": reductions,
    }


def vanishes_at_dth_root(weights: tuple[int, ...], frequency: int) -> bool:
    """Test N(zeta_d^frequency)=0 by exact cyclotomic reduction."""

    degree = len(weights)
    frequency %= degree
    if frequency == 0:
        return sum(weights) == 0
    common = math.gcd(frequency, degree)
    order = degree // common
    primitive_exponent = frequency // common
    value_polynomial = sum(
        weight * z ** ((index * primitive_exponent) % order)
        for index, weight in enumerate(weights)
    )
    modulus = sp.Poly(sp.cyclotomic_poly(order, z), z, domain=sp.QQ)
    remainder = sp.rem(
        sp.Poly(value_polynomial, z, domain=sp.QQ),
        modulus,
    )
    return remainder.is_zero


def integer_cycle_witness(degree: int) -> dict[str, object]:
    """Build a rational/integer cycle whose first hit by g=x is d/p."""

    prime = least_prime_divisor(degree)
    first_order = degree // prime
    weights = tuple(
        prime - 1 if index % prime == 0 else -1
        for index in range(degree)
    )
    require(sum(weights) == 0, f"degree {degree}: weights are not a cycle")
    support = tuple(
        frequency
        for frequency in range(1, degree)
        if not vanishes_at_dth_root(weights, frequency)
    )
    expected_support = tuple(
        multiplier * first_order for multiplier in range(1, prime)
    )
    require(support == expected_support, (
        f"degree {degree}: unexpected integer-cycle Fourier support {support}"
    ))
    hits = [order for order in range(1, degree) if order % degree in support]
    require(hits and hits[0] == first_order, (
        f"degree {degree}: unexpected first hit {hits[:1]}"
    ))
    return {
        "degree": degree,
        "least_prime_divisor": prime,
        "weights": list(weights),
        "fourier_support": list(support),
        "perturbation": "g=x",
        "first_nonzero_order": first_order,
    }


def complex_cycle_witness(degree: int) -> dict[str, object]:
    """Record the character-orthogonality witness for the d-1 lower bound."""

    require(degree >= 2, "degree must be at least two")
    return {
        "degree": degree,
        "weights": "n_j=omega^j",
        "coefficient_field": "Q(omega), generally not Z",
        "fourier_support": [degree - 1],
        "perturbation": "g=x",
        "first_nonzero_order": degree - 1,
        "orthogonality_identity": (
            "sum_j omega^(j*(r+1)) is d for r=d-1 and zero otherwise"
        ),
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
    parser.add_argument("--maximum-witness-degree", type=int, default=18)
    args = parser.parse_args()
    require(args.maximum_witness_degree >= 2, (
        "maximum witness degree must be at least two"
    ))

    cayley_hamilton = [
        verify_cayley_hamilton(degree, perturbation_degree)
        for degree, perturbation_degree in (
            (2, 4),
            (3, 5),
            (4, 6),
        )
    ]
    ideal_screens = [
        verify_ideal_screen(screen)
        for screen in (
            IdealScreen("quadratic-rectangular", 2, 4, (1,), 1, 6),
            IdealScreen("cubic-rectangular-r1", 3, 5, (1,), 2, 7),
            IdealScreen("cubic-rectangular-r2", 3, 5, (2,), 2, 7),
            IdealScreen("quartic-integer-midpoint", 4, 6, (2,), 3, 8),
            IdealScreen("sextic-integer-midpoint", 6, 6, (3,), 5, 8),
            IdealScreen("sextic-published-support", 6, 6, (1, 5), 5, 8),
        )
    ]
    integer_witnesses = [
        integer_cycle_witness(degree)
        for degree in range(2, args.maximum_witness_degree + 1)
    ]
    complex_witnesses = [
        complex_cycle_witness(degree)
        for degree in range(2, args.maximum_witness_degree + 1)
    ]

    receipt: dict[str, object] = {
        "schema": "power-phase-bautin-falsification-v2",
        "status": "pass",
        "phase_family": "f=x^d",
        "coefficient_ring": "Q[a_0,...,a_n], including screened cases n>d",
        "cayley_hamilton_checks": cayley_hamilton,
        "coefficient_ideal_screens": ideal_screens,
        "integer_cycle_lower_bound_witnesses": integer_witnesses,
        "complex_cycle_sharpness_witnesses": complex_witnesses,
        "claim_boundary": {
            "established_by_exact_finite_checks": [
                "generic multiplication-matrix Cayley--Hamilton identities for d=2,...,4 with n=d+2",
                "representative rectangular coefficient-ideal reductions through order eight",
                "exact Fourier supports and first-hit orders of integer witnesses through the declared degree",
                "the algebraic character-orthogonality form of the complex-cycle witnesses",
            ],
            "requires_written_proof": [
                "ordinary coefficient-ideal stabilization by order d-1 for every d and n",
                "equivalence between active power coordinates and Melnikov coefficient ideals",
            ],
            "not_established": [
                "sharpness of d-1 when cycles are required to have integer coefficients",
                "novelty, independent review, peer review, or publication readiness",
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
