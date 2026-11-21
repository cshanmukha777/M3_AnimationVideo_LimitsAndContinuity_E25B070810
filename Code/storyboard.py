"""Generate the submission storyboard from the source script and frames."""
import json
import math
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

from main import FPS, LEAD, ROOT, SPEED, TAILS, duration
from scenes import frame

DETAIL = (
    ("Separate a nearby height from an assigned value.",
     "Move the gold and blue points inward along the same line, with axis guides. Reveal the two heights.",
     "Nearby rule x + 2. Open (2, 4). Filled (2, 1)."),
    ("Define the limit and its symbols.",
     "Hold the limit notation on screen and reveal the nearby rule and directional notation.",
     "x is an input, a is the target input, f(x) is an output and L is the limiting output."),
    ("Show where the two one-sided limits come from.",
     "Animate each direction on the same scale. Remove the assigned point while keeping the approaching curve.",
     "Both sides approach 4. The value at 2 can be 1 or undefined."),
    ("Evaluate a limit and construct a continuous extension.",
     "Reveal factorization, cancellation and the limiting result. Fill the hole during the piecewise example.",
     "The quotient (x² − 4)/(x − 2) equals x + 2 for x different from 2. Define g(2) = 4."),
    ("Interpret the three continuity checks on graphs.",
     "Switch between the complete line, moved point and jump. Highlight the failed checks.",
     "Complete: 4 = 4. Moved: 4 differs from 1. Jump: one-sided limits 4 and 2 disagree."),
    ("Reinforce three takeaways and credit the tools and references.",
     "Hold the recap and credits for reading, with an end marker in the closing beat.",
     "A limit describes nearby outputs. The assigned value can differ. Continuity needs agreement."),
)
PREVIEW_BEAT = (1, 2, 2, 2, 2, 1)
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
        for cue in narration:
            y = paragraph(pdf, cue, y)
        if y < 30:
            raise ValueError(f"Scene {i+1} exceeds its page")
        pdf.showPage()
        start += length
    pdf.save()


if __name__ == "__main__":
    render()
