# Why the remaining finite-controller lower is null

The new PR531/535/741 source-specific upper bounds do not supply a numerical
necessary crossover scale. These constructions have coordinate rank73 and a
finite cover of group order V with bit length2628. V is a role-copy count;
interpreting it as a later supplier coordinate rank2^H invents an exponential.
No such interpretation is used here.

The current full optimized-GMP source upper, per gate type, is

    2^(2^72+3) * (n+1)^8.

Its fixed logarithmic coefficient is 4722366482869645213699. Even a compulsory
literal full-cover scalar operation has only an ordinary fixed work exponent
of a few thousand. The familiar eighth-root no-win argument cannot produce a
positive useful input exponent from these two quantities. Its failure says the
reference upper is too weak for this purpose; it says nothing about the unknown
actual crossing or the speed of the finite construction.

A concrete way to change this conclusion would be to prove, for the *same*
selected optimized source and declared instruction lowering, a finite-range
upper such as 2^C*(n+1)^8 with C below approximately1900 through n=2^100,
then compare it to a separately authenticated mandatory full-cover work floor.
That requires a source-complete bounded finite native call tree: all selected
Toom evaluations/interpolations, balanced and unbalanced recursive products,
basecase/linear/division helpers, data-dependent predication, and an inventory
of the actual word/SIMD opcode input widths. The present enormous finite-leaf
halting/transition bound cannot be replaced by a guessed small coefficient.

There is a simpler possible census through4096-bit operands: the selected
Skylake threshold26limbs and the next threshold73limbs leave only native
basecase and a shallow balanced Toom22 path. This would at best yield a modest
finite-prefix exclusion. It has not been developed into a new cost certificate
in this pass, and would not answer the request for a galactic-scale interval.

The current lower therefore remains null. A chosen activation or proof-validity
cutover is not substituted for a necessary crossover. No new reference algorithm,
schoolbook fallback comparator, CPU timing estimate or optimistic constant is
silently introduced.
