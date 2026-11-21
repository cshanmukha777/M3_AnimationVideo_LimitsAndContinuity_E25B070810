# Mathematical verification

## Limit notation and the moving dots

For the examples shown, a two-sided limit is L if for every positive tolerance ε there is a positive δ such that admissible x with 0 < |x − a| < δ satisfy |f(x) − L| < ε. The minus and plus superscripts restrict x to the left and right of a respectively. Both sides contain nearby domain points in this lesson. The two-sided finite limit exists when their finite limits agree.

Near 2 the curve is y = x + 2. The four sampled pairs are (1.5, 3.5), (1.9, 3.9), (2.5, 4.5), and (2.1, 4.1). Each satisfies y − 4 = x − 2. Thus δ = ε works on both sides. The open circle is (2, 4). A filled dot at (2, 1) sets f(2) = 1. Removing that filled dot leaves f(2) undefined. Neither edit changes y − 4 = x − 2 at nearby inputs or changes the limit.

## Quotient and continuous extension

1. The denominator vanishes at 2. Substitution gives 0/0, so the quotient is undefined there.
2. Expanding (x − 2)(x + 2) gives x² − 4 because the two linear terms cancel.
3. Dividing by x − 2 is valid for x ≠ 2. The quotient then equals x + 2.
4. The nearby difference from 4 is x − 2, which tends to zero. The limit is 4 from either side.
5. The graph is the line y = x + 2 except for the open circle at (2, 4).
6. Let g equal the quotient for x ≠ 2 and set g(2) = 4. The same limit exists, the value is defined, and both equal 4. Therefore g is continuous at 2.

## Continuity comparison

| Graph | Rule near 2 | Left limit | Right limit | Value at 2 | Result |
|---|---|---|---|---|---|
| Complete line | x + 2 | 4 | 4 | 4 | Continuous |
| Moved point | x + 2 for x ≠ 2 | 4 | 4 | 1 | Removable discontinuity |
| Jump | x + 2 for x < 2 and x for x ≥ 2 | 4 | 2 | 2 | Jump discontinuity |

For the jump, the open point (2, 4) belongs to the left branch's limiting position and the filled point (2, 2) gives the right branch's endpoint. Since 4 ≠ 2, the common limit does not exist. Any reassignment at x = 2 leaves both one-sided limits unchanged.

The derivations above independently check the displayed equations and the plotted coordinates. The remaining external checks are a human peer review and the student's paper rehearsal.
