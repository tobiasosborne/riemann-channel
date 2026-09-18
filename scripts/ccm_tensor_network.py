#!/usr/bin/env python3
"""Deterministic finite tensor-network and CCM rank-one checks.

The small algebraic fixtures use exact SymPy arithmetic.  NumPy is used only
as an independent floating-point check of the two-dimensional CCM quotient.
Every failed condition raises CheckFailure, including under ``python -O``.

Run from the repository root:

    python3 scripts/ccm_tensor_network.py --self-test
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import subprocess
import sys
import tempfile

import numpy as np
import sympy as sp


class CheckFailure(RuntimeError):
    """A certificate condition failed."""


N_CHECKS = 0
CCM_BOUNDARY_MODE = "eta"  # MUTATION_TARGET_CCM_BOUNDARY
CLOCK_FEATURE_MODE = "conjugated"  # MUTATION_TARGET_CLOCK_FEATURE


def require(condition: bool, message: str) -> None:
    """Raise an explicit exception on failure, and count atomic checks."""
    global N_CHECKS
    N_CHECKS += 1
    if not bool(condition):
        raise CheckFailure(message)


def require_matrix(actual: sp.Matrix, expected: sp.Matrix, message: str) -> None:
    require(actual.shape == expected.shape, message + " (shape)")
    difference = actual - expected
    require(all(sp.simplify(x) == 0 for x in difference), message)


def matrix_polynomial(matrix: sp.Matrix, coefficients: list[sp.Expr]) -> sp.Matrix:
    result = sp.zeros(matrix.rows)
    power = sp.eye(matrix.rows)
    for coefficient in coefficients:
        result += coefficient * power
        power *= matrix
    return sp.simplify(result)


def hs_inner(left: sp.Matrix, right: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(left.conjugate().T * right))


def metric_hs_inner(left: sp.Matrix, right: sp.Matrix, metric: sp.Matrix) -> sp.Expr:
    # The metric adjoint is A^sharp = metric^{-1} A^dagger metric.
    return sp.simplify(sp.trace(metric.inv() * left.conjugate().T * metric * right))


def gram(powers: list[sp.Matrix], inner) -> sp.Matrix:
    return sp.Matrix([[inner(left, right) for right in powers] for left in powers])


def case_permutation_gns() -> str:
    """The (12)(345) transfer: counts, kernel, and cyclic quotient."""
    permutation = [1, 0, 3, 4, 2]
    transfer = sp.zeros(5)
    for source, target in enumerate(permutation):
        transfer[target, source] = 1

    counts = [sp.trace(transfer**n) for n in range(7)]
    require(counts == [5, 0, 2, 3, 2, 0, 5], "permutation fixed-point counts")

    powers = [transfer**j for j in range(5)]
    moment_gram = gram(powers, hs_inner)
    require(moment_gram.rank() == 4, "permutation moment Gram has rank four")

    # p(z) = lcm(z^2-1,z^3-1) = z^4+z^3-z-1.
    kernel_polynomial = sp.Matrix([-1, -1, 0, 1, 1])
    require_matrix(moment_gram * kernel_polynomial, sp.zeros(5, 1), "minimal polynomial is Gram-null")
    require_matrix(
        matrix_polynomial(transfer, list(kernel_polynomial)),
        sp.zeros(5),
        "minimal polynomial annihilates permutation transfer",
    )

    quotient_metric = moment_gram[:4, :4]
    for size in range(1, 5):
        require(quotient_metric[:size, :size].det() > 0, "quotient Gram is positive definite")
    multiplication = sp.Matrix(
        [
            [0, 0, 0, 1],
            [1, 0, 0, 1],
            [0, 1, 0, 0],
            [0, 0, 1, -1],
        ]
    )
    require_matrix(
        multiplication.T * quotient_metric * multiplication,
        quotient_metric,
        "quotient multiplication is unitary in the moment metric",
    )
    z = sp.symbols("z")
    require(
        sp.expand(multiplication.charpoly(z).as_expr()) == z**4 + z**3 - z - 1,
        "quotient characteristic polynomial",
    )
    return "counts [5,0,2,3,2,0,5]; Gram rank 4; kernel p=z^4+z^3-z-1"


def case_pauli_corrected_metric() -> str:
    """The retained F_5 Pauli block is nonnormal but metric-unitary."""
    root5 = sp.sqrt(5)
    transfer = sp.Matrix([[0, -5], [1, -2]]) / root5
    metric = sp.Matrix([[1, -1], [-1, 5]])
    require(metric[0, 0] > 0 and metric.det() > 0, "Pauli corrected metric is positive")
    require_matrix(transfer.T * metric * transfer, metric, "Pauli block is metric-unitary")
    require_matrix(
        matrix_polynomial(transfer, [1, 2 / root5, 1]),
        sp.zeros(2),
        "Pauli moment polynomial annihilates the transfer",
    )
    require(transfer.T * transfer != transfer * transfer.T, "Pauli block is nonnormal natively")

    powers = [transfer**j for j in range(3)]
    corrected = gram(powers, lambda left, right: metric_hs_inner(left, right, metric))
    native = gram(powers, hs_inner)
    moments = [sp.simplify(sp.trace(transfer**n)) for n in range(3)]
    toeplitz = sp.Matrix(3, 3, lambda j, k: moments[abs(k - j)])
    require_matrix(corrected, toeplitz, "corrected operator Gram equals trace-moment Toeplitz matrix")
    require(native != toeplitz, "native Hilbert-Schmidt Gram differs from moment Toeplitz matrix")
    require(hs_inner(transfer, transfer) == 6, "native Pauli block norm squared is six")
    require(metric_hs_inner(transfer, transfer, metric) == 2, "corrected Pauli block norm squared is two")

    kernel = sp.Matrix([1, 2 / root5, 1])
    require_matrix(toeplitz * kernel, sp.zeros(3, 1), "Pauli Toeplitz kernel polynomial")
    lam = sp.symbols("lam")
    expected = lam * (lam - sp.Rational(14, 5)) * (lam - sp.Rational(16, 5))
    require(sp.factor(toeplitz.charpoly(lam).as_expr() - expected) == 0, "Pauli Toeplitz spectrum")
    return "native ||U||_HS^2=6, corrected=2; Toeplitz spectrum {0,14/5,16/5}"


def case_jordan_blindness() -> str:
    """Trace moments forget the nilpotent part of a Jordan block."""
    jordan = sp.Matrix([[1, 1], [0, 1]])
    diagonal = sp.eye(2)
    jordan_counts = [sp.trace(jordan**n) for n in range(6)]
    diagonal_counts = [sp.trace(diagonal**n) for n in range(6)]
    require(jordan_counts == diagonal_counts == [2] * 6, "Jordan and diagonal counts coincide")

    moment_matrix = sp.ones(2, 2) * 2
    annihilator = sp.Matrix([-1, 1])
    require_matrix(moment_matrix * annihilator, sp.zeros(2, 1), "z-1 is moment-null")
    require_matrix(matrix_polynomial(diagonal, list(annihilator)), sp.zeros(2), "z-1 kills diagonal model")
    residual = matrix_polynomial(jordan, list(annihilator))
    require(residual != sp.zeros(2), "moment annihilator does not kill original Jordan transfer")
    require(hs_inner(residual, residual) == 1, "Jordan nilpotent residual has norm squared one")
    return "same counts 2; p=z-1 is GNS-null but ||p(J)||_HS^2=1"


def case_scalar_needs_duality() -> str:
    """A positive Toeplitz sequence can come from a strict contraction."""
    radius = sp.Rational(1, 2)
    toeplitz = sp.Matrix(4, 4, lambda j, k: radius ** abs(k - j))
    determinants = [sp.factor(toeplitz[:size, :size].det()) for size in range(1, 5)]
    require(determinants == [1, sp.Rational(3, 4), sp.Rational(9, 16), sp.Rational(27, 64)], "scalar Toeplitz minors")
    native = sp.Matrix(4, 4, lambda j, k: radius ** (j + k))
    require(native != toeplitz, "strict-contraction Toeplitz form is not the native powers Gram")
    reflected = 1 / radius
    require(radius < 1 and reflected != radius, "strict contraction lacks inversion duality")
    return "r=1/2; leading minors [1,3/4,9/16,27/64]; reflected point is 2"


def case_underresolved_minimum() -> str:
    """A degenerate finite-window minimum does not identify the support."""
    omega = (-1 + sp.I * sp.sqrt(3)) / 2
    transfer = sp.diag(1, omega, omega**2)
    require_matrix(transfer**3, sp.eye(3), "three-mode fixture lies on the unit circle")

    short_powers = [transfer**j for j in range(2)]
    short_gram = gram(short_powers, hs_inner)
    require_matrix(short_gram, 3 * sp.eye(2), "underresolved two-power Gram is scalar")
    shifted = short_gram - 3 * sp.eye(2)
    require_matrix(shifted, sp.zeros(2), "underresolved shifted Gram has two-dimensional radical")

    arbitrary_minimizer = sp.Matrix([1, sp.Rational(-1, 2)])
    require(1 - sp.Rational(1, 2) * 2 == 0, "arbitrary minimizer polynomial has root two")
    require(2 not in list(transfer.diagonal()), "spurious root is outside the true support")
    require(
        matrix_polynomial(transfer, list(arbitrary_minimizer)) != sp.zeros(3),
        "arbitrary underresolved minimizer does not annihilate transfer",
    )

    resolved_powers = [transfer**j for j in range(4)]
    resolved_gram = gram(resolved_powers, hs_inner)
    true_kernel = sp.Matrix([-1, 0, 0, 1])
    require(resolved_gram.rank() == 3, "resolved Gram has the support cardinality")
    require_matrix(resolved_gram * true_kernel, sp.zeros(4, 1), "resolved kernel is z^3-1")
    require_matrix(
        matrix_polynomial(transfer, list(true_kernel)),
        sp.zeros(3),
        "resolved kernel annihilates transfer",
    )
    return "W_short=3I_2 has arbitrary root 2; resolved kernel is z^3-1"


def case_signed_grading() -> str:
    """The raw supertrace form is indefinite; arranging signs recovers a Gram."""
    even = sp.Matrix([[1]])
    odd = sp.diag(sp.I, -sp.I)
    even_powers = [even**j for j in range(3)]
    odd_powers = [odd**j for j in range(3)]
    even_gram = gram(even_powers, hs_inner)
    odd_gram = gram(odd_powers, hs_inner)
    signed = even_gram - odd_gram

    negative_vector = sp.Matrix([1, 0, 0])
    positive_vector = sp.Matrix([1, 0, 1])
    negative_value = (negative_vector.T * signed * negative_vector)[0]
    positive_value = (positive_vector.T * signed * positive_vector)[0]
    require(negative_value == -1 and positive_value == 4, "raw supertrace form is indefinite")

    # If s_n=tr(E_even^n)-tr(E_odd^n) and t_n is the trivial even
    # contribution, then t_n-s_n=tr(E_odd^n), including n=0.
    arranged = sp.Matrix(
        3,
        3,
        lambda j, k: sp.trace(odd ** (k - j)),
    )
    require_matrix(arranged, odd_gram, "trivial-even removal and sign arrangement gives odd Gram")
    require(arranged.rank() == 2, "arranged graded Gram has the expected rank")
    require_matrix(arranged * positive_vector, sp.zeros(3, 1), "z^2+1 is the arranged kernel")
    return "raw quadratic values -1 and +4; arranged odd Gram is PSD of rank 2"


def case_physical_parent_space() -> str:
    """The physical parent space is ker(Gamma^dagger), not ker(Gamma)."""
    gamma = sp.Matrix([[1], [0]])
    require(len(gamma.nullspace()) == 0, "Gamma:C->C^2 has no boundary-data kernel")
    adjoint_kernel = gamma.conjugate().T.nullspace()
    require(len(adjoint_kernel) == 1, "Gamma adjoint has one-dimensional physical parent space")
    require_matrix(adjoint_kernel[0], sp.Matrix([0, 1]), "physical parent vector is the unused letter")
    parent_projector = adjoint_kernel[0] * adjoint_kernel[0].conjugate().T
    require_matrix(parent_projector * gamma, sp.zeros(2, 1), "physical parent projector kills im Gamma")
    require(parent_projector.rank() == 1, "physical parent projector is nonzero")
    return "ker Gamma=0; ker Gamma^dagger=span{|1>}; parent projector rank 1"


def case_unary_automaton() -> str:
    """Exact small instance of the bounded-bond unary-clock automaton."""
    phases = [sp.Integer(1), sp.I]
    spectral_projectors = [sp.diag(1, 0), sp.diag(0, 1)]
    phase_matrix = sp.diag(*phases)
    zero = sp.zeros(2)
    identity = sp.eye(2)
    letter_one = phase_matrix.row_join(zero).col_join(zero.row_join(zero))
    letter_zero = zero.row_join(identity).col_join(zero.row_join(identity))
    require_matrix(letter_zero * letter_one, sp.zeros(4), "unary automaton rejects substring 01")

    start = sp.Matrix([[1, 1, 0, 0]])
    endpoint_columns = [
        sp.Matrix.vstack(*[projector[:, column] for column in range(2)])
        for projector in spectral_projectors
    ]
    endpoint = sp.Matrix.vstack(
        endpoint_columns[0].T,
        endpoint_columns[1].T,
        endpoint_columns[0].T,
        endpoint_columns[1].T,
    )
    transfer = sp.diag(*phases)
    nonzero_words = []
    for word_number in range(8):
        word = tuple((word_number >> shift) & 1 for shift in (2, 1, 0))
        amplitude = start
        for symbol in word:
            amplitude *= letter_one if symbol else letter_zero
        feature = amplitude * endpoint
        is_unary = all(word[position] >= word[position + 1] for position in range(2))
        if is_unary:
            ones = sum(word)
            expected_matrix = transfer**ones
            expected = sp.Matrix.vstack(*[expected_matrix[:, column] for column in range(2)]).T
            require_matrix(feature, expected, "unary automaton emits the correct transfer power")
            nonzero_words.append("".join(map(str, word)))
        else:
            require_matrix(feature, sp.zeros(1, 4), "unary automaton kills a non-unary clock word")
    require(nonzero_words == ["000", "100", "110", "111"], "unary automaton accepted-word language")
    return "bond 4; accepted {000,100,110,111}; endpoints are vec(I),vec(U),vec(U^2),vec(U^3)"


def case_clock_partial_trace() -> str:
    """Partial trace, null projector, and propagation-history Hamiltonian."""
    transfer = sp.diag(1, sp.I)
    powers = [transfer**j for j in range(3)]
    # Column-stacking convention: vec(UA)=(I tensor U)vec(A).
    features = [sp.Matrix.vstack(*[power[:, column] for column in range(power.cols)]) for power in powers]
    feature_map = sp.Matrix.hstack(*features)
    # Rows are the amplitudes of |j>_clock tensor |vec(E^j)>_register.
    amplitudes = feature_map.T
    rho_clock = amplitudes * amplitudes.conjugate().T
    conventional_gram = gram(powers, hs_inner)
    require_matrix(rho_clock, conventional_gram.T, "clock partial trace equals Gram transpose")
    require_matrix(rho_clock, conventional_gram.conjugate(), "Hermitian Gram transpose is its conjugate")
    require(rho_clock != conventional_gram, "complex fixture detects an omitted transpose")
    require(rho_clock[0, 1] == 1 - sp.I and conventional_gram[0, 1] == 1 + sp.I, "clock off-diagonal convention")
    require(sp.trace(rho_clock) == 6, "unnormalized clock state has the expected norm")

    # Conjugating every feature is the convention used for the canonical
    # history: its clock marginal is W itself, not W^T.
    conjugated_features = [feature.conjugate() for feature in features]
    conjugated_amplitudes = sp.Matrix.hstack(*conjugated_features).T
    conjugated_rho = conjugated_amplitudes * conjugated_amplitudes.conjugate().T
    conjugated_history = sp.Matrix.vstack(*conjugated_features)
    canonical_rho = conjugated_rho if CLOCK_FEATURE_MODE == "conjugated" else rho_clock
    canonical_history = conjugated_history if CLOCK_FEATURE_MODE == "conjugated" else sp.Matrix.vstack(*features)
    require_matrix(canonical_rho, conventional_gram, "conjugated-feature clock marginal equals Gram")

    # p(z)=(z-1)(z-i)=z^2-(1+i)z+i.  Gram's null vector is
    # xi, whereas the history state is killed by the clock projector onto
    # conjugate(xi); this is where the transpose of rho_clock matters.
    xi = sp.Matrix([sp.I, -(1 + sp.I), 1])
    require_matrix(conventional_gram * xi, sp.zeros(3, 1), "clock Gram null polynomial")
    history = sp.Matrix.vstack(*features)
    conjugate_xi = xi.conjugate()
    null_projector = conjugate_xi * conjugate_xi.conjugate().T / (conjugate_xi.conjugate().T * conjugate_xi)[0]
    require_matrix(
        sp.kronecker_product(null_projector, sp.eye(4)) * history,
        sp.zeros(12, 1),
        "conjugated Gram-null clock projector annihilates history",
    )
    wrong_projector = xi * xi.conjugate().T / (xi.conjugate().T * xi)[0]
    wrong_history = sp.kronecker_product(wrong_projector, sp.eye(4)) * history
    require(hs_inner(wrong_history, wrong_history) == 2, "unconjugated clock projector must fail")
    gram_kernel_projector = xi * xi.conjugate().T / (xi.conjugate().T * xi)[0]
    require_matrix(
        sp.kronecker_product(gram_kernel_projector, sp.eye(4)) * canonical_history,
        sp.zeros(12, 1),
        "ker Gram projector annihilates conjugated-feature history",
    )

    # Feynman-Kitaev propagation checks a different null relation.  Its
    # ground history is fixed by the local recurrence psi_{j+1}=V psi_j.
    register_step = sp.kronecker_product(sp.eye(2), transfer.conjugate())
    propagation = sp.zeros(12)
    for clock in range(2):
        current = sp.zeros(3)
        following = sp.zeros(3)
        forward = sp.zeros(3)
        current[clock, clock] = 1
        following[clock + 1, clock + 1] = 1
        forward[clock + 1, clock] = 1
        local_term = sp.kronecker_product(current + following, sp.eye(4))
        local_term -= sp.kronecker_product(forward, register_step)
        local_term -= sp.kronecker_product(forward.T, register_step.conjugate().T)
        require_matrix(local_term * local_term, 2 * local_term, "propagation local term is positive")
        propagation += local_term
    require_matrix(propagation, propagation.conjugate().T, "propagation Hamiltonian is Hermitian")
    require_matrix(
        propagation * conjugated_history,
        sp.zeros(12, 1),
        "propagation Hamiltonian annihilates conjugated-feature history",
    )
    require(propagation.rank() == 8, "three-clock propagation Hamiltonian has four-dimensional kernel")

    clock_zero = sp.zeros(3)
    clock_zero[0, 0] = 1
    initial_feature = conjugated_features[0]
    initial_projector = initial_feature * initial_feature.conjugate().T / hs_inner(initial_feature, initial_feature)
    pin = sp.kronecker_product(clock_zero, sp.eye(4) - initial_projector)
    require_matrix(pin, pin.conjugate().T, "history pin is Hermitian")
    require_matrix(pin * pin, pin, "history pin is a positive projector")
    pinned = propagation + pin
    require_matrix(pinned * conjugated_history, sp.zeros(12, 1), "pinned Hamiltonian keeps target history")
    require(pinned.rank() == 11, "pinned history Hamiltonian has a unique ground-state line")
    return "literal rho=W^T; conjugated rho=W; ker-W parent and uniquely pinned FK history verified"


def case_ccm_loewner() -> str:
    """Exact three-mode CCM Loewner, quotient, and boundary identities."""
    indices = [-1, 0, 1]
    scaling = sp.diag(*indices)
    base_form = sp.Matrix([[6, 2, 2], [2, 1, 2], [2, 2, 6]])
    shift = sp.Rational(7, 3)
    tau = base_form + shift * sp.eye(3)
    epsilon = shift
    shifted_form = tau - epsilon * sp.eye(3)
    beta = sp.Matrix([-2, 0, 2])
    eta = sp.ones(3, 1)
    xi = sp.Matrix([sp.Rational(-1, 2), 2, sp.Rational(-1, 2)])

    # M is induced by a real signed point distribution on [0,2*pi].
    nodes = [sp.pi / 2, sp.pi, 3 * sp.pi / 2]
    weights = [(7 - sp.pi) / 2, -6, (7 + 3 * sp.pi) / 2]
    for row, n in enumerate(indices):
        distribution_b = -sum(weight * sp.sin(n * node) for node, weight in zip(nodes, weights)) / sp.pi
        distribution_a = 2 * sum(
            weight * (1 - node / (2 * sp.pi)) * sp.cos(n * node)
            for node, weight in zip(nodes, weights)
        )
        require(sp.simplify(distribution_b - beta[row]) == 0, "real distribution gives CCM b_n")
        require(sp.simplify(distribution_a - base_form[row, row]) == 0, "real distribution gives CCM a_n")

    for row, i in enumerate(indices):
        for column, j in enumerate(indices):
            if i != j:
                expected = sp.simplify((beta[row] - beta[column]) / (i - j))
                require(tau[row, column] == expected, "CCM off-diagonal Loewner entry")
    require_matrix(
        scaling * tau - tau * scaling,
        beta * eta.T - eta * beta.T,
        "CCM rank-two displacement identity",
    )
    require(sp.factor(shifted_form.charpoly().as_expr()) == sp.Symbol("lambda") * (sp.Symbol("lambda") - 4) * (sp.Symbol("lambda") - 9), "shifted form spectrum")
    require_matrix(shifted_form * xi, sp.zeros(3, 1), "CCM minimal vector spans shifted-form kernel")
    require((eta.T * xi)[0] == 1, "CCM boundary normalization")

    center_boundary = sp.Matrix([0, sp.Rational(1, 2), 0])
    boundary = eta if CCM_BOUNDARY_MODE == "eta" else center_boundary
    corrected = scaling - (scaling * xi) * boundary.T
    require_matrix(corrected * xi, sp.zeros(3, 1), "CCM corrected operator kills kernel vector")
    require_matrix(
        shifted_form * corrected,
        corrected.T * shifted_form,
        "CCM corrected operator is symmetric in shifted metric",
    )

    # Representatives e_-1,e_1 and a left section that kills xi.
    representatives = sp.Matrix([[1, 0], [0, 0], [0, 1]])
    section = sp.Matrix([[1, sp.Rational(1, 4), 0], [0, sp.Rational(1, 4), 1]])
    require_matrix(section * representatives, sp.eye(2), "CCM quotient section")
    require_matrix(section * xi, sp.zeros(2, 1), "CCM quotient section kills radical")
    quotient_operator = section * corrected * representatives
    quotient_metric = representatives.T * shifted_form * representatives
    require_matrix(
        quotient_metric * quotient_operator,
        quotient_operator.T * quotient_metric,
        "CCM quotient is metric-self-adjoint",
    )
    spectral_parameter = sp.symbols("s")
    require(
        sp.expand((quotient_operator - spectral_parameter * sp.eye(2)).det()) == spectral_parameter**2 - 2,
        "CCM quotient characteristic polynomial",
    )
    secular = sp.simplify(
        (scaling - spectral_parameter * sp.eye(3)).det()
        * sum(xi[j] / (indices[j] - spectral_parameter) for j in range(3))
    )
    require(sp.cancel(secular - (spectral_parameter**2 - 2)) == 0, "CCM secular determinant identity")

    numeric_operator = np.array(quotient_operator.tolist(), dtype=float)
    numeric_spectrum = np.linalg.eigvals(numeric_operator)
    require(float(np.max(np.abs(numeric_spectrum.imag))) < 1e-14, "CCM quotient spectrum is numerically real")
    require(
        np.allclose(np.sort(numeric_spectrum.real), [-np.sqrt(2.0), np.sqrt(2.0)], rtol=0, atol=1e-14),
        "CCM quotient numerical roots",
    )

    # This wrong functional is normalized on xi and still makes D_bad xi=0.
    # It nevertheless destroys metric self-adjointness.
    wrong = scaling - (scaling * xi) * center_boundary.T
    require((center_boundary.T * xi)[0] == 1, "wrong CCM boundary remains normalized")
    require_matrix(wrong * xi, sp.zeros(3, 1), "wrong CCM boundary still kills xi")
    wrong_residual = shifted_form * wrong - wrong.T * shifted_form
    residual_squared = sum(entry**2 for entry in wrong_residual)
    require(residual_squared == 36, "wrong CCM boundary must fail metric symmetry")
    return "real-distribution M spectrum {0,4,9}; quotient roots +/-sqrt(2); wrong-boundary residual^2=36"


CASES = [
    ("permutation Gram/kernel/quotient", case_permutation_gns),
    ("Pauli nonnormal corrected metric", case_pauli_corrected_metric),
    ("Jordan trace blindness", case_jordan_blindness),
    ("scalar Toeplitz needs duality", case_scalar_needs_duality),
    ("underresolved minimal eigenvector", case_underresolved_minimum),
    ("signed grading arrangement", case_signed_grading),
    ("physical parent adjoint kernel", case_physical_parent_space),
    ("unary-clock automaton", case_unary_automaton),
    ("clock-register partial trace", case_clock_partial_trace),
    ("CCM Loewner rank-one", case_ccm_loewner),
]


def run_cases(only_ccm: bool = False, only_clock: bool = False) -> None:
    if only_ccm:
        selected = CASES[-1:]
    elif only_clock:
        selected = [(name, function) for name, function in CASES if function is case_clock_partial_trace]
    else:
        selected = CASES
    for name, function in selected:
        try:
            detail = function()
        except CheckFailure as error:
            raise CheckFailure(f"{name}: {error}") from error
        print(f"PASS {name} | {detail}")


def run_red_mutation() -> None:
    """Mutate a copied checker and require the copy to exit nonzero."""
    source_path = Path(__file__).resolve()
    source = source_path.read_text(encoding="utf-8")
    target = 'CCM_BOUNDARY_MODE = ' + '"eta"' + '  # MUTATION_TARGET_CCM_BOUNDARY'
    replacement = 'CCM_BOUNDARY_MODE = ' + '"center"' + '  # MUTATION_TARGET_CCM_BOUNDARY'
    require(source.count(target) == 1, "red mutation target is unique")
    mutated = source.replace(target, replacement, 1)
    with tempfile.TemporaryDirectory(prefix="ccm-tn-red-") as temporary_directory:
        copied_path = Path(temporary_directory) / source_path.name
        copied_path.write_text(mutated, encoding="utf-8")
        environment = os.environ.copy()
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        process = subprocess.run(
            [sys.executable, str(copied_path), "--mutation-probe"],
            cwd=temporary_directory,
            env=environment,
            text=True,
            capture_output=True,
            check=False,
        )
    combined = process.stdout + process.stderr
    require(process.returncode != 0, "mutated checker must exit nonzero")
    require("FAIL CCM Loewner rank-one" in combined, "mutation must reach the intended CCM failure")
    print("PASS red mutation | copied eta->center boundary is rejected with nonzero exit")


def run_clock_red_mutation() -> None:
    """Replace conjugated history by literal features in a copied checker."""
    source_path = Path(__file__).resolve()
    source = source_path.read_text(encoding="utf-8")
    target = 'CLOCK_FEATURE_MODE = ' + '"conjugated"' + '  # MUTATION_TARGET_CLOCK_FEATURE'
    replacement = 'CLOCK_FEATURE_MODE = ' + '"literal"' + '  # MUTATION_TARGET_CLOCK_FEATURE'
    require(source.count(target) == 1, "clock red mutation target is unique")
    mutated = source.replace(target, replacement, 1)
    with tempfile.TemporaryDirectory(prefix="ccm-tn-clock-red-") as temporary_directory:
        copied_path = Path(temporary_directory) / source_path.name
        copied_path.write_text(mutated, encoding="utf-8")
        environment = os.environ.copy()
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        process = subprocess.run(
            [sys.executable, str(copied_path), "--clock-mutation-probe"],
            cwd=temporary_directory,
            env=environment,
            text=True,
            capture_output=True,
            check=False,
        )
    combined = process.stdout + process.stderr
    require(process.returncode != 0, "literal-feature clock mutation must exit nonzero")
    require("FAIL clock-register partial trace" in combined, "clock mutation must reach transpose failure")
    print("PASS clock red mutation | copied conjugated->literal history is rejected with nonzero exit")


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--self-test", action="store_true", help="run all checks and copied red mutation")
    mode.add_argument("--mutation-probe", action="store_true", help=argparse.SUPPRESS)
    mode.add_argument("--clock-mutation-probe", action="store_true", help=argparse.SUPPRESS)
    return parser.parse_args()


def main() -> int:
    arguments = parse_arguments()
    try:
        if arguments.mutation_probe:
            run_cases(only_ccm=True)
        elif arguments.clock_mutation_probe:
            run_cases(only_clock=True)
        else:
            run_cases()
            run_red_mutation()
            run_clock_red_mutation()
            print(f"ALL CHECKS PASS ({N_CHECKS} atomic conditions, 2 red mutations)")
    except CheckFailure as error:
        print(f"FAIL {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
