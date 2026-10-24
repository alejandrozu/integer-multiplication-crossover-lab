# Adaptive lockstep height and a shifted-logarithmic majorant

This is a conditional finite compiler theorem. It changes the height of the
integer flow; it does not change the native productive/paid word, award new
productive credit, or assert its physical or analytic premises. A final
numerical witness must satisfy the directed inequalities below; exploratory
decimals alone are not a certificate.

The finite integer/Pascal compiler is Jacob Alan Sussman's construction.
The capped overlapping-rank flow and its chronological interpretation are
my [PR #4436](https://github.com/CrocSwap/integer-mult-bounds/pull/4436). Ryanson Jonathan's corrected [PR #4459](https://github.com/CrocSwap/integer-mult-bounds/pull/4459) supplies the mirror-window
identity and boundary-share method. [PR #4456](https://github.com/CrocSwap/integer-mult-bounds/pull/4456), [PR #4465](https://github.com/CrocSwap/integer-mult-bounds/pull/4465), [PR #4467](https://github.com/CrocSwap/integer-mult-bounds/pull/4467) and [PR #4476](https://github.com/CrocSwap/integer-mult-bounds/pull/4476) provide
independent finite checks and important warnings about the original height:
leaf exits need not be sublinear and their potential cannot be discarded.
The present argument changes that height, bounds root and leaf contributions,
and supplies the complete recurrence majorant. It does not repeat the
invalid assumption that the original flow's leaf ranks are uniformly o(n).
Substantial OpenAI Codex assistance, including separate mathematical agents;
new material is Apache-2.0. Source manifests retain predecessor authorship.

## 1. Arbitrary-height finite flow

Let W_k and P_r be positive integer target and chronological paid-rank
multiplicities of a fixed native unit. Assume

```
2 <= k_min <= k <= m=max(k),       1 <= r <= r_max < m.
```

The native contract, including the order of individual paid positions, is a
premise; two paid positions cannot be combined merely because ranks agree.
Fix an integer ambient rank n>=m and put C_n=floor(n/m). Choose any integer
G>=0. For a target multiindex alpha define

```
c(alpha)=product_k k^alpha_k,
u(alpha)=multinomial(|alpha|;alpha) product_k W_k^alpha_k.
```

For every paid-round path of length d<=G and multiplier rho, instantiate
u(alpha) units for every multiindex of degree G-d with

```
rho*c(alpha) <= C_n.
```

Each such unit has column multiplicity rho*c(alpha). At a paid position of
rank r, child demand at point gamma is the sum of W_k*u(gamma-e_k) over
eligible child units. The complete Pascal sum is u(gamma). Consequently
present parent supply dominates child demand. Match whole integer jobs;
retain excess parent supply as boundary exits, and supply demands with
absent parent points by distinct top input arrays. At depth G all paid
jobs are leaf exits. At the root all target demands are top sources.

This is the same finite Pascal routing argument as [PR #4436](https://github.com/CrocSwap/integer-mult-bounds/pull/4436). It does not
require G=floor(log_(k_min) C_n). In particular a root class may be empty
while later classes receive new top sources. These are finitely many
chronological classes with explicit fresh source endpoints. They do not
copy productive input data or obtain credit from a discarded request.
One may include empty classes in the finite schedule; a class and all its
exits return before the next suspended paid position resumes.

Every source fits n: it is a target of an actual child or root unit of
column z<=n/m, hence has rank kz<=n. Every exit is an actual paid job of
rank rz<=r_max*n/m<n. A nonroot source has an absent parent point with
rho_parent*c(gamma)>C_n, so its integer column is greater than n/m and
its source rank r*rho_parent*c(gamma)>n/m. **Only root sources lose this
lower bound when the height changes.** Root sources remain positive and
at most n; their complement jobs therefore have nonnegative rank below n.

All recursive complement and exit ranks descend strictly. The original
integer batch-clearing construction, for example nested widths divisible
by all earlier widths, produces a finite uniform program. If S_s and E_e
are its source and exit inventories and its source count is positive, the
normalized paid-leaf recurrence is

```
L(n)=[sum_s S_s L(n-s)+sum_e E_e L(e)]/sum_s S_s.             (1)
```

Below a chosen cutoff we may use the elementary L(n)=n construction. No
claims about small ranks need to be supplied by an empty adaptive flow.
The concrete profiles here have paid rank-one calls, which guarantee a
nonempty degree-zero leaf class at every height. More generally, the later
positive occupation bound guarantees nonempty flows in its certified range.

## 2. Exact potentials and the height-independent mirror bound

At a real exponent t in (0,1), put

```
T_t=sum_k W_k*k^t,       P_t=sum_r P_r*r^t.
```

For one finite flow let H_t be the sum of column^t over all unit instances.
Let R_t and I_t be respectively root and nonroot source t-potentials; B_t
and F_t respectively boundary and leaf exit t-potentials. Matched jobs
cancel at their actual ranks, giving the exact identity

```
I_t+R_t = B_t+F_t+(T_t-P_t)H_t.                            (2)
```

Always

```
F_t <= P_t^(G+1).                                         (3)
```

Indeed a capped leaf path is a subset of all paid paths of length G,
followed by one paid letter. Formula (3) is an upper bound; an exact
untruncated leaf law is not assumed.

The mirror identity from corrected [PR #4459](https://github.com/CrocSwap/integer-mult-bounds/pull/4459) remains valid at arbitrary G.
For a paid-prefix path rho of length d<G and target multiindex alpha of
degree G-d-1, write z=rho*c(alpha), with its integer base weight. For a
pair (r,k), boundary exits occur when

```
C_n/r < z <= C_n/k,     r>k,
```

and inner sources occur when

```
C_n/k < z <= C_n/r,     k>r.
```

Both have rank rkz and coefficient P_r W_k. The complete Pascal expansion
accounts for multiplicities, including points with several eligible target
predecessors. These statements use the integer cutoff C_n, not an
inconsistent replacement of floor(n/m) by n/m at a boundary.

Partition the positive z/C_n axis into intervals with endpoints 1/r and
1/k. On each interval J, let E_J(t) and S_J(t) be the sums of
P_r W_k(rk)^t whose respective windows contain J. If

```
E_J(t) <= beta S_J(t)    for every elementary interval J,   (4)
```

then B_t<=beta I_t for every n and every G. Intervals with S_J=0 must
also have E_J=0. This is a pointwise coefficient inequality against a
nonnegative base measure; no asymptotic distributional assumption enters.
A uniform interval certificate for (4) over all exponents used below is
required. A finite observed boundary share is insufficient.

## 3. Mixed layers and two Chernoff inequalities

Choose positive integers a,b, set g=a+b, and choose an integer M>1. At
rank n set

```
ell=floor(log_M C_n),       G=g*ell.
```

These are exact integer definitions. At fixed exponent t abbreviate
T=T_t, P=P_t, q=T/P. Under the t-tilted target law, a rank k has
probability W_k k^t/T; define the analogous paid law. A layer with h
target letters and G-h paid letters has unit potential exactly

```
T^h P^(G-h) Pr(S_h^T+S_(G-h)^P <= ln C_n).                 (5)
```

All increments are nonnegative. Thus a final admitted paid product has
admitted paid prefixes, even when some increments are zero. Equation (5)
therefore describes the actually capped chronological classes, rather than
an enlarged path family introduced only for an estimate.

Choose s>0 and lambda>0 and suppose

```
T_(t+s)/T >= P_(t+s)/P,
u_t=M^(-s)(T_(t+s)/T)^a(P_(t+s)/P)^b <1,
v_t=M^lambda (T_(t-lambda)/P)^g <1.                        (6)
```

For 0<=h<=a*ell, the exponential Markov bound and
ln C_n>=ell ln M imply

```
Pr(S_h^T+S_(G-h)^P >ln C_n)
 <=M^(-s*ell)(T_(t+s)/T)^h(P_(t+s)/P)^(G-h)
 <=u_t^ell.
```

The first guard in (6) is needed for the second inequality: the endpoint
h=a*ell must be the largest of these moment-generating expressions.
If T>P, summing (5) over h=0,...,a*ell gives

```
(T-P)H_t >=(1-u_t^ell)P^(G+1)(q^(a*ell+1)-1).             (7)
```

This geometric sum is essential: replacing it by one layer introduces an
unnecessary inverse moment-gap prefactor.

The root potential is exactly T times the truncated target degree-G
potential. Since C_n<M^(ell+1), lower-tail exponential Markov gives

```
R_t <=T*C_n^lambda*T_(t-lambda)^G
    <=q*M^lambda*v_t^ell*P^(G+1).                          (8)
```

Set A_t=(T-P)H_t-R_t. Combining (7)--(8) yields

```
A_t >=D_ell(t)P^(G+1),
D_ell(t)=(1-u_t^ell)(q^(a*ell+1)-1)-q*M^lambda*v_t^ell.    (9)
```

The useful geometry has ln M/g strictly between the relevant paid and
target tilted log means. Under that choice the two tail bounds can hold
at once, even though paid ranks overlap productive ranks. This is the
structural change from the original minimum-target height.

## 4. Sharp use of the exact cancellation

Suppose B_t<=beta I_t and beta<eta<1. If

```
(eta-beta)D_ell(t) >=1-eta,                               (10)
```

then

```
B_t+F_t <=eta I_t.                                       (11)
```

To prove this, (9), (3), and (10) imply A_t>=0 and
(eta-beta)A_t>=(1-eta)F_t. Identity (2) says I_t=B_t+F_t+A_t,
so (1-beta)I_t<=F_t+A_t. Therefore

```
(1-eta)(F_t+A_t) <=(1-beta)A_t,
(1-eta)I_t <=A_t,
B_t+F_t=I_t-A_t <=eta I_t.
```

This proof also covers zero leaf mass without division. Replacing (10)
by D>=1/(eta-beta) would discard the favorable cancellation and lose much
of the improvement. The required threshold is
(1-eta)/(eta-beta).

For a pure power, take eta=t*m^(t-1). For every inner source rank s>n/m,
concavity gives

```
n^t-(n-s)^t >=t*n^(t-1)*s >=eta*s^t.
```

Root complement capacity is nonnegative and can be omitted. Thus (11)
proves the n^t supersolution inequality for (1). The next section funds a
stronger majorant without an adverse final inverse-slack power.

## 5. Shifted logarithms and the local tangent exponent

Fix t0 in (0,1), p>0 and c>=p/(1-t0). Define

```
f(x)=A0*x^t0*(c+ln x)^p   for x>=1,       f(0)=0,
tau(x)=t0+p/(c+ln x).
```

Here A0 is a positive normalization chosen below. On x>=1, tau(x)<=1 and

```
f'(x)=f(x)*tau(x)/x,
f''(x)/f(x)=x^(-2)[tau(x)(tau(x)-1)-p/(c+ln x)^2] <=0.     (12)
```

For positive integer e<=n, log(1+y)<=y, with
1+y=(c+ln e)/(c+ln n)>0, gives the exact bound

```
f(e)/f(n)
 =(e/n)^t0[(c+ln e)/(c+ln n)]^p
 <=(e/n)^tau(n).                                         (13)
```

The zero-rank term is handled by f(0)=0. Concavity on [1,n] gives, for
n-s>=1, f(n)-f(n-s)>=f'(n)s. When s=n the same inequality follows
from tau(n)<=1. Hence for every inner source,

```
f(n)-f(n-s) >=tau(n)*f(n)*s/n
 >=eta_tau*f(n)*(s/n)^tau,
eta_tau=tau*m^(tau-1).                                   (14)
```

Apply (6)--(10) at t=tau(n), with eta=eta_tau. By (13) the total exit
charge is at most f(n)n^(-tau)(B_tau+F_tau), and by (14) the inner source
capacity is at least f(n)n^(-tau)eta_tau I_tau. Root capacity remains
nonnegative. These bounds prove

```
sum_s S_s f(n-s)+sum_e E_e f(e) <=(sum_s S_s)f(n).         (15)
```

Suppose a finite certificate establishes these guards uniformly for all
n>=n0. Set

```
A0=n0^(1-t0)/(c+ln n0)^p.                                (16)
```

Since the logarithmic derivative of f(x)/x is (tau(x)-1)/x<=0,
f(n)>=n for 1<=n<=n0. Use rank-one evaluation in this base range.
Strong induction with (1) and (15) gives L(n)<=f(n) at every rank.
Finally, a desired final exponent z>t0 at an explicit N follows from

```
ln A0+p*ln(c+ln N) <=(z-t0)*ln N.                         (17)
```

Every term in (17), including normalization and the base cutoff, must be
funded. The height change alone is not a numerical saving certificate.

## 6. A reusable finite certificate for all larger ranks

The following guards turn the infinitely many local exponents and heights
into a finite list of inequalities. Fix ell0>=1 and choose n0>=m*M^ell0.
Let t_hi be an upper bound for tau(n0). On [t0,t_hi], certify

```
T_t0>P_t0,
(d/dt)ln(T_t/P_t)>=d>0,
q_t<=Q,       u_t<=U<1,       v_t<=V<1,
B_t<=beta I_t,       eta_t>=eta_min>beta,
T_(t+s)/T_t >=P_(t+s)/P_t.                                (18)
```

Then q_t>=exp(d(t-t0)). For n with height ell>=ell0,

```
n<m*(M^(ell+1)+1),
ln n<ln m+(ell+1)ln M+ln 2,
q_tau^(a*ell+1)
 >=exp[d*p*(a*ell+1)/(c+ln m+(ell+1)ln M+ln 2)].           (19)
```

The fraction in (19) is increasing in ell if

```
a*(c+ln m+ln 2)+(a-1)ln M >=0,
```

which holds for the positive integer a used here. Consequently the single
exact inequality

```
(1-U^ell0)*
 (exp[d*p*(a*ell0+1)/(c+ln m+(ell0+1)ln M+ln 2)]-1)
 -Q*M^lambda*V^ell0
 >=(1-eta_min)/(eta_min-beta)                             (20)
```

implies (10) for every larger ell. The right side decreases with eta;
therefore eta_min is the correct conservative endpoint. This proves a
uniform recurrence, rather than inferring one from a rank scan.

Useful finite guard reductions use increasing tilted means
mu_T(t)=d ln T_t/dt and mu_P(t)=d ln P_t/dt, whose derivatives are
nonnegative variances. For example
mu_T(t0)-mu_P(t_hi)>=d proves the derivative guard. The logarithmic
derivative of each ratio T_(t+s)/T_t or P_(t+s)/P_t is nonnegative,
so u_t is increasing and its upper endpoint suffices. The stronger
simple guard T_(t0+s)/T_t0 >=P_(t_hi+s)/P_t_hi proves the required
ordering of these ratios throughout the interval. Loose endpoint bounds
Q>=T_t_hi/P_t0 and V>=M^lambda(T_(t_hi-lambda)/P_t0)^g are valid because
all native ranks are at least one. The mirror guard (4) must still be
certified on every elementary interval throughout [t0,t_hi].

One exploratory p7 choice is

```
t0=.99731352, p=.1, c=38, M=256, a=b=1,
s=lambda=.1, ell0=100,
Q=1.001, U=.961, V=.903, d=1.72,
beta=.321, eta_min=.9845.
```

For n0=121*256^100, use t_hi=.997481. The smaller trial endpoint
.9974808 fails to cover tau(n0) and is an explicit rejection control.
The exact package receipt certifies these guards and (17), alongside the
newer native profiles. Other profiles may use different guards.

## 7. Native caller assumptions and limits

The theorem consumes the same native hypotheses as the predecessor finite
compiler. In particular it assumes all-column arbitrary-input correctness
at every positive integer column multiplicity; actual disjoint productive
owners; the literal chronological paid interface; and permitted, priced
whole-job adapters including the input map. Correlated contents of distinct
fields do not permit field aliasing, input cloning, or extra productive
credit. Each raw instance retains its owned centers and scratch until its
word initializes, uses, restores and erases them. All unmatched jobs,
source complements, moves, adapters, coefficients and ownership operations
remain present in the finite word.

The arbitrary-height flow has finitely many classes and integer weights.
Its source counts and recursive batch denominators must be cleared with
actual divisible widths. The normalized recurrence alone does not bound
those widths or physical resources. [PR #4436](https://github.com/CrocSwap/integer-mult-bounds/pull/4436)'s fixed-rule finite counting
method can be applied after accounting for the new G=O(log n), but no old
numerical precision or stock constant may simply be copied to the new
expanded word. An ambient rank reduction is neither a materialized-word
size bound nor a practical runtime claim.

The native tensor realization, analytic transfer, exact recovery, precision,
fine-prime exclusions, stock, whole-job implementation tariffs, and physical
fixed-tape execution assumptions remain inherited. Finite arithmetic or
flow checks do not establish those premises. This theorem does not merge
or scientifically admit pending profiles, change the selected record, or
by itself prove a larger multiplication kappa.

## Open next questions

1. Independently check the arbitrary-height flow and mirror identity,
   including small root sources and empty-root classes. A finite integer
   check should distinguish this flow from the old minimum-target height.
2. Extend the certificates beyond the three supplied raw profiles using
   (18)--(20), or improve their geometry while holding the consumer saving
   fixed. Compare complete final ranks through (17), including normalization.
3. Audit the resulting word's native physical implementations and full
   finite constants. The theorem removes an exponent-convergence obstacle;
   it does not discharge those caller obligations.
