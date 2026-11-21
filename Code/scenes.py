"""Six chapters. Each narration beat selects a graph and its matching claim."""
from graphics import BLUE, GOLD, INK, MUTED, PINK, TEAL, box, canvas, card, header, label, study_plot


def hook(draw, beat, p):
    header(draw, 1, "Limits and Continuity", "Shanmukha Sai Chakali  •  E25B070810")
    study_plot(draw, "f", p if beat==0 else 1, (-1,1))
    card(draw, 152, "Where are the points heading?", "Follow the two horizontal guides.")
    if beat:
        card(draw, 235, "Nearby outputs approach 4", "Both moving points approach the hole.")
        card(draw, 318, "The assigned output is 1", "Read the filled point at input 2.", PINK)
        label(draw, 542, 420, "Read a graph  •  Calculate  •  Test continuity", 14, MUTED)


def notation(draw, beat, p):
    header(draw, 2, "What does a limit say?", "A statement about function values near an input.")
    box(draw, 48, 147, 865, 106)
    label(draw, 80, 168, "lim", 34, INK, True)
    label(draw, 67, 211, "x → a", 17, GOLD)
    label(draw, 153, 176, "f(x)  =  L", 34, TEAL, True)
    label(draw, 430, 169, "x   input           a   target input", 20)
    label(draw, 430, 204, "f(x)   output     L   limiting output", 20)
    if beat >= 1:
        label(draw, 66, 286, "Any desired output tolerance", 22, TEAL, True)
        label(draw, 66, 323, "Take domain inputs x sufficiently close to a, with x ≠ a.", 20)
    if beat == 2:
        label(draw, 66, 387, "Approach from both sides", 22, TEAL, True)
        label(draw, 66, 422, "x → a⁻   smaller inputs", 20, GOLD)
        label(draw, 450, 422, "x → a⁺   larger inputs", 20, BLUE)
        label(draw, 66, 461, "A finite two-sided limit requires equal finite one-sided limits.", 17)


def intuition(draw, beat, p):
    header(draw, 3, "Read the graph of f", "The same function stays on screen throughout this scene.")
    study_plot(draw, "f", p if beat<2 else 1, ((-1,), (1,), (-1,1))[beat])
    card(draw, 152, "Left-hand limit  →  4", "1.50 → 3.50          1.90 → 3.90", GOLD)
    if beat >= 1:
        card(draw, 235, "Right-hand limit  →  4", "2.50 → 4.50          2.10 → 4.10", BLUE)
    if beat == 2:
        card(draw, 318, "Two-sided limit  =  4", "Open (2, 4). Filled (2, 1).")
        label(draw, 544, 420, "f(2) = 1", 24, PINK, True)


def worked(draw, beat, p):
    header(draw, 4, "Calculate the limit of f", "Track which branch applies before simplifying.")
    study_plot(draw, "f", p, (-1,1) if beat==2 else ())
    box(draw, 539, 147, 374, 100)
    label(draw, 556, 161, "f(x) = (x² − 4)/(x − 2),   x ≠ 2", 17, TEAL, True)
    label(draw, 556, 196, "f(2) = 1", 19, PINK, True)
    if beat == 0:
        card(draw, 264, "The quotient at x = 2", "0/0 is undefined. The branch gives 1.")
    if beat >= 1:
        card(draw, 260, "x² − 4 = (x − 2)(x + 2)", "Factor the difference of squares.")
        card(draw, 335, "f(x) = x + 2   for x ≠ 2", "Cancel the nonzero factor x − 2.")
    if beat == 2:
        card(draw, 410, "Limit = 2 + 2 = 4", "The assigned value stays at 1.", GOLD)


def continuity(draw, beat, p):
    kind = ("f","g","h")[beat]
    titles = ("f  •  Removable discontinuity","g  •  Continuous","h  •  Jump discontinuity")
    subtitles = ("f(2) = 1, while nearby outputs approach 4.",
                 "g(x) = x² + 1",
                 "h(x) = x + 2 for x < 2.  h(x) = x for x ≥ 2.")
    header(draw, 5, titles[beat], subtitles[beat])
    study_plot(draw, kind, p, (-1,1))
    values = (
        ("f(2) = 1","Both sides approach 4.","1 ≠ 4. Assign 4 to repair the hole."),
        ("g(2) = 2² + 1 = 5","Both sides approach 5.","5 = 5. All three checks pass."),
        ("h(2) = 2","Left → 4. Right → 2.","No common limit to compare."),
    )[beat]
    checks = ("1. Is the value defined?", "2. Does the limit exist?", "3. Do they agree?")
    for index, (heading, detail) in enumerate(zip(checks, values)):
        color = PINK if (beat==0 and index==2) or (beat==2 and index==1) else TEAL
        if beat==2 and index==2:
            color=MUTED
        card(draw, 152+82*index, heading, detail, color)


def summary(draw, beat, p):
    header(draw, 6, "Read the approach. Check the point.", "Limits and Continuity  •  Shanmukha Sai Chakali  •  E25B070810")
    for index, text in enumerate((
        "A limit describes the nearby outputs.",
        "The assigned value can differ from the limit.",
        "Continuity requires both values to exist and agree.",
    )):
        y = 148+59*index
        box(draw, 48,y,865,48)
        label(draw, 69,y+13,str(index+1),19,TEAL,True)
        label(draw, 110,y+13,text,20,INK,True)
    if beat:
        label(draw, 49, 346, "REFERENCES & CREDITS", 13, TEAL, True)
        label(draw, 49, 376, "Course brief: M3 Animation Video Project Instructions", 16)
        label(draw, 49, 402, "Visual teaching reference: 3Blue1Brown", 16)
        label(draw, 49, 428, "AI assistance: ChatGPT (script, graphics, code), ElevenLabs (voice)", 16)
        label(draw, 49, 454, "Original animation  •  No background music", 16)


SCENES = (hook, notation, intuition, worked, continuity, summary)


def frame(scene, beat, progress):
    image, draw = canvas()
    SCENES[scene](draw, beat, progress)
    return image
