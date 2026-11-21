# Mathematical verification

At an interior approach point a, a finite two-sided limit L means that for every ε > 0 there is δ > 0 such that every domain input with 0 < |x − a| < δ satisfies |f(x) − L| < ε. The one-sided definitions restrict inputs to x < a and x > a. With nearby domain points on both sides, equal finite one-sided limits give the finite two-sided limit. Take the smaller of the two δ values to prove the forward construction. Restrict the two-sided condition to each side to prove the converse.

## Example A · Piecewise f

For x ≠ 2, f(x) = (x² − 4)/(x − 2). By definition f(2) = 1. Multiplication verifies (x − 2)(x + 2) = x² − 4. Cancellation requires x − 2 ≠ 0, so f(x) = x + 2 for x ≠ 2. The quotient by itself is undefined at 2 because substitution yields 0/0. The separately assigned value of f at 2 is 1 throughout the video.

For nearby inputs, |f(x) − 4| = |x − 2|, so δ = ε works. Independently substituting the displayed inputs gives:

| Input | 1.50 | 1.90 | 2.10 | 2.50 |
|---|---:|---:|---:|---:|
| Output | 3.50 | 3.90 | 4.10 | 4.50 |

Both approaches land at the limiting height 4. The graph marks (2,4) open and (2,1) filled. Conditions 1 and 2 pass. Condition 3 fails because 1 ≠ 4. Reassigning the value to 4 gives a different function that is continuous at 2.

## Example B · Parabola g

g(x) = x² + 1 on the real numbers. Substitution gives g(2) = 5 and the graph shows the filled point (2,5). For |x − 2| < 1, |g(x) − 5| = |x − 2||x + 2| ≤ 5|x − 2|. Choosing δ = min(1, ε/5) verifies both sides approach 5. The left samples are below 5 and the right samples are above 5 near 2. The value exists, the limit exists, and 5 = 5. All three continuity conditions pass.

## Jump · Function h

h(x) = x + 2 for x < 2 and h(x) = x for x ≥ 2. As x tends to 2 from the left, the output approaches 4. From the right it approaches 2. This follows from |x + 2 − 4| = |x − 2| on the left and |x − 2| on the right. The left marker (2,4) is open and (2,2) is filled, giving h(2) = 2. Condition 1 passes and condition 2 fails. There is no common limit to compare in condition 3. Reassigning h(2) cannot change the two one-sided limits.

## Renderer

Every sampled dot is computed by evaluating its own branch, then mapping both coordinates onto the same scale as the axes. Endpoint data independently encode the assigned point and excluded limiting point. The parabola is shown in a local window around 2. The drawn branch ends at x = 2.35, which gives y = 6.5225 inside the displayed range.
