# The Dickson amplitude-module theorem

**Date:** 27 August 2026  
**Status:** complete candidate proof using the reconstructed
amplitude-support theorem  
**Claim ceiling:** theorem candidate; not independently reviewed, not a novelty
or publication-readiness determination

## 1. Statement

Let \(a\in\mathbf C^\times\), let \(d\ge 2\), and write

\[
P(x)=D_d(x,a),
\qquad
D_j(u+a/u,a)=u^j+a^j u^{-j}.
\]

For a polynomial primitive \(G\in\mathbf C[x]\), write its unique expansion

\[
G=H_0(P)+
\sum_{1\le j<d/2}
\bigl(H_j(P)D_j+K_j(P)D_{d-j}\bigr)
+\mathbf 1_{2\mid d}H_{d/2}(P)D_{d/2},                 \tag{1}
\]

where every displayed coefficient is in \(\mathbf C[y]\), evaluated at
\(y=P(x)\).  Let

\[
N(G)=\#\{j:1\le j<d/2,\ (H_j,K_j)\ne(0,0)\}
\]

and, when \(d\) is even, let
\(\varepsilon(G)=1\) if \(H_{d/2}\ne0\), and \(0\) otherwise.  Put
\(\varepsilon(G)=0\) when \(d\) is odd.

The reconstructed polynomial-amplitude theorem proves that for \(A=G'\),
the cyclic rank \(q(P,A\,dx)\) equals the number of
nonzero non-trace residue channels of the normalized inverse series
\(G(\xi(t))\), where \(P(\xi(t))=t^d\).  Then

\[
\boxed{q(D_d,G'\,dx)=2N(G)+\varepsilon(G).}              \tag{2}
\]

Equivalently, the paired summand indexed by \(j<d/2\) has support exactly
\(\{j,d-j\}\pmod d\) whenever it is nonzero, the midpoint summand has
support \(\{d/2\}\), and \(H_0(P)\) has no reduced support.

## 2. The module decomposition

The Dickson polynomial \(D_j(x,a)\) is monic of degree \(j\).  Consequently

\[
1,D_1(x,a),\ldots,D_{d-1}(x,a)                           \tag{3}
\]

is a triangular change of basis from \(1,x,\ldots,x^{d-1}\).  Because
\(P=D_d(x,a)\) is monic of degree \(d\), the latter list is a basis of the
free \(\mathbf C[P]\)-module \(\mathbf C[x]\).  Thus (3) is also a
\(\mathbf C[P]\)-basis.  Pairing \(D_j\) with \(D_{d-j}\), and retaining
\(D_{d/2}\) once when \(d\) is even, proves existence and uniqueness of
(1).

## 3. The quadratic obstruction

Work in the Laurent-series field at infinity.  Choose the solution \(w\) of

\[
w+\frac{a^d}{w}=t^d                                      \tag{4}
\]

with \(w/t^d\to1\), and choose \(u\) with \(u^d=w\) and \(u/t\to1\).
Then

\[
\xi(t)=u+\frac au,
\qquad
D_d(\xi(t),a)=t^d.                                       \tag{5}
\]

Moreover \(w\in t^d\mathbf C[[t^{-d}]]\) and
\(u\in t\mathbf C[[t^{-d}]]\), with the more precise expansions involving
only even multiples of \(d\).  Hence multiplication by a rational function
of \(t^d\) does not change a residue class modulo \(d\).

The element \(w\) does not belong to \(\mathbf C(t^d)\).  Indeed, with
\(Y=t^d\), equation (4) is

\[
w^2-Yw+a^d=0.                                            \tag{6}
\]

Its discriminant \(Y^2-4a^d\) has two distinct simple zeros because
\(a\ne0\).  A square in \(\mathbf C(Y)\) has even valuation at every point,
so this discriminant is not a square in \(\mathbf C(Y)\).  The quadratic
(6) is therefore irreducible over \(\mathbf C(Y)\).

## 4. No channel can disappear inside a Dickson pair

Fix \(1\le j<d/2\) and abbreviate \(F=H_j\), \(K=K_j\).  On the inverse
branch (5), the paired summand becomes

\[
\begin{aligned}
F(P)D_j+K(P)D_{d-j}
={}&u^j\left(F(Y)+\frac{a^{d-j}K(Y)}{w}\right)\\
 &+u^{-j}\left(a^jF(Y)+K(Y)w\right).                    \tag{7}
\end{aligned}
\]

The first line of (7) lies wholly in residue \(j\pmod d\), and the second
lies wholly in residue \(-j=d-j\pmod d\).  These residues are distinct
because \(j<d/2\).

Suppose the coefficient of the first residue vanished.  After multiplication
by \(w\), this would give

\[
F(Y)w+a^{d-j}K(Y)=0.                                     \tag{8}
\]

If \(F=0\), equation (8) forces \(K=0\); otherwise it forces
\(w=-a^{d-j}K/F\in\mathbf C(Y)\), contradicting Section 3.  Thus the first
residue is nonzero for every nonzero pair \((F,K)\).  The same argument
applied to

\[
a^jF(Y)+K(Y)w=0                                          \tag{9}
\]

shows that the second residue is also nonzero.  Therefore a nonzero paired
summand has support exactly \(\{j,d-j\}\).

If \(d\) is even, a nonzero midpoint term
\(H_{d/2}(P)D_{d/2}\) is a nonzero Laurent series whose exponents all have
residue \(d/2\); it therefore contributes exactly that one channel.
Finally, \(H_0(P)=H_0(t^d)\) occupies only the trace residue \(0\).

The supports belonging to distinct unordered pairs are disjoint.  Taking
their union proves the support count \(2N(G)+\varepsilon(G)\), and the
reconstructed amplitude-support theorem gives (2).

## 5. Consequences

1. If \(d\) is odd, the possible ranks are
   \(0,2,4,\ldots,d-1\).
2. If \(d\) is even, every rank \(0,1,\ldots,d-1\) occurs.
3. The rank is zero exactly when \(G\in\mathbf C[P]\).
4. The classification is uniform in every nonzero complex parameter \(a\);
   the excluded value \(a=0\) is the power phase and has a different,
   degenerate pairing mechanism.

## 6. Assurance boundary

This file closes the family-specific algebraic proof obligation identified in
the Stage 1 brief and now cites the self-contained reconstruction in
THEOREM_H_SUPPORT_RANK.md.  That reconstruction followed inspection of the
Atlas and is not an independent reproduction.  Neither file establishes
historical novelty, peer review, or authorization to publish.  The existing
57-case exact receipt remains falsification and replay evidence, not the proof
of the all-degree statement.
