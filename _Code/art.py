from functools import lru_cache
from io import BytesIO
from matplotlib.mathtext import math_to_image
from PIL import Image, ImageDraw, ImageFont

BG = "#0B101B"
WHITE = "#EDF2FB"
CYAN = "#54D5DF"
GOLD = "#FFC969"
BLUE = "#89B7FF"
RED = "#FF847C"
GREEN = "#81DFAB"
GRID = "#263344"
MUTED = "#A5B4C8"


@lru_cache(None)
def font(size):
    return ImageFont.truetype("DejaVuSans.ttf", size)


def text(im, xy, s, size=34, color=WHITE, anchor="lt"):
    ImageDraw.Draw(im).text(xy,s,font=font(size),fill=color,anchor=anchor)


@lru_cache(None)
def glyph(s, size, color):
    stream = BytesIO()
    math_to_image("$"+s+"$", stream, dpi=144, format="png", color=color,
                  prop=__import__("matplotlib.font_manager",fromlist=["FontProperties"]).FontProperties(size=size/2, math_fontfamily="cm"))
    src = Image.open(stream).convert("RGB")
    from PIL import ImageChops
    alpha = ImageChops.difference(src, Image.new("RGB",src.size,"white")).convert("L")
    peak=alpha.getextrema()[1]
    alpha=alpha.point(lambda x: round(255*x/max(1,peak)))
    out=Image.new("RGBA",src.size,color)
    out.putalpha(alpha)
    return out


def math(im, xy, s, size=52, color=WHITE, opacity=1):
    tile=glyph(s,size,color)
    mask=tile.getchannel("A")
    if opacity<1:
        mask=mask.point(lambda x:round(x*opacity))
    im.paste(tile,tuple(round(v) for v in xy),mask)
    return tile.size


def pt(x,y):
    return round(155+x*242),round(900-y*108)


def line(im,a,b,c,w=3):
    ImageDraw.Draw(im).line((a,b),fill=c,width=w)


def dot(im,x,y,c,r=10,hole=False):
    a,b=pt(x,y)
    ImageDraw.Draw(im).ellipse((a-r,b-r,a+r,b+r),fill=BG if hole else c,outline=c,width=4)


def plane(im,kind="f"):
    from models import RULES
    for x in range(5):
        line(im,pt(x,0),pt(x,6.45),GRID)
        text(im,pt(x,-.15),str(x),23,MUTED,"mt")
    for y in range(1,7):
        line(im,pt(0,y),pt(4.25,y),GRID)
        text(im,(132,pt(0,y)[1]),str(y),23,MUTED,"rm")
    line(im,pt(0,0),pt(4.3,0),MUTED)
    line(im,pt(0,0),pt(0,6.5),MUTED)
    text(im,pt(4.32,-.04),"x",27)
    text(im,(118,181),"y",27)
    left,right,end=RULES[kind]
    for a,b,rule in ((0,2,left),(2,end,right)):
        xs=[a+(b-a)*j/160 for j in range(161)]
        ImageDraw.Draw(im).line([pt(x,rule(x)) for x in xs],fill=CYAN,width=6)


def clamp(p):
    return max(0,min(1,p))


def smooth(p):
    p=clamp(p)
    return p*p*(3-2*p)
