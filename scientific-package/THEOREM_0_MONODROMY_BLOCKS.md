# The monodromy-block amplitude theorem

**Date:** 27 August 2026  
**Status:** complete candidate proof using the reconstructed
amplitude/root-span theorem  
**Role:** organizing theorem for the explicit Dickson and exceptional modules  
**Claim ceiling:** theorem candidate; not independently reviewed or certified
novel

## 1. Statement

Let \(P\in\mathbf C[x]\) be monic of degree \(d\ge2\), let
\(\Gamma\le S_d\) be the monodromy group on a generic fibre, and let
\(c\in\Gamma\) be the inertia \(d\)-cycle at infinity.  Write the permutation
module as

\[
\mathbf C^d=U_0\oplus U_1\oplus\cdots\oplus U_k,
\]

where \(U_0\) is the trace line.

The \(c\)-eigenvalues on \(\mathbf C^d\) are all distinct.  Hence the
\(\Gamma\)-module is multiplicity-free, and there is a unique partition

\[
\mathbf Z/d\mathbf Z=B_0\sqcup B_1\sqcup\cdots\sqcup B_k,
\qquad B_0=\{0\},
\]

such that \(U_i\) is spanned by the Fourier characters indexed by \(B_i\).

The reconstructed polynomial-amplitude theorem proves

\[
|\Sigma(P;G)|
=\dim\operatorname{span}_{\mathrm{red}}
  \{G(x_1),\ldots,G(x_d)\}.                             \tag{H}
\]

Then there is a direct decomposition into free \(\mathbf C[P]\)-modules

\[
\boxed{
\mathbf C[x]=\mathcal M_0\oplus\mathcal M_1\oplus\cdots
\oplus\mathcal M_k,
\qquad
\mathcal M_0=\mathbf C[P],
\qquad
\operatorname{rank}_{\mathbf C[P]}\mathcal M_i=|B_i|.
}                                                        \tag{1}
\]

Every nonzero \(G_i\in\mathcal M_i\), \(i>0\), has inverse support exactly
\(B_i\).  Consequently, if

\[
G=G_0+G_1+\cdots+G_k,\qquad G_i\in\mathcal M_i,
\]

then

\[
\boxed{
\Sigma(P;G)=\bigcup_{\substack{i>0\\G_i\ne0}}B_i.
}                                                        \tag{2}
\]

For an arbitrary set
\(S\subset(\mathbf Z/d\mathbf Z)\setminus\{0\}\), put

\[
V_S=\{G\in\mathbf C[x]:\Sigma(P;G)\subset S\}.
\]

If \(S^\circ\) is the union of all blocks \(B_i\subset S\), then

\[
\boxed{
V_S=V_{S^\circ}
=\mathcal M_0\oplus
 \bigoplus_{\substack{i>0\\B_i\subset S}}\mathcal M_i,
\qquad
\operatorname{rank}_{\mathbf C[P]}V_S=1+|S^\circ|.
}                                                        \tag{3}
\]

Thus the attainable supports are exactly the unions of non-trace monodromy
blocks.

## 2. Multiplicity-free character blocks

The restriction of the permutation module to the cyclic group
\(\langle c\rangle\) is its regular representation, so every character of
\(\mathbf Z/d\mathbf Z\) occurs once.

If a \(\Gamma\)-irreducible representation appeared twice, every
\(\langle c\rangle\)-character appearing in its restriction would occur at
least twice in the full permutation module.  This is impossible.  Therefore
the permutation module is multiplicity-free.

Every \(U_i\) is \(c\)-invariant.  Since \(c\) has simple spectrum, \(U_i\)
is the span of a unique subset \(B_i\) of the Fourier eigenvectors.  Directness
of the irreducible decomposition makes the \(B_i\) a partition.  Transitivity
of \(\Gamma\) makes the invariant trace line the unique trivial constituent,
so \(B_0=\{0\}\).

## 3. Central projectors descend to polynomial operators

Let \(e_i\in\mathbf C[\Gamma]\) be the central idempotent projecting onto
\(U_i\).  For \(G\in\mathbf C[x]\), form its generic root-value vector

\[
v_G(y)=\bigl(G(x_1(y)),\ldots,G(x_d(y))\bigr)
\]

in a splitting field of \(P(x)-y\).

The first coordinate of \(e_iv_G\) is fixed by the stabilizer
\(\Gamma_0\) of \(x_1\).  Indeed, \(e_i\) is central, and an element of
\(\Gamma_0\) fixes the first coordinate after permuting the vector.
By Galois correspondence this coordinate belongs to
\(\mathbf C(x_1)\).

Every \(x_j\) is integral over \(\mathbf C[y]\), hence so is every
\(G(x_j)\) and every constant linear combination of these values.  The first
coordinate is both integral over \(\mathbf C[y]\) and contained in
\(\mathbf C(x_1)\).  The integral closure of \(\mathbf C[y]\) in
\(\mathbf C(x_1)\), where \(y=P(x_1)\), is \(\mathbf C[x_1]\).  The coordinate
is therefore a polynomial; denote it by \(T_iG\).

This constructs a \(\mathbf C[P]\)-linear idempotent

\[
T_i:\mathbf C[x]\longrightarrow\mathbf C[x]
\]

whose conjugate-value vector is \(e_iv_G\).  The central idempotent relations
give

\[
T_iT_j=\delta_{ij}T_i,\qquad \sum_iT_i=1.
\]

Put \(\mathcal M_i=\operatorname{im}T_i\).  Equation (1) is direct.
Each image is a projective direct summand of the free
\(\mathbf C[P]\)-module \(\mathbf C[x]\), hence is free because
\(\mathbf C[P]\) is a PID.

After extending scalars from \(\mathbf C(P)\) to the splitting field, the
generic evaluation map identifies
\(\mathbf C(x)\otimes_{\mathbf C(P)}\Omega\) with \(\Omega^d\).
The image of \(T_i\) becomes \(U_i\otimes\Omega\), so
\(\mathcal M_i\) has \(\mathbf C[P]\)-rank \(\dim U_i=|B_i|\).
The trace projector sends \(G\) to its normalized field trace, which is a
polynomial in \(P\); hence \(\mathcal M_0=\mathbf C[P]\).

## 4. Support of a block module

Take nonzero \(G_i\in\mathcal M_i\), \(i>0\).  Its root-value vector lies
in the irreducible module \(U_i\), and its monodromy orbit spans all of
\(U_i\).  Therefore its reduced root-span dimension is \(|B_i|\).

Because \(U_i\) is spanned by the \(c\)-characters in \(B_i\), the inverse
support of \(G_i\) is contained in \(B_i\).  The support/root-span theorem
says that the
support cardinality is \(|B_i|\), so containment is equality:

\[
\Sigma(P;G_i)=B_i.
\]

For a sum of block components, the blocks are disjoint, so their inverse
series cannot cancel across components.  This proves (2).

Equation (3) follows immediately: a component with block not contained in
\(S\) must vanish, while every component whose block lies in \(S\) is
admitted.  The rank is the sum of the block dimensions plus the trace rank.

## 5. Consequences for the explicit results

1. For \(P=D_d(x,a)\), the non-trace blocks are the pairs
   \(\{j,d-j\}\), with the midpoint singleton when \(d\) is even.  Theorem A
   identifies explicit Dickson generators for these abstract modules.
2. For \(P=(x^4+x)^3\), the blocks are
   \[
   \{4\},\ \{8\},\ \{1,7,10\},\ \{2,5,11\},\ \{3,6,9\}.
   \]
   Theorem B supplies the explicit triangular generators and correction
   coefficients.
3. If the monodromy action is two-transitive, the only blocks are
   \(\{0\}\) and \(\{1,\ldots,d-1\}\).  Therefore every
   \(G\notin\mathbf C[P]\) has full support.

The abstract block theorem explains which support unions are possible.  It
does not by itself compute convenient low-degree generators; that is the
additional content of the explicit families.

## 6. Assurance and novelty boundary

The proof uses the self-contained reconstruction in
THEOREM_H_SUPPORT_RANK.md rather than importing the Atlas equality as a bare
hypothesis.  It corrects a proof route in the identified non-public companion
drafts by replacing formal dimension counting with central-projector descent
to polynomials.

Multiplicity-free monodromy representations, Fourier characters and
polynomial moment relation modules have substantial prior art, particularly
Pakovich--Muzychuk.  No claim of priority for the block formulation is made
without a dedicated literature audit.  Neither this document nor the
reconstructed support theorem has received independent specialist review.
