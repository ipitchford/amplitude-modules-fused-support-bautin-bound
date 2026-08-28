# Exact weighted period-order theorem and certificate

**Date:** 27 August 2026  
**Status:** complete candidate proof using the reconstructed amplitude-support
theorem; two exact software implementations agree on the retained benchmark  
**Claim ceiling:** theorem candidate and computational reconstruction; not an
independent review, novelty determination, or publication-readiness decision

## 1. Statement

Let \(P,A\in\mathbf C[x]\), with \(d=\deg P\ge2\), and choose
\(G\in\mathbf C[x]\) with \(G'=A\).  For a flat rapid-decay cycle
\(\Gamma\), define

\[
I_{\Gamma,A}(s)=\int_\Gamma A(x)e^{sP(x)}\,dx.            \tag{1}
\]

Let

\[
\mathcal H_P=
\frac{\mathbf C(s)[x]\,dx}
     {(d/dx+sP'(x))\mathbf C(s)[x]\,dx}                  \tag{2}
\]

be the one-variable twisted de Rham quotient, and put

\[
v_j=[P^jA\,dx]\in\mathcal H_P,\qquad j\ge0.              \tag{3}
\]

Let \(q\) be the least index for which \(v_0,\ldots,v_q\) are linearly
dependent over \(\mathbf C(s)\).  Equivalently,

\[
q=\dim_{\mathbf C(s)}
  \operatorname{span}\{v_0,v_1,v_2,\ldots\}.             \tag{4}
\]

The reconstructed polynomial-amplitude theorem applies.  Hien's perfect
period-pairing theorem applies to the rank-one exponential connection on
\(\mathbf A^1\), pairing its algebraic twisted de Rham cohomology with the
rapid-decay homology of the dual connection.  Then

\[
\boxed{
q=|\Sigma(P;G)|
 =\dim\operatorname{span}\{\text{reduced }G\text{-values on a generic
 fibre of }P\}.
}                                                         \tag{5}
\]

If \(q>0\), the first dependence can be written uniquely after normalizing
its last coefficient to one:

\[
v_q+\sum_{j=0}^{q-1}c_j(s)v_j=0,
\qquad c_j(s)\in\mathbf C(s).                            \tag{6}
\]

It produces the scalar operator

\[
L_A=D_s^q+\sum_{j=0}^{q-1}c_j(s)D_s^j                  \tag{7}
\]

and

\[
L_A I_{\Gamma,A}=0                                      \tag{8}
\]

for every flat rapid-decay cycle.  After clearing denominators and content,
(7) has primitive polynomial coefficients; for
\(P,A\in\mathbf Q[x]\), they may be chosen canonically in
\(\mathbf Z[s]\), with positive leading coefficient in the highest
derivative term.

The order \(q\) is the minimal order of an operator annihilating the complete
period system.  It need not be minimal for an arbitrary specified cycle,
which may annihilate active channels.  No generic-individual-period
minimality claim is made here.

If \(q=0\), then \([A\,dx]=0\), every period (1) vanishes, and the correct
certificate is the equation \(I_{\Gamma,A}=0\).

## 2. Exact reduction and termination

Write

\[
P'(x)=p\,x^{d-1}+L(x),\qquad \deg L<d-1,\quad p\ne0.
\]

Integration by parts in (2), applied to \(x^k\), gives

\[
0=[k x^{k-1}+sP'(x)x^k]\,dx.
\]

Therefore

\[
[x^{k+d-1}dx]
=-\frac{k}{s\,p}[x^{k-1}dx]
 -\frac1p[x^kL(x)dx].                                   \tag{9}
\]

Every term on the right has degree strictly below \(k+d-1\).  Repeated use
of (9) terminates and gives a unique representative in

\[
\operatorname{span}_{\mathbf C(s)}
\{dx,x\,dx,\ldots,x^{d-2}dx\}.                           \tag{10}
\]

These representatives are independent: if \(f\ne0\), the leading term of
\((d/dx+sP')f\) has degree \(\deg f+d-1\), so no nonzero twisted-exact
polynomial can have degree below \(d-1\).  Thus
\(\dim\mathcal H_P=d-1\), and the \(d\) columns
\(v_0,\ldots,v_{d-1}\) necessarily contain a dependence.  Exact rational
linear algebra finds the first one and verifies it by substitution into all
\(d-1\) coordinates.

## 3. Why the dependence is a period operator

Flatness of \(\Gamma\) and rapid decay justify differentiation under the
integral:

\[
\frac{d^j}{ds^j}I_{\Gamma,A}(s)
=\int_\Gamma P(x)^jA(x)e^{sP(x)}\,dx.                   \tag{11}
\]

Pairing (6) with \(\Gamma\) and using (11) gives (8).  Integration-by-parts
relations have no boundary contribution on a rapid-decay cycle, so the
quotient calculation is an exact annihilation proof rather than a formal
analogy.

No lower-order operator can annihilate every period in the complete system.
Indeed, Hien's Theorem 5.2 in *Periods for flat algebraic connections*
(Invent. Math. 178 (2009), 1--22; arXiv:0803.3463) gives a perfect pairing
between algebraic de Rham cohomology and rapid-decay homology of the dual
connection.  Apply it after specializing the rational coefficient functions
at a generic nonsingular value of \(s\).  An operator of order \(r<q\)
annihilating every period would pair the nonzero class
\(\sum_{j=0}^r c_j(s)v_j\) to zero against every rapid-decay class, contrary
to perfectness and the independence of \(v_0,\ldots,v_r\).

A particular cycle can nevertheless kill part of the cyclic subsystem and
satisfy a lower-order equation.  Establishing a generic-individual-period
minimality statement would require an additional differential-module
argument and is deliberately outside this theorem.

Finally, the reconstructed support theorem identifies (4) with the inverse-support and
reduced-root-span quantities in (5).  This is the step that turns a
twisted-quotient computation into the promised support-predicted order
oracle.

## 4. Standard-ray cycle-specific bounds

The false exact channel-count formula is replaced by the following weaker
statement.  The
ray-cycle and Fourier--Gamma argument in THEOREM_H_SUPPORT_RANK.md supplies
the analytic channel-contact input for the standard cycles used here.

Choose the standard ray-cycle basis at infinity and let \(n\in\mathbf C^d\)
have zero trace.  On a common sector the corresponding period has the
monodromy-channel decomposition

\[
I_n(s)=\sum_{r\in\Sigma(P;G)}\widehat n(r)\Lambda_r(s),                 \tag{12}
\]

where every nonzero \(\Lambda_r\) has formal-monodromy eigenvalue
\(\exp(-2\pi i r/d)\).  Put

\[
R=\operatorname{supp}(\widehat n)\cap\Sigma(P;G),
\]

and let \(B_1,\ldots,B_t\) be the monodromy blocks from the block-amplitude
theorem that meet \(R\).  If \(R\ne\varnothing\), then the minimal scalar
operator for this specified period satisfies

\[
\boxed{
|R|\ \le\ \operatorname{ord}_{\min}(I_n)
\le\ \sum_{i=1}^t|B_i|\ \le\ q(P,G'\,dx).
}                                                                    \tag{13}
\]

For the lower bound, the formal solution space of any rational-coefficient
operator annihilating \(I_n\) is stable under formal monodromy.  The distinct
eigenvalues in (12) permit Lagrange projection onto every touched
\(\Lambda_r\).  Those projected solutions are linearly independent, so the
operator order is at least \(|R|\).

For the upper bound, decompose \(G\) by the central projectors of the
monodromy-block theorem.  Only components whose blocks meet \(R\) contribute
to (12).  The complete-system operator for the component in \(B_i\) has order
\(|B_i|\), by (5); a least common left multiple of these component operators
annihilates \(I_n\) and has order at most their summed orders.

Consequently equality holds throughout the first two terms of (13) whenever
every touched block is touched in all of its channels.  Equality with the
block-mass upper bound also holds when the touched block differential modules
are irreducible and pairwise nonisomorphic; their disjoint formal-monodromy
spectra ensure the latter condition.

Equation (13) is the corrected part incorporated from the repaired note.  Its
standard-ray analytic input is now proved in the reconstructed support
theorem; arbitrary contour systems remain outside the statement.  No
unrestricted individual-cycle equality or general Dickson block-mass equality
is claimed.  Establishing the latter would require an explicit derivation of
the scalar connection for every Dickson pair.

## 5. Exact certificate algorithm over \(\mathbf Q\)

For trusted \(P,A\in\mathbf Q[x]\):

1. form \(A,P A,\ldots,P^{d-1}A\);
2. reduce each column with (9) in the basis (10);
3. find the first exact dependent prefix;
4. normalize its final coefficient to one;
5. clear rational-function denominators;
6. divide the common polynomial factor and integer content;
7. orient the sign by the leading coefficient of the highest derivative;
8. substitute the resulting \(\mathbf Z[s]\) coefficients into the full
   exact Krylov matrix and require a zero residual;
9. reconstruct \(C(x,s)\in\mathbf Q(s)[x]\) and verify the polynomial
   identity
   \[
   \sum_j c_j(s)P(x)^jA(x)
   =\partial_xC(x,s)+sP'(x)C(x,s);
   \]
10. bind inputs, matrix, operator, witness, claim boundary, and replay result by
   SHA-256.

The algorithm is finite, deterministic, and offline.  Its output is an
annihilation certificate for the supplied polynomials.  The theorem, rather
than the hash, supplies the support identity and generic minimality.

## 6. Independent-program cross-check

The retained second implementation,
standalone_weighted_order_oracle.py, imports no Atlas source or private
helper.  It reconstructs (9) directly and finds the dependence from a
nullspace, whereas the producer uses the Atlas reducer and a deterministic
pivot solve.  The standalone certificate additionally retains the exact
total-derivative witness in Step 9, so annihilation can be checked by a direct
polynomial identity independently of the quotient implementation.

Across the seven retained cases, the two programs agree on every primitive
\(\mathbf Z[s]\) coefficient, not merely the order.  The cases include
orders \(0,1,2,3,4\), affine transport, a Dickson phase, and the exceptional
Ritt collision.  For example:

\[
\begin{array}{c|c|c}
(P,A) & q & \text{primitive coefficients, low to high}\\ \hline
(x^7,1) & 1 & (1,7s)\\
((x^4+x)^3,4x^3+1) & 1 & (1,3s)\\
(x^5-5x^3+5x,1) & 2 &
(-100s^2-1,\ 25s,\ 25s^2).
\end{array}
\]

The second verifier also rejects a semantically changed operator after its
outer JSON digest is recomputed.  This is independent-program reconstruction,
not independent human or institutional reproduction.

## 7. Assurance and prior-art boundary

The result is an amplitude-weighted support-to-certificate bridge specialized
to one-variable polynomial exponential periods.  General creative
telescoping, minimal telescopers, order bounds, and order-degree trade-offs
are established prior art; this theorem does not claim to invent them.

The complete-system minimality step uses Hien's published perfect-pairing
theorem.  The standard-ray channel input is supplied by the reconstructed
formal-moment and Fourier--Gamma argument; no Borel-summability assertion is
load-bearing.  Because the reconstruction followed the Atlas proof
architecture, it is not independent validation.  Novelty relative to the
exact weighted formulation, specialist correctness review, arbitrary-contour
analysis, and publication readiness remain separate gates.
