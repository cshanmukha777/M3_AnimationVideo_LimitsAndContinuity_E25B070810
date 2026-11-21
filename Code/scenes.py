"""Scene drawings. Each beat introduces a specific part of the argument."""
from graphics import (BLUE, GOLD, INK, MUTED, PINK, TEAL, box, canvas,
                      card, graph, header, label)


def hook(draw, beat, p):
    header(draw, 1, "Limits and Continuity", "Shanmukha Sai Chakali  •  E25B070810")
    graph(draw, "moved", p, (-1,1), hole=True)
    card(draw, 153, "Where are the dots going?", "Follow the curve as the input nears 2.")
    if beat:
        card(draw, 234, "Nearby height  →  4", "Both travelling dots approach the hole.")
        card(draw, 315, "Assigned height  =  1", "The filled dot gives the value at 2.", PINK)
        label(draw, 541, 412, "Predict • Calculate • Check continuity", 15, MUTED)


def notation(draw, beat, p):
    header(draw, 2, "What a limit means", "Read the notation from the input to the output.")
    box(draw, 48, 146, 865, 97)
    label(draw, 80, 171, "lim", 32, INK, True)
    label(draw, 64, 211, "x → a", 16, GOLD)
    label(draw, 147, 183, "f(x)  =  L", 34, TEAL, True)
    label(draw, 416, 178, "x  input     a  target input", 19)
    label(draw, 416, 209, "f(x)  output     L  target output", 19)
    for index, (heading, detail) in enumerate([
        ("Nearby outputs", "Make f(x) as close to L as desired by taking x close enough to a, with x ≠ a."),
        ("On the line x + 2", "As x approaches 2, x + 2 approaches 4."),
        ("Two directions", "x → a⁻ from smaller inputs     •     x → a⁺ from larger inputs"),
    ][:beat+1]):
        y = 267 + 71*index
        label(draw, 65, y, heading, 20, TEAL, True)
        label(draw, 65, y+28, detail, 17)


def intuition(draw, beat, p):
    header(draw, 3, "Read the graph", "Open circles mark excluded points. Filled dots give assigned values.")
    sides = ((-1,), (1,), (-1,1))[beat]
    kind = "hole" if beat == 2 and p > 0.62 else "moved"
    graph(draw, kind, p, sides, hole=True)
    card(draw, 153, "From the left  →  4", "x: 1.5 → 1.9     y: 3.5 → 3.9", GOLD)
    if beat >= 1:
        card(draw, 234, "From the right  →  4", "x: 2.5 → 2.1     y: 4.5 → 4.1", BLUE)
    if beat == 2:
        card(draw, 315, "The two sides agree", "The limit is 4 in both versions.")
        label(draw, 545, 421, "f(2) is undefined" if kind == "hole" else "f(2) = 1", 20, PINK, True)


def worked(draw, beat, p):
    header(draw, 4, "Work it out", "Evaluate the limit of the quotient as x approaches 2.")
    graph(draw, "complete" if beat == 3 and p > 0.58 else "hole",
          p, (-1,1) if beat == 2 else (), hole=True)
    lines = [
        ("(x² − 4) / (x − 2)", "At x = 2, substitution gives 0/0."),
        ("= [(x − 2)(x + 2)] / (x − 2)", "Factor the numerator."),
        ("= x + 2     for x ≠ 2", "Cancel only when x − 2 is nonzero."),
        ("Limit  =  2 + 2  =  4", "The quotient has a hole at (2, 4)."),
    ]
    if beat == 3:
        card(draw, 153, "Define g piecewise", "Keep the quotient for x ≠ 2.")
        card(draw, 234, "Set g(2) = 4", "This assigns the missing output.")
        card(draw, 315, "Limit = g(2) = 4", "g is continuous at 2.")
    else:
        count = (2, 3, 4)[beat]
        for index, (heading, detail) in enumerate(lines[:count]):
            card(draw, 145+76*index, heading, detail)


def continuity(draw, beat, p):
    header(draw, 5, "Check continuity", "Apply the three conditions at x = 2.")
    kind = "complete" if beat == 0 or beat == 1 and p < 0.42 else "moved"
    if beat == 2:
        kind = "jump"
    graph(draw, kind, p, (-1,1) if kind == "moved" else (), hole=True)
    cases = {
        "complete": ("f(2) = 4", "Both sides approach 4.", "4 = 4   •   Continuous"),
        "moved": ("f(2) = 1", "Both sides approach 4.", "4 ≠ 1   •   Removable"),
        "jump": ("f(2) = 2", "Left → 4   •   Right → 2", "The two-sided limit is undefined."),
    }
    headings = ("1. The value is defined", "2. The limit exists", "3. They are equal")
    for index, (heading, detail) in enumerate(zip(headings, cases[kind])):
        fail = index == 2 and kind != "complete" or index == 1 and kind == "jump"
        card(draw, 153+81*index, heading, detail, PINK if fail else TEAL)
    label(draw, 544, 416, {"complete":"All three conditions pass.",
          "moved":"Assign 4 to repair the discontinuity.",
          "jump":"Changing only f(2) cannot repair a jump."}[kind], 15, MUTED)


def summary(draw, beat, p):
    header(draw, 6, "Three things to remember", "Limits and Continuity  •  Shanmukha Sai Chakali  •  E25B070810")
    for index, text in enumerate([
        "A limit describes what nearby outputs approach.",
        "The assigned value can differ from the limit.",
        "Continuity requires a value and a limit that agree.",
    ]):
        y = 147+59*index
        box(draw, 48, y, 865, 48)
        label(draw, 69, y+13, f"{index+1}", 19, TEAL, True)
        label(draw, 112, y+13, text, 19, INK, True)
    label(draw, 49, 348, "REFERENCES & CREDITS", 13, TEAL, True)
    label(draw, 49, 378, "Course brief: M3 Animation Video Project Instructions", 16)
    label(draw, 49, 404, "Visual teaching inspiration: 3Blue1Brown", 16)
    label(draw, 49, 430, "AI: ChatGPT assisted scripting, visuals and code. ElevenLabs generated the voice.", 16)
    label(draw, 49, 456, "Original graphs and animation  •  No background music", 16)
    if beat:
        label(draw, 910, 456, "END", 13, TEAL, True, anchor="rt")


SCENES = (hook, notation, intuition, worked, continuity, summary)


def frame(scene, beat, progress):
    image, draw = canvas()
    SCENES[scene](draw, beat, progress)
    return image
