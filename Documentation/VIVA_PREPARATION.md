# Viva preparation

1. **What does the video teach?** It teaches how to infer nearby behaviour, compute a limit, and test continuity at one point.
2. **What does lim as x → a of f(x) = L mean?** Outputs can be made as close to L as desired by taking inputs sufficiently close to a and different from a.
3. **What do x, a, f(x) and L represent?** The input, target input, output for that input, and limiting output.
4. **Why exclude x = a when defining the limit?** The definition measures surrounding behaviour. The exact input may have a different value or be outside the domain.
5. **What is the left-hand limit?** The value approached as x gets close through inputs smaller than a.
6. **What is the right-hand limit?** The value approached as x gets close through inputs larger than a.
7. **When do these give a two-sided limit?** In the examples, both one-sided limits must exist and agree.
8. **Can the limit exist when the function is undefined?** Yes. Removing (2, 4) from y = x + 2 keeps both approaches to 4.
9. **What does the filled dot at (2, 1) tell us?** The function's assigned value at x = 2 is 1.
10. **Why does substitution give 0/0 in the quotient?** At x = 2, both x² − 4 and x − 2 evaluate to zero. The quotient is undefined at that input.
11. **How did you factor x² − 4?** It is a difference of squares, giving (x − 2)(x + 2).
12. **Why may you cancel x − 2?** At every input under consideration other than 2, the factor is nonzero.
13. **How does the graph confirm the result?** The quotient equals x + 2 away from 2. That line approaches the height 4 from both directions.
14. **What are the three continuity checks?** The assigned value exists, the limit exists, and they agree.
15. **How do you repair the removable case?** Set the value at 2 equal to 4 while keeping the nearby rule.
16. **Why can you not repair the jump that way?** The two branches approach different heights. Editing one assigned value leaves those approaches unchanged.
17. **How does Manim generally work?** A Python scene creates mathematical objects and changes them over time with animations. This project uses Pillow to draw frames and FFmpeg to encode them instead.
18. **How do you place a point on the graph in code?** The coordinate helper maps (x, y) to (92 + 88x, 440 − 49y) in design units. The minus flips the upward math axis for the pixel canvas.
19. **How do the moving dots stay on the line?** The code computes an input on each side of 2, calculates y = x + 2 and uses the same coordinate helper for the dot and its projections.
20. **Why choose the colors and timing?** Opposite approaches use gold and blue, the common curve uses teal, and assigned values that fail continuity use rose. On-screen changes are timed to the relevant spoken paragraph.
