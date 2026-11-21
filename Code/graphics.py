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


def study_plot(draw, kind, progress, sides=()):
    """Plot the selected function near x=2, with optional moving samples."""
    from models import RULES, ENDPOINTS

    box(draw, 48, 144, 466, 332)
    def point(x, y):
        return 92+88*x, 436-40*y

    for x in range(5):
        line(draw, point(x,0), point(x,6.6))
        label(draw, *point(x,-0.24), str(x), 12, MUTED, anchor="mt")
    for y in range(1,7):
        line(draw, point(0,y), point(4.25,y))
        label(draw, 83, point(0,y)[1], str(y), 12, MUTED, anchor="rm")
    line(draw, point(0,0), point(4.25,0), MUTED)
    line(draw, point(0,0), point(0,6.6), MUTED)
    label(draw, 477, 429, "x", 15, MUTED)
    label(draw, 67, 162, "y", 15, MUTED)
    dash(draw, point(2,0), point(2,6.35), MUTED)
    left_rule, right_rule, right_edge = RULES[kind]
    for start, end, rule in ((0,2,left_rule), (2,right_edge,right_rule)):
        points = [point(start+(end-start)*i/100, rule(start+(end-start)*i/100))
                  for i in range(101)]
        draw.line([(round(x*2),round(y*2)) for x,y in points], fill=TEAL, width=6)
    for side in sides:
        distance = (0.29 if kind == "g" else 0.5) * (1-progress) + 0.10*progress
        x = 2+side*distance
        y = (left_rule if side < 0 else right_rule)(x)
        color = GOLD if side < 0 else BLUE
        dash(draw, point(x,0), point(x,y), color)
        dash(draw, point(0,y), point(x,y), color)
        disk(draw, point(x,y), color, radius=4)
    for value, hollow in ENDPOINTS[kind]:
        disk(draw, point(2,value), TEAL if hollow or kind=="g" else PINK,
             radius=6, hollow=hollow)
