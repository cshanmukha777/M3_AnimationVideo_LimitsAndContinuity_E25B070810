# Limits and Continuity

Narrator: George · ElevenLabs Multilingual v2

## 01/06 · Hook / Context · 0:00–0:44

Imagine covering just one point on this graph with your fingertip. You can still see the gold point climbing from the left and the blue point coming down from the right. Which height would you predict under your finger? Follow the line and you would guess four. Lift your finger, though, and the filled point is down at one. Both readings are correct. One describes the surrounding curve. The other tells us what the function actually assigns at the input two.

## 02/06 · Concept Introduction · 0:44–1:43

Keep your eye on height four. The horizontal strip marks how far above or below four we are willing to let the output wander. Its half width is called epsilon. Now look down at the input axis. The vertical strip selects inputs close to two. Its half width is called delta. For this particular line, moving one tenth horizontally changes the height by exactly one tenth. So we can choose delta equal to epsilon. Narrow the horizontal strip, and the vertical strip tightens with it. Every selected input except two gives an output inside the horizontal strip. However small you make the tolerance, the same argument works. That is what the limit statement means.

## 03/06 · Visual Intuition · 1:43–2:35

Follow the coordinate labels. The first number is the input. The second is the height. Starting on the left, one point five gives three point five. As the gold point slides right, each remaining gap to two is exactly the remaining gap to four. Now watch the blue point. It starts on the right and approaches the same height from above. The right-hand limit is also four. Since the two sides agree, the two-sided limit is four. The open circle marks an excluded point. The filled point still gives the actual value at two, which is one.

## 04/06 · Worked Example · 2:35–3:35

Can algebra explain the line we just saw? Away from two, the function is the quotient on screen. At two itself, a separate rule assigns one. Look first at the numerator. The difference of two squares factors into x minus two times x plus two. Now the same factor appears above and below the fraction bar. For nearby inputs different from two, that factor is nonzero. Dividing the top and bottom by it leaves x plus two. Keep the restriction in view. This cancellation describes the curve on either side of the hole. As the input approaches two, the simplified expression approaches two plus two, or four. The assigned value at the exact point still comes from the separate rule.

## 05/06 · Interpretation · 3:35–4:39

Continuity at a point takes three checks. Is there an assigned value? Is there a two-sided limit? Do they agree? Here the first two answers are yes, but one and four differ. Imagine redefining just the assigned value. Lift that single point up to the hole. Once it reaches four, the repaired function is continuous. The neighbouring curve never had to move. Now switch to a different function, the parabola x squared plus one. At two its height is five, and both sides approach five. All three checks pass. Finally look at the jump. The branch on the left approaches four, while the branch on the right approaches two. Moving one point cannot bring those branches together. This time the two-sided limit itself is missing.

## 06/06 · Summary & Credits · 4:39–5:00

Read a graph in three passes. First, follow the nearby outputs from both sides. If they approach the same height, that height is the limit. Second, read the filled point to find the assigned value. The two numbers can differ. Third, test continuity. The assigned value and the limit must both exist and agree. Those three questions let you distinguish a continuous curve, a repairable hole, and a jump.
