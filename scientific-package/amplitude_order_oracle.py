#!/usr/bin/env python3
"""Exact scalar-ODE certificates for polynomial-amplitude periods.

For trusted rational P,A, this program computes the first exact dependence of

    [A dx], [P A dx], [P^2 A dx], ...

in the twisted de Rham quotient.  Pairing with a flat rapid-decay cycle turns
that dependence into a scalar differential operator for

    I_{Gamma,A}(s) = integral_Gamma A(x) exp(s P(x)) dx.

The operator order is checked against the primitive-amplitude inverse-support
theorem, using the frozen Atlas implementation as one computational producer.
Minimality is for the complete period solution space; no full-order claim is
made for an arbitrary individual cycle.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any

import sympy as sp


def load_atlas(atlas_root: Path) -> dict[str, Any]:
    source_root = atlas_root / "src"
    if not source_root.is_dir():
        raise RuntimeError("Atlas src directory is missing")
    sys.path.insert(0, str(source_root))
    from amplitude_support import analyse_amplitude, parse_amplitude  # noqa: PLC0415
    from fusion_support import (  # noqa: PLC0415
        K,
        canonical_expr,
        canonical_hash,
        coordinate_column,
        first_dependence,
        parse_polynomial,
        require,
        s,
        x,
    )
    from order_oracle import (  # noqa: PLC0415
        _matrix_sha256,
        _pivot_solution,
        _primitive_integer_coefficients,
    )

    return locals()


def amplitude_operator_matrix(phase: sp.Poly, amplitude: sp.Poly, atlas: dict[str, Any]) -> sp.Matrix:
    """Return one more Krylov column than the ambient quotient dimension."""

    K = atlas["K"]
    x = atlas["x"]
    coordinate_column = atlas["coordinate_column"]
    ambient_rank = phase.degree() - 1
    phase_k = sp.Poly(phase.as_expr(), x, domain=K)
    iterate = sp.Poly(amplitude.as_expr(), x, domain=K)
    columns: list[sp.Matrix] = []
    for _ in range(ambient_rank + 1):
        columns.append(coordinate_column(iterate, phase))
        iterate *= phase_k
    return sp.Matrix.hstack(*columns)


def exact_amplitude_operator(phase: sp.Poly, amplitude: sp.Poly, atlas: dict[str, Any]) -> dict[str, Any]:
    canonical_expr = atlas["canonical_expr"]
    first_dependence = atlas["first_dependence"]
    require = atlas["require"]
    s = atlas["s"]
    matrix_sha256 = atlas["_matrix_sha256"]
    pivot_solution = atlas["_pivot_solution"]
    primitive_integer_coefficients = atlas["_primitive_integer_coefficients"]

    matrix = amplitude_operator_matrix(phase, amplitude, atlas)
    order = first_dependence(matrix)
    ambient_rank = phase.degree() - 1
    require(order <= ambient_rank, "amplitude order exceeds the twisted quotient rank")

    if order == 0:
        require(all(sp.cancel(value) == 0 for value in matrix[:, 0]), "rank-zero seed is nonzero")
        return {
            "order": 0,
            "independent_variable": "s",
            "derivation_symbol": "D_s",
            "coefficient_order": "low_derivative_to_high_derivative",
            "coefficients": ["1"],
            "equation": "I(s) = 0",
            "rank_zero_seed_column": True,
            "exact_krylov_residual_zero": True,
            "original_input_krylov_matrix_sha256": matrix_sha256(matrix),
        }

    require(order < matrix.cols, "operator matrix did not include a dependence")
    pivot_rows, solution = pivot_solution(matrix, order)
    rational_coefficients = [-sp.cancel(value) for value in solution] + [sp.Integer(1)]
    coefficients = primitive_integer_coefficients(rational_coefficients)

    residual = sp.zeros(matrix.rows, 1)
    for derivative_order, coefficient in enumerate(coefficients):
        residual += matrix[:, derivative_order] * coefficient
    require(
        all(sp.cancel(value) == 0 for value in residual),
        "primitive amplitude operator has a nonzero exact residual",
    )

    coefficient_strings = [canonical_expr(value) for value in coefficients]
    leading = sp.Poly(coefficients[-1], s, domain=sp.ZZ)
    require(leading != 0, "highest derivative coefficient vanished")
    return {
        "order": order,
        "independent_variable": "s",
        "derivation_symbol": "D_s",
        "coefficient_order": "low_derivative_to_high_derivative",
        "coefficients": coefficient_strings,
        "equation": "sum_{j=0}^q coefficients[j] * I^(j)(s) = 0",
        "leading_derivative_coefficient": coefficient_strings[-1],
        "primitive_integer_polynomial_coefficients": True,
        "pivot_rows_zero_based": pivot_rows,
        "exact_krylov_residual_zero": True,
        "original_input_krylov_matrix_sha256": matrix_sha256(matrix),
    }


def amplitude_order_certificate(
    phase_text: str,
    amplitude_text: str,
    atlas_root: Path,
    atlas: dict[str, Any] | None = None,
) -> dict[str, Any]:
    atlas = atlas or load_atlas(atlas_root)
    analyse_amplitude = atlas["analyse_amplitude"]
    canonical_hash = atlas["canonical_hash"]
    parse_amplitude = atlas["parse_amplitude"]
    parse_polynomial = atlas["parse_polynomial"]
    require = atlas["require"]

    phase = parse_polynomial(phase_text)
    amplitude = parse_amplitude(amplitude_text)
    support_analysis = analyse_amplitude(phase_text, amplitude_text)
    operator = exact_amplitude_operator(phase, amplitude, atlas)
    predicted_order = support_analysis["theorem_identity"]["primitive_inverse_support_size"]
    require(operator["order"] == predicted_order, "operator order disagrees with primitive support")

    result: dict[str, Any] = {
        "schema": "polynomial-amplitude-order-oracle-certificate-v1",
        "status": "pass",
        "input": {"phase": phase_text, "amplitude": amplitude_text},
        "input_sha256": canonical_hash({"phase": phase_text, "amplitude": amplitude_text}),
        "degree": phase.degree(),
        "order_prediction": {
            "complete_system_minimal_order_candidate": predicted_order,
            "primitive_inverse_support": support_analysis["primitive_inverse_at_infinity"]["support"],
            "primitive_inverse_support_size": predicted_order,
            "twisted_amplitude_cyclic_rank": support_analysis["theorem_identity"][
                "twisted_amplitude_cyclic_rank"
            ],
            "reduced_primitive_root_span_dimension": support_analysis["theorem_identity"][
                "reduced_B_root_span_dimension"
            ],
            "all_equal": support_analysis["theorem_identity"]["all_equal"],
        },
        "scalar_operator_for_original_inputs": operator,
        "atlas_amplitude_certificate_sha256": support_analysis["certificate_sha256"],
        "claim_boundary": {
            "annihilation": (
                "The displayed operator annihilates every flat rapid-decay period "
                "I_Gamma,A(s)=integral_Gamma A(x) exp(sP(x)) dx."
            ),
            "minimality": (
                "By the reconstructed amplitude-support theorem and the nondegenerate rapid-decay period pairing, "
                "its order is minimal for one operator annihilating the complete period system. "
                "No generic-individual-period minimality claim is made."
            ),
            "input": "Trusted rational polynomial expressions only.",
            "not_established": [
                "rapid decay of an arbitrary supplied contour",
                "minimality for every individual cycle",
                "generic-individual-period minimality",
                "independent implementation",
                "novelty, priority, specialist review, or publication readiness",
            ],
        },
    }
    result["certificate_sha256"] = canonical_hash(result)
    return result


def verify_amplitude_order_certificate(
    certificate: dict[str, Any], atlas_root: Path, atlas: dict[str, Any] | None = None
) -> dict[str, Any]:
    atlas = atlas or load_atlas(atlas_root)
    canonical_hash = atlas["canonical_hash"]
    require = atlas["require"]

    require(isinstance(certificate, dict), "certificate must be a JSON object")
    require(
        certificate.get("schema") == "polynomial-amplitude-order-oracle-certificate-v1",
        "unknown amplitude oracle certificate schema",
    )
    supplied_digest = certificate.get("certificate_sha256")
    require(isinstance(supplied_digest, str), "certificate digest is missing")
    unhashed = dict(certificate)
    unhashed.pop("certificate_sha256", None)
    require(canonical_hash(unhashed) == supplied_digest, "certificate digest mismatch")
    inputs = certificate.get("input", {})
    phase = inputs.get("phase")
    amplitude = inputs.get("amplitude")
    require(isinstance(phase, str) and isinstance(amplitude, str), "certificate inputs are missing")
    recomputed = amplitude_order_certificate(phase, amplitude, atlas_root, atlas)
    require(recomputed == certificate, "certificate differs from exact recomputation")
    return {
        "schema": "polynomial-amplitude-order-oracle-verification-v1",
        "status": "pass",
        "certificate_sha256": supplied_digest,
        "phase": phase,
        "amplitude": amplitude,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--atlas-root", type=Path, required=True)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--phase")
    action.add_argument("--verify-certificate", type=Path)
    parser.add_argument("--amplitude")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()

    atlas = load_atlas(args.atlas_root)
    if args.verify_certificate:
        supplied = json.loads(args.verify_certificate.read_text(encoding="utf-8"))
        result = verify_amplitude_order_certificate(supplied, args.atlas_root, atlas)
    else:
        atlas["require"](isinstance(args.amplitude, str), "--amplitude is required with --phase")
        result = amplitude_order_certificate(args.phase, args.amplitude, args.atlas_root, atlas)
    encoded = json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n" if args.compact else json.dumps(
        result, indent=2, sort_keys=True
    ) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
    else:
        print(encoded, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
