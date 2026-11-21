from itertools import accumulate
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image as PDFImage
from io import BytesIO
from main import ROOT,DURATIONS
from scenes import frame,TITLES

def build():
    style=getSampleStyleSheet()
    parts=[]
    def para(s,kind="BodyText"):
        parts.extend((Paragraph(s,style[kind]),Spacer(1,12)))
    para("Limits and Continuity","Title")
    para("Linear Algebra and Calculus • Shanmukha Sai Chakali • E25B070810")
    para("By the end of the film, the viewer can interpret a two-sided limit, evaluate a removable quotient and check continuity at a point.")
    script=(ROOT/"Narration/narration_script.md").read_text().split("\n## ")[1:]
    directions=["Predict the approaching height and compare it with the filled point.","Shrink equal output and input tolerances about 4 and 2.","Track both live coordinates on the line.","Factor the numerator, strike the common nonzero factors and evaluate the limit.","Lift the assigned value to repair the hole, then compare the parabola and jump.","Recall the three observations and credit the sources."]
    for i,(section,direction) in enumerate(zip(script,directions)):
        parts.append(PageBreak())
        title,body=section.split("\n\n",1)
        para(title,"Heading1")
        stream=BytesIO()
        frame(i,.55).save(stream,format="PNG")
        stream.seek(0)
        parts.append(PDFImage(stream,width=450,height=253.125))
        para(direction)
        para(body)
    SimpleDocTemplate(str(ROOT/"Storyboard/M3_Animation_Storyboard.pdf")).build(parts)

if __name__=="__main__":
    build()
