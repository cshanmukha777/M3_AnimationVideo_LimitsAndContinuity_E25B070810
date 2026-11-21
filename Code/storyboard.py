"""Generate the submission storyboard from the source script and frames."""
import json
import math
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

from main import CUES, FPS, LEAD, ROOT, SPEED, TAILS, duration
from scenes import frame

DETAIL = (
    ("Separate approaching height from assigned output.",
     "Approach input 2 using gold and blue points with horizontal guides. Hold the endpoint markers.",
     "Open (2, 4) excludes that point. Filled (2, 1) gives f(2) = 1."),
    ("Define limits, notation and one-sided approaches.",
     "Reveal the tolerance statement and the left and right approach symbols in narration order.",
     "x is the input, a is the target input, f(x) is the output and L is the limit. Use x different from a."),
    ("Infer the limit from samples on each side.",
     "Animate each side on the same axes, then compare both guides. The filled point stays at height 1.",
     "The left and right limits equal 4. The assigned function value is f(2) = 1."),
    ("Evaluate the limit of the piecewise function f.",
     "Reveal the two branches, factor the numerator, cancel and show the limiting height.",
     "f(x) = (x² − 4)/(x − 2) = x + 2 for x different from 2. f(2) = 1. The limit equals 4."),
    ("Apply the three tests to three explicitly named functions.",
     "Show f, then the parabola g, then the jump h. Move the dots along each function's own branches.",
     "f: limit 4, value 1. g(x) = x² + 1: limit and value 5. h: left 4, right 2, value 2."),
    ("Reinforce the three takeaways and display credits.",
     "Hold the recap, then reveal the reference, source and voice credits for reading.",
     "A finite two-sided limit concerns nearby outputs. Continuity requires the limit and value to agree."),
)
PREVIEW_BEAT = (1, 2, 2, 2, 1, 1)
W, H = 612, 792


def paragraph(pdf, text, y, size=10.5):
    style = ParagraphStyle("storyboard", fontName="Helvetica", fontSize=size,
                           leading=size*1.31, textColor=colors.HexColor("#233540"))
    block = Paragraph(escape(text), style)
    _, height = block.wrap(W-88, 600)
    block.drawOn(pdf, 44, y-height)
    return y-height-8


def render():
    chapters = json.loads((ROOT / "Narration" / "cues.json").read_text())
    output = ROOT / "Storyboard" / "M3_Animation_Storyboard.pdf"
    pdf = canvas.Canvas(str(output), pagesize=(W,H))
    pdf.setTitle("M3 Animation Storyboard | Limits and Continuity")
    pdf.setAuthor("Shanmukha Sai Chakali")
    pdf.setFillColor(colors.HexColor("#101820"))
    pdf.rect(0, 315, W, H-315, fill=1, stroke=0)
    pdf.setFillColor(colors.HexColor("#59e2c3"))
    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(44, 729, "LINEAR ALGEBRA AND CALCULUS  /  M3")
    pdf.setFillColor(colors.white)
    pdf.setFont("Helvetica-Bold", 42)
    pdf.drawString(44, 655, "Limits and Continuity")
    pdf.setFont("Helvetica", 16)
    pdf.drawString(45, 613, "Animation storyboard")
    pdf.drawString(45, 568, "Shanmukha Sai Chakali  |  E25B070810")
    pdf.drawImage(ImageReader(frame(0, 1, 0.7)), 45, 276, 522, 293.625)
    paragraph(pdf, "Learning objective", 237, 14)
    paragraph(pdf, "By the end of this video, the viewer will be able to understand the behaviour of a function near a point, calculate a limit, distinguish a function's limit from its actual value, and determine whether a function is continuous at a given point.", 209, 12)
    pdf.showPage()
    start = 0
    for i, (title, narration) in enumerate(chapters):
        seconds = duration(ROOT / "Narration" / "audio" / f"scene-{i+1}.mp3")
        length = math.ceil((LEAD+seconds/SPEED+TAILS[i])*FPS)/FPS
        pdf.setFillColor(colors.HexColor("#087765"))
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(44, 750, f"SCENE {i+1:02}  /  {start:.1f}–{start+length:.1f}s   ({length:.1f}s)")
        pdf.setFillColor(colors.HexColor("#101820"))
        pdf.setFont("Helvetica-Bold", 28)
        pdf.drawString(44, 712, title)
        pdf.drawImage(ImageReader(frame(i, PREVIEW_BEAT[i], 0.85)), 44, 423, 474, 266.625)
        y = 399
        for heading, body in zip(("Purpose", "Visual and animation direction", "Mathematical content"), DETAIL[i]):
            y = paragraph(pdf, f"{heading} — {body}", y)
        y = paragraph(pdf, "Narration", y-3, 12)
        cue_times = (LEAD, *(LEAD + t/SPEED for t in CUES[i]))
        for time, cue in zip(cue_times, narration):
            y = paragraph(pdf, f"{start+time:.1f}s  {cue}", y)
        if y < 30:
            raise ValueError(f"Scene {i+1} exceeds its page")
        pdf.showPage()
        start += length
    pdf.save()


if __name__ == "__main__":
    render()
