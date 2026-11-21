"""Canvas, typography and coordinate geometry for the six scenes."""
from functools import lru_cache
from PIL import Image, ImageDraw, ImageFont

BG = "#101820"
PANEL = "#182631"
INK = "#f1f6f7"
MUTED = "#adbfc8"
TEAL = "#59e2c3"
GOLD = "#ffcb74"
BLUE = "#8dc8ff"
PINK = "#ff9cae"
GRID = "#30434e"
WIDTH, HEIGHT = 1920, 1080


@lru_cache(maxsize=None)
def font(size, bold):
    family = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(family, size * 2)


def canvas():
    image = Image.new("RGB", (WIDTH, HEIGHT), BG)
    return image, ImageDraw.Draw(image)


def label(draw, x, y, text, size=19, color=INK, bold=False, anchor="lt"):
    draw.text((2*x, 2*y), text, font=font(size, bold), fill=color, anchor=anchor)


def line(draw, start, end, color=GRID, width=1):
    draw.line(tuple(2 * value for point in (start, end) for value in point),
              fill=color, width=width*2)


def box(draw, x, y, w, h, color=PANEL):
    draw.rounded_rectangle((2*x, 2*y, 2*(x+w), 2*(y+h)), radius=24, fill=color)


def disk(draw, point, color, radius=6, hollow=False):
    x, y = point
    draw.ellipse((2*(x-radius), 2*(y-radius), 2*(x+radius), 2*(y+radius)),
                 fill=PANEL if hollow else color, outline=color, width=5)


def dash(draw, start, end, color=GRID):
    for index in range(0, 22, 2):
        points = [tuple(a+(b-a)*fraction/22 for a,b in zip(start,end))
                  for fraction in (index, index+1)]
        line(draw, *points, color)


def coords(x, y):
    return (92 + 88*x, 440 - 49*y)


def graph(draw, kind, progress=1, moving=(), hole=False):
    box(draw, 48, 144, 466, 332)
    for x in range(5):
        line(draw, coords(x,0), coords(x,5.5))
        label(draw, *coords(x,-0.18), str(x), 12, MUTED, anchor="mt")
    for y in range(1,6):
        line(draw, coords(0,y), coords(4.25,y))
        label(draw, 83, coords(0,y)[1], str(y), 12, MUTED, anchor="rm")
    line(draw, coords(0,0), coords(4.25,0), MUTED)
    line(draw, coords(0,0), coords(0,5.55), MUTED)
    label(draw, 477, 431, "x", 14, MUTED)
    label(draw, 67, 162, "y", 14, MUTED)
    dash(draw, coords(2,0), coords(2,4.2), MUTED)
    if kind == "jump":
        line(draw, coords(0.2,2.2), coords(2,4), TEAL, 3)
        line(draw, coords(2,2), coords(3.35,3.35), TEAL, 3)
        disk(draw, coords(2,4), TEAL, hollow=True)
        disk(draw, coords(2,2), PINK)
    else:
        line(draw, coords(0.2,2.2), coords(3.35,5.35), TEAL, 3)
        if kind == "complete":
            disk(draw, coords(2,4), TEAL)
        elif hole:
            disk(draw, coords(2,4), TEAL, hollow=True)
            if kind == "moved":
                disk(draw, coords(2,1), PINK)
    for side in moving:
        x = 2 + side * (0.09 + 1.13*(1-progress)**2)
        color = GOLD if side < 0 else BLUE
        dash(draw, coords(x,0), coords(x,x+2), color)
        dash(draw, coords(0,x+2), coords(x,x+2), color)
        disk(draw, coords(x,x+2), color, radius=4)


def header(draw, scene, title, sub):
    label(draw, 48, 25, "LINEAR ALGEBRA AND CALCULUS  /  M3", 12, TEAL, True)
    label(draw, 48, 51, title, 37, INK, True)
    label(draw, 49, 106, sub, 16, MUTED)
    label(draw, 910, 28, f"{scene:02} / 06", 13, MUTED, anchor="rt")
    for index in range(6):
        box(draw, 48+index*146, 513, 132, 3, TEAL if index < scene else GRID)


def card(draw, y, heading, detail, color=TEAL):
    box(draw, 539, y, 374, 66)
    label(draw, 556, y+10, heading, 19, color, True)
    label(draw, 556, y+36, detail, 14, INK)
