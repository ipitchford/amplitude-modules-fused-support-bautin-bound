# Reconstructed polynomial-amplitude support theorem

**Date:** 27 August 2026  
**Status:** self-contained candidate proof reconstructed from the Atlas proof
architecture, with a corrected Wronskian expansion  
**Claim ceiling:** internally checked theorem candidate; not an independent
reproduction, specialist review, peer review, or novelty determination

## 1. Statement

Let (P,A\in\mathbf C[x]), with (d=\deg P\ge2), and choose a polynomial
primitive (G) with (G'=A).  Put (K=\mathbf C(s)) and

\[
\mathcal H_P=
K[x],dx/(\partial_x+sP')K[x],dx,
\qquad
\nabla_s[f,dx]=[(\partial_sf+Pf),dx].                 \tag{1}
\]

Let (q(P,A,dx)) be the (K)-dimension of the cyclic submodule generated
by ([A,dx]).  After affine normalization, let

\[
P(\xi(t))=t^d,
\qquad
\xi(t)=t+O(t^{-1}),                                    \tag{2}
\]

and write

\[
G(\xi(t))=\sum_{m\le M}c_mt^m.
\]

Define the non-trace primitive support

\[
\Sigma(P;G)=
\{r\in\{1,\ldots,d-1\}:c_m\ne0
\text{ for some }m\equiv r\pmod d\}.                 \tag{3}
\]

Then

\[
\boxed{
q(P,A,dx)=|\Sigma(P;G)|
=\dim_{\mathbf C}\operatorname{span}^{\mathrm{red}}
\{G(x_0),\ldots,G(x_{d-1})\},
}                                                       \tag{4}
\]

where (x_j=\xi(\zeta_d^jt)) are the inverse roots near infinity.  The
second equality uses the constant span in the local splitting field and
removes the common trace line.  Lemma 5.1 below proves that, outside the
finite algebraic excluded set of regular values constructed there, this
dimension is also the dimension of the full monodromy orbit of the specialized
reduced root-value vector.

For the standard consecutive ray-cycles at infinity, the Fourier mode of a
cycle indexed by (r) pairs nontrivially with the amplitude cyclic module
exactly when (r\in\Sigma(P;G)).  This supplies the channel input needed for
the supporting cycle-order bounds without assuming a separate
Borel-summability statement.

## 2. Twisted quotient and affine normalization

The leading coefficient of (sP') is a unit in (K).  Cancelling leading
monomials gives a unique representative of degree below (d-1), hence

\[
\mathcal H_P\cong K^{d-1}
\]

with basis ([dx],\ldots,[x^{d-2}dx]).  The connection in (1) is well
defined because

\[
[\partial_s+P,\partial_x+sP']=0.
\]

An affine source change transports both the phase and the one-form.  A target
translation acts triangularly on powers of (P), and a target scaling is
absorbed by rescaling (s).  We may therefore take (P) monic and centred.
The formal implicit-function recursion then gives the unique inverse (2).

## 3. The formal moment transform

Put (K_0=\mathbf C((s))).  For (1\le r\le d-1), let
(\mathcal K_r=K_0e_r) with connection

\[
\partial_se_r=-\frac rd s^{-1}e_r.                    \tag{5}
\]

Define nonzero constants (\mu_{r,n}), for every (n\in\mathbf Z), by

\[
\mu_{r,0}=1,
\qquad
\mu_{r,n+1}=-\frac{r+nd}{d}\mu_{r,n}.                 \tag{6}
\]

The recurrence is read forward from \(n=0\) for positive indices and backward
for negative indices; equivalently,

\[
\mu_{r,n-1}=-\frac d{r+(n-1)d}\mu_{r,n}.
\]

No factor vanishes because (r\not\equiv0\pmod d).  On the bounded-above
Laurent one-forms in residue class (r-1), set

\[
\mathfrak M_r
\left(t^{r+nd-1}dt\right)
=\mu_{r,n}s^{-n}e_r.                                   \tag{7}
\]

This is well defined: a bounded-above (t)-series maps to an (s)-Laurent
series with a lower-bounded valuation.  After allowing coefficients in
(K_0), every coefficient of a fixed power of (s) receives only finitely
many contributions.  Thus no uncontrolled double Laurent series is used.

For (h=t^{r+nd}), equations (6)--(7) give

\[
\mathfrak M_r
\bigl((\partial_th+sd t^{d-1}h)dt\bigr)=0.             \tag{8}
\]

The identity holds termwise for every bounded-above Laurent series.  Pulling
back by (x=\xi(t)) gives

\[
(\partial_xq+sP'q)dx
\longmapsto
(\partial_t(q(\xi))+sd t^{d-1}q(\xi))dt,
\]

so the direct sum of the maps (7) descends to

\[
\mathfrak M:
\mathcal H_P\otimes_KK_0
\longrightarrow
\bigoplus_{r=1}^{d-1}\mathcal K_r.                    \tag{9}
\]

It is compatible with the (s)-connections.  Indeed,

\[
\partial_s(\mu_{r,n}s^{-n}e_r)
=-\left(n+\frac rd\right)\mu_{r,n}s^{-n-1}e_r
=\mu_{r,n+1}s^{-n-1}e_r,                              \tag{10}
\]

which is the moment of multiplication by (t^d=P(\xi)).

Finally, for (0\le j\le d-2),

\[
\xi(t)^j\xi'(t)=t^j+O(t^{j-2}).                       \tag{11}
\]

In the bases (dx,\ldots,x^{d-2}dx) and (e_1,\ldots,e_{d-1}), the
matrix of (9) lies in (\operatorname{Mat}_{d-1}(\mathbf C[[s]])).  Its
constant term is triangular with diagonal one: the diagonal entry comes from
(t^jdt), lower (t)-powers lie weakly above the diagonal, and no negative
power of (s) can occur because (j+1<d).  The determinant is a unit, so
(9) is an isomorphism of differential modules.

## 4. Active channels and the corrected Wronskian

Because (A(\xi)\xi'dt=d(G(\xi))), the (r)-component of the seed is

\[
v_r=
\sum_n(r+nd)c_{r+nd}\mu_{r,n}s^{-n}e_r.                \tag{12}
\]

Distinct coefficients occupy distinct powers of (s), and neither
(r+nd) nor (\mu_{r,n}) vanishes.  Hence

\[
v_r\ne0\quad\Longleftrightarrow\quad r\in\Sigma(P;G). \tag{13}
\]

Let (S) be the active set.  For each (r\in S), choose the largest
(n_r) occurring in (12), write its coefficient as (c_r\ne0), and put

\[
\alpha_r=-n_r-\frac rd.
\]

For (j\ge0), the correct leading expansion is

\[
\partial_s^jv_r
=c_rs^{-n_r-j}
\bigl((\alpha_r)_{\underline j}+O(s)\bigr)e_r.         \tag{14}
\]

Because \(1\le r\le d-1\), the number
\(\alpha_r=-n_r-r/d\) is not an integer.  Thus every individual falling
factorial in (14) is nonzero.  More importantly, the leading determinant must
be evaluated as the whole polynomial matrix rather than by an unsupported
entrywise factorization.  After factoring the row and column powers from the
first \((|S|)\) derivative columns, its leading coefficient is

\[
\left(\prod_{r\in S}c_r\right)
\det\bigl((\alpha_r)_{\underline j}\bigr)
=\left(\prod_{r\in S}c_r\right)
\prod_{r<r'}(\alpha_{r'}-\alpha_r).                   \tag{15}
\]

The (\alpha_r) are distinct: equality would imply
(r+n_rd=r'+n_{r'}d), impossible for different residues.  Thus (15) is
nonzero.  The direct sum of the active Kummer lines is an
\((|S|)\)-dimensional differential submodule containing the seed, so it is an
upper bound for the cyclic rank.  In the first \((|S|)\) derivative columns,
factor \(c_rs^{-n_r}\) from row \(r\) and \(s^{-j}\) from column \(j\);
equation (15) gives \((|S|)\) independent columns and the matching lower
bound.  A finite matrix over \(K\) has the same rank after the faithful
extension \(K\subset K_0\), so completion does not change the original cyclic
rank.  Therefore

\[
q(P,A,dx)=|S|=|\Sigma(P;G)|.                           \tag{16}
\]

## 5. Reduced root-value span

Label the inverse roots near infinity by
\(x_j(t)=\xi(\zeta_d^jt)\), \(0\le j<d\).  Fourier projection gives

\[
Y_r(t)=\frac1d\sum_{j=0}^{d-1}
\zeta_d^{-jr}G(x_j(t))
=\sum_{m\equiv r\ (d)}c_mt^m.                         \tag{17}
\]

**Lemma 5.1 (equivariant span and generic specialization).**  Let
\(\mathcal L\) be a splitting field of \(P(X)-y\) over \(\mathbf C(y)\), let
\(\Gamma\) be its geometric monodromy group, and set

\[
\bar g_j=G(x_j)-\frac1d\sum_{i=0}^{d-1}G(x_i),\qquad
W_G=\operatorname{span}_{\mathbf C}\{\bar g_0,\ldots,\bar g_{d-1}\}
\subset\mathcal L.
\]

Then

\[
\dim_{\mathbf C}W_G=|\Sigma(P;G)|.                    \tag{18}
\]

There is also a finite algebraic set
\(Z_G\subset\mathbf A^1_y\), containing every critical value of \(P\), such
that for \(y_0\notin Z_G\), and for any simultaneous determination of the
inverse roots at \(y_0\), the full \(\Gamma\)-orbit of

\[
\bigl(\bar g_0(y_0),\ldots,\bar g_{d-1}(y_0)\bigr)       \tag{19}
\]

has complex span of dimension \(\dim W_G\).

**Proof.**  Put

\[
E=\{(a_0,\ldots,a_{d-1})\in\mathbf C^d:\sum_ja_j=0\}
\]

and define

\[
\Phi_G:E\longrightarrow\mathcal L,qquad
(a_j)\longmapsto\sum_ja_jG(x_j).
\]

This map is \(\Gamma\)-equivariant and has image \(W_G\).  The non-trace
Fourier vectors form a basis of \(E\), and their images under \(\Phi_G\) are
the functions \(dY_r\), \(1\le r<d\).  The nonzero \(Y_r\) are linearly
independent over \(\mathbf C\) because their Laurent supports occupy disjoint
residue classes.  Hence
\(\operatorname{rank}\Phi_G=|\Sigma(P;G)|\), which proves (18).

The inertia element at infinity is a \(d\)-cycle and has simple spectrum on
\(\mathbf C^d\).  Thus the \(\Gamma\)-permutation module is
multiplicity-free: two copies of one irreducible constituent would contribute
the same nonempty set of inertia characters twice, contradicting simple
spectrum.  The quotient \(W_G\) is also multiplicity-free.  Write it as
\(W_G=\bigoplus_\nu W_\nu\) with the \(W_\nu\) pairwise nonisomorphic and
irreducible.  Choose a nonzero algebraic function
\(h_\nu\in W_\nu\) for each nonzero summand.  Starting from the critical
values of \(P\), add the projections to the \(y\)-line of the finitely many
zeros and poles of all \(h_\nu\) on the compactified finite cover.  This gives
the finite set \(Z_G\).

For \(y_0\notin Z_G\), evaluation on a simultaneous determination defines
\(\lambda_{y_0}\in W_G^*\), and its restriction to each \(W_\nu\) is nonzero.
Central idempotents isolate these nonzero irreducible components; each then
generates its entire dual summand.  Hence the \(\Gamma\)-orbit of
\(\lambda_{y_0}\) spans all of \(W_G^*\).  The dual map

\[
\Phi_G^*:W_G^*\hookrightarrow E^*
\]

is injective and \(\Gamma\)-equivariant.  Under the standard invariant
identification \(E^*\simeq E\), its value at \(\lambda_{y_0}\) is the vector
in (19): for every \((a_j)\in E\), its pairing is
\(\sum_ja_jG(x_j(y_0))=\sum_ja_j\bar g_j(y_0)\).  Therefore the full
monodromy-orbit span of (19) has dimension \(\dim W_G\).  Changing the
simultaneous determination only applies an element of \(\Gamma\), so the
dimension is unchanged. \(\square\)

Lemma 5.1 and (16) prove (4), including its full generic-specialization
interpretation.  In particular, this equality is available before any use of
central projectors or any family-specific Dickson or exceptional-Ritt
classification.

## 6. Standard ray-cycles and channel contact

**Lemma 6.1 (standard-ray flat family and Fourier pairing).**  Fix a simply
connected sector

\[
\mathfrak S=\{s\ne0:|\arg s-\theta_0|<\varepsilon\},
\qquad0<\varepsilon<\pi/2,
\]

and continuous branches of \(\arg s\) and \(s^{1/d}\) on it.  If
\(s=|s|e^{i\theta}\), define

\[
\phi_k(s)=\frac{\pi-\theta+2\pi k}{d},\qquad
\ell_k(s)=e^{i\phi_k(s)}[0,\infty).
\]

Orient \(\Gamma_k(s)\) from infinity to the origin on \(\ell_k(s)\), then
from the origin to infinity on \(\ell_{k+1}(s)\).  These contours form a flat
family of rapid-decay classes on \(\mathfrak S\), and

\[
\sum_k[\Gamma_k]=0,
\qquad
[\Gamma_0],\ldots,[\Gamma_{d-2}]
\text{ form a basis}.                                  \tag{20}
\]

For \(0\le j,k\le d-2\), with \(r=j+1\), one has uniformly as \(s\to0\)
inside every compact subsector

\[
s^{r/d}\int_{\Gamma_k}x^je^{sP(x)}dx
\longrightarrow
\frac{\Gamma(r/d)}d e^{\pi ir/d}
(\zeta_d^r-1)\zeta_d^{kr}.                             \tag{21}
\]

This leading matrix has full rank.  Under the formal-moment isomorphism (9),
its Fourier diagonalization gives a nondegenerate pairing of the \(r\)-th
Kummer line with the dual ray-cycle Fourier mode.

**Proof.**  Along \(\ell_k(s)\), one has
\(sx^d=-|s||x|^d\).  The two ends of \(\Gamma_k(s)\) therefore remain in
consecutive rapid-decay sectors and vary continuously with \(s\).  Contour
deformation within those sectors gives a locally constant, hence flat,
relative class.  For a sufficiently large disk, the rapid-decay relative
homology retracts to the reduced zero-dimensional homology of the \(d\)
marked decay intervals on its boundary.  The boundary of \(\Gamma_k\) is
\(e_{k+1}-e_k\), so (20) is its only relation and any consecutive \(d-1\)
classes form a basis.

After scaling \(u=s^{1/d}x\), the moving rays become the fixed rays
\(\arg u=(\pi+2\pi k)/d\), and the monic centred phase satisfies

\[
sP(s^{-1/d}u)
=u^d+\sum_{\ell=0}^{d-2}p_\ell s^{1-\ell/d}u^\ell.
\]

On a compact subsector, Young's inequality gives constants \(c,C>0\),
independent of sufficiently small \(s\), for which the real part of the right
side is at most \(-c|u|^d+C\) on every scaled ray.  Hence
\(C(1+|u|)^j e^{-c|u|^d}\) is an integrable majorant.  It justifies dominated
convergence and, with the same estimate after multiplying by any polynomial,
differentiation of polynomial-amplitude periods under the integral.  The
limit is the incoming integral on the \(k\)-th monomial ray plus the outgoing
integral on the next.  Direct Gamma integration with these orientations gives
(21).

For \(0\le k\le d-2\) and \(1\le r\le d-1\), the matrix in (21) is a
nonzero diagonal matrix times
\((\zeta_d^{kr})\).  Its determinant is the Vandermonde determinant on the
distinct nodes \(\zeta_d,\ldots,\zeta_d^{d-1}\), so it is nonzero.
Continuation once around \(s=0\) changes \(\phi_k\) to \(\phi_{k-1}\) and
therefore sends \([\Gamma_k]\) to \([\Gamma_{k-1}]\).  The ray Fourier modes
have the same distinct characters as the Kummer lines in (9); the nonzero
Fourier-diagonal leading matrix identifies the dual characters and proves the
claimed nondegenerate pairing. \(\square\)

If \(\Gamma(n)=\sum_kn_k\Gamma_k\) and
\(\widehat n(r)=\sum_kn_k\zeta_d^{kr}\), Lemma 6.1 and the isomorphism (9)
show that its period has a nonzero \(r\)-monodromy projection exactly when

\[
r\in\Sigma(P;G)
\quad\text{and}\quad
\widehat n(r)\ne0,                                     \tag{22}
\]

up to the global replacement \(r\leftrightarrow-r\) from the opposite Fourier
convention.  This is the channel-contact statement used in the supporting
weighted-order bridge.  It asserts neither Borel summability nor a result for
arbitrary contour systems.

## 7. Assurance boundary

This document removes Hypothesis H as an imported premise of Results A--C by
including the load-bearing proof in the same review target.  It does not
constitute independent reproduction: the proof was reconstructed after
inspection of the Atlas, by the same research system that prepared the
downstream results.  The corrected Wronskian notation, completion check and
ray-cycle specialization have received only internal adversarial review.

The finite support/rank reconstruction is a falsification control, not a
formal proof.  Historical priority, independent specialist verification,
peer review and authorization to publish remain open.
