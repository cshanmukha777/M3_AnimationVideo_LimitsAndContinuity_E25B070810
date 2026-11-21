# Viva preparation

1. **What does the video teach?** How to read nearby behaviour, calculate a limit and test continuity at a point.
2. **What does a limit equal to L mean?** All outputs at sufficiently close domain inputs distinct from a can be kept within any chosen positive tolerance of L.
3. **What do x, a, f(x) and L represent?** The input, target input, output and limiting output.
4. **Why exclude x = a?** The value at that input can be assigned independently of the nearby behaviour.
5. **What is a left-hand limit?** The limit through inputs smaller than a.
6. **What is a right-hand limit?** The limit through inputs larger than a.
7. **When is there a finite two-sided limit?** When both one-sided limits exist as finite numbers and agree, for the two-sided approach points in this project.
8. **What does the open circle at (2,4) mean?** That point is excluded from the graph of f. It is the limiting position.
9. **What does the filled point at (2,1) mean?** f(2) is defined and equals 1.
10. **Why does the quotient give 0/0 at 2?** Both its numerator and denominator vanish there. The quotient is undefined there, while the second branch defines f(2).
11. **How did you factor x² − 4?** Use the difference of squares to get (x − 2)(x + 2).
12. **Why can you cancel x − 2?** The quotient branch applies only when x ≠ 2.
13. **How does the graph verify the limit?** The samples lie on y = x + 2 and approach 4 from either side of x = 2.
14. **What are the three continuity conditions?** The assigned value exists, the limit exists, and the two agree.
15. **Why is f removable?** Reassigning f(2) to 4 repairs it while preserving all nearby outputs.
16. **Why is g continuous at 2?** Both sides of x² + 1 approach 5, and substitution gives g(2) = 5.
17. **Why is h a jump?** Its one-sided limits at 2 differ, 4 versus 2. Changing h(2) cannot fix them.
18. **How are axes and plot points drawn?** Python maps each plotted coordinate to a pixel position. The vertical coordinate is flipped because image pixels count downward.
19. **How are motions and audio timed?** The renderer moves a sampled input toward 2 with easing, calculates its output from the correct branch, and changes beats at source-audio cue times adjusted for playback speed.
20. **What tools and design choices did you use?** Pillow draws each frame, FFmpeg encodes it, ElevenLabs narrates, and ReportLab makes the storyboard. Gold and blue separate directions. The open and filled markers communicate membership independently of colour.
