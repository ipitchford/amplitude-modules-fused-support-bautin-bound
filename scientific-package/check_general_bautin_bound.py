#!/usr/bin/env python3
"""Exact structural checks for the unrestricted zero-cycle Bautin bound.

For a monic phase f of degree d and a perturbation g of any fixed degree n,
this script constructs multiplication by g in

    Q[f_0,...,f_(d-1),a_0,...,a_n,t,x]/(f(x)-t).

It verifies Cayley--Hamilton in small generic cases with n>d, where the old
affine-in-t proof no longer applies.  It also checks the cyclic averaging
identity used in the new injectivity lemma: averaging any zero-sum cycle over
the d-cycle at infinity gives the zero cycle.  The written proof combines
this injectivity with the undifferentiated moment recurrence, so no bound on
the t-degree of the characteristic coefficients is required.

These are exact falsification checks.  The general theorem rests on the
written quotient-ring and content-ideal proof.
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
t = sp.Symbol("t")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def generic_multiplication_matrix(
    degree: int,
    perturbation_degree: int,
) -> tuple[sp.Matrix, tuple[sp.Symbol, ...], tuple[sp.Symbol, ...]]:
    require(degree >= 2, "degree must be at least two")
    require(perturbation_degree >= 0, "perturbation degree must be nonnegative")
    phase_parameters = sp.symbols(f"p0:{degree}")
    perturbation_parameters = sp.symbols(f"a0:{perturbation_degree + 1}")
    phase = x**degree + sum(
        phase_parameters[index] * x**index for index in range(degree)
    )
    perturbation = sum(
        perturbation_parameters[index] * x**index
        for index in range(perturbation_degree + 1)
    )
    modulus = sp.Poly(phase - t, x, domain=sp.EX)
    matrix = sp.zeros(degree)
    for column in range(degree):
        remainder = sp.rem(
            sp.Poly(sp.expand(perturbation * x**column), x, domain=sp.EX),
            modulus,
        )
        for (row,), coefficient in remainder.terms():
            matrix[row, column] = sp.expand(coefficient)
    return matrix, phase_parameters, perturbation_parameters


def verify_generic_case(
    degree: int,
    perturbation_degree: int,
) -> dict[str, object]:
    matrix, phase_parameters, perturbation_parameters = (
        generic_multiplication_matrix(degree, perturbation_degree)
    )
    characteristic = matrix.charpoly().as_poly()
    coefficients = characteristic.all_coeffs()
    require(len(coefficients) == degree + 1 and coefficients[0] == 1, (
        f"degree {degree}: malformed characteristic polynomial"
    ))

    coefficient_records: list[dict[str, object]] = []
    for index, coefficient in enumerate(coefficients[1:], start=1):
        polynomial = sp.Poly(sp.expand(coefficient), t, domain=sp.EX)
        t_degree = int(polynomial.degree())
        coefficient_records.append({
            "characteristic_index": index,
            "t_degree": t_degree,
            "coefficient_sha256": canonical_hash(sp.sstr(sp.expand(coefficient))),
        })

    identity = sp.eye(degree)
    evaluated = sp.zeros(degree)
    for coefficient in coefficients:
        evaluated = evaluated * matrix + coefficient * identity
    residuals = [sp.expand(entry) for entry in evaluated]
    require(all(entry == 0 for entry in residuals), (
        f"degree {degree}: Cayley--Hamilton residual is nonzero"
    ))
    return {
        "degree": degree,
        "perturbation_degree": perturbation_degree,
        "phase_parameter_count": len(phase_parameters),
        "perturbation_parameter_count": len(perturbation_parameters),
        "maximum_matrix_entry_t_degree": max(
            int(sp.Poly(entry, t, domain=sp.EX).degree())
            for entry in matrix
        ),
        "characteristic_coefficients": coefficient_records,
        "cayley_hamilton_residual_is_zero": True,
        "multiplication_matrix_sha256": canonical_hash(
            [sp.sstr(entry) for entry in matrix]
        ),
    }


def verify_cycle_average(degree: int) -> dict[str, object]:
    """Check that averaging a zero-sum cycle over infinity monodromy is zero."""

    weights = list(sp.symbols(f"n0:{degree - 1}"))
    weights.append(-sum(weights))
    rotations = [
        weights[-shift:] + weights[:-shift]
        for shift in range(degree)
    ]
    averaged_numerators = [
        sp.expand(sum(rotation[index] for rotation in rotations))
        for index in range(degree)
    ]
    require(all(value == 0 for value in averaged_numerators), (
        f"degree {degree}: cyclic average of a zero-sum cycle is nonzero"
    ))
    return {
        "degree": degree,
        "rotation_count": degree,
        "zero_sum_substitution": f"n_{degree - 1}=-sum(n_0,...,n_{degree - 2})",
        "all_averaged_cycle_coordinates_zero": True,
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
    parser.add_argument("--maximum-symbolic-degree", type=int, default=3)
    parser.add_argument("--degree-excess", type=int, default=2)
    parser.add_argument("--maximum-cycle-degree", type=int, default=12)
    args = parser.parse_args()
    require(2 <= args.maximum_symbolic_degree <= 4, (
        "maximum symbolic degree must lie between two and four"
    ))
    require(args.degree_excess >= 1, "degree excess must be positive")
    require(args.maximum_cycle_degree >= args.maximum_symbolic_degree, (
        "maximum cycle degree must cover the symbolic degrees"
    ))

    degrees = range(2, args.maximum_symbolic_degree + 1)
    generic_checks = [
        verify_generic_case(degree, degree + args.degree_excess)
        for degree in degrees
    ]
    cycle_average_checks = [
        verify_cycle_average(degree)
        for degree in range(2, args.maximum_cycle_degree + 1)
    ]

    receipt: dict[str, object] = {
        "schema": "general-zero-cycle-bautin-bound-falsification-v2",
        "status": "pass",
        "scope": {
            "phase": "monic f of degree d",
            "perturbation": "g of arbitrary fixed finite degree",
            "cycle": "arbitrary zero-cycle of f",
            "candidate_bound": "ordinary coefficient Bautin ideal stabilizes by d-1",
        },
        "generic_quotient_checks": generic_checks,
        "cycle_average_checks": cycle_average_checks,
        "claim_boundary": {
            "established_by_exact_finite_checks": [
                "generic quotient multiplication matrices with deg(g)>deg(f) in the declared symbolic degrees",
                "Cayley--Hamilton identities in those degrees",
                "cyclic averaging of generic zero-sum cycles through the declared degree",
            ],
            "requires_written_proof": [
                "the all-degree quotient-ring argument",
                "the basis-independent content-ideal argument",
                "the all-order Melnikov identity",
                "injectivity of every positive t-derivative on zero-cycle polynomial integrals",
            ],
            "not_established": [
                "sharpness for integer-weighted cycles in every degree",
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
