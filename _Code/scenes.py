from PIL import Image, ImageDraw
from art import BG,WHITE,CYAN,GOLD,BLUE,RED,GREEN,MUTED,pt,text,math,line,dot,plane,smooth,clamp,glyph

TITLES=("Limits and Continuity","How close is close enough?","Two paths to one height","Why the hole appears","Three tests for continuity","Three ways to read a graph")


def marker(im,side,d,tracker=False):
    x=2+side*d
    y=x+2
    a,b=pt(x,y)
    color=GOLD if side<0 else BLUE
    line(im,(155,b),(a,b),color,2)
    dot(im,x,y,color,8)
    if tracker:
        end=(a+side*74,b+(80 if side>0 else -80))
        line(im,(a,b),end,color,2)
        text(im,end,f"({x:.2f}, {y:.2f})",32,color,"lm" if side>0 else "rm")


def endpoints(im):
    dot(im,2,4,RED,13,True)
    dot(im,2,1,RED,12)


def hook(im,p):
    plane(im)
    endpoints(im)
    for side in (-1,1):
        marker(im,side,1.55-1.48*smooth(p*1.6))
    text(im,(1230,395),"Which height?",58)
    if p>.46:
        math(im,(1250,510),r'\lim_{x\to 2} f(x)=4',57,CYAN)
    if p>.59:
        math(im,(1250,640),'f(2)=1',55,RED)


def tolerance(im,p):
    width=1.35-1.22*smooth(p)
    a,b=pt(2-width,4+width)
    c,d=pt(2+width,4-width)
    draw=ImageDraw.Draw(im,"RGBA")
    draw.rectangle((155,b,1183,d),fill=(79,218,216,43))
    draw.rectangle((a,203,c,900),fill=(255,196,86,36))
    for y in (b,d):
        draw.line((155,y,1183,y),fill=(79,218,216,48),width=10)
        draw.line((155,y,1183,y),fill=(79,218,216,195),width=2)
    plane(im)
    endpoints(im)
    math(im,(1220,310),r'|y-4|<\epsilon',60,CYAN)
    math(im,(1220,425),r'0<|x-2|<\delta',59,GOLD)
    math(im,(1220,552),r'\delta=\epsilon',60)
    text(im,(1220,660),f"Half-width   {width:.2f}",36)
    math(im,(1220,750),r'x\,\ne\,a,\quad a=2',42,MUTED)


def trackers(im,p):
    plane(im)
    endpoints(im)
    for side in (-1,1):
        start=0 if side<0 else .36
        marker(im,side,.50-.48*smooth((p-start)/.45),True)
    math(im,(1210,380),r'\lim_{x\to2^{-}} f(x)=4',56,GOLD)
    if p>.36:
        math(im,(1210,515),r'\lim_{x\to2^{+}} f(x)=4',56,BLUE)
    if p>.72:
        math(im,(1210,680),'f(2)=1',58,RED)


def algebra(im,p):
    plane(im)
    endpoints(im)
    x=1320
    size=74
    math(im,(1210,270),r'x\,\ne\,2',50,GOLD)
    if p < .22:
        math(im,(x-30,390),r"\frac{x^2-4}{x-2}",112)
        return
    blend=smooth((p-.22)/.10)
    strike=smooth((p-.49)/.09)
    vanish=smooth((p-.60)/.12)
    math(im,(x,398),'x^2-4',size,WHITE,(1-blend)*(1-vanish))
    factor=r'(x-2)'
    w,h=glyph(factor,size,RED).size
    math(im,(x-96,398),factor,size,RED,blend*(1-vanish))
    math(im,(x-90+w+128*vanish,398+80*vanish),r'(x+2)' if vanish<1 else 'x+2',size,WHITE,blend)
    if vanish<1:
        colour=tuple(round(v*(1-vanish)+b*vanish) for v,b in zip((235,240,250),(11,16,27)))
        line(im,(x-100*blend,490),(x+230+75*blend,490),colour,4)
        math(im,(x,520),factor,size,RED,1-vanish)
        if strike:
            for a,b in ((x-96,398),(x,520)):
                col=tuple(round(v*(1-vanish)+c*vanish) for v,c in zip((255,132,124),(11,16,27)))
                line(im,(a,b+h),(a+round(w*strike),b+h-round(h*strike)),col,5)
    if p>.75:
        math(im,(1200,686),r'\lim_{x\to2} f(x)=2+2=4',48,GREEN)


def interpret(im,p):
    if p<.49:
        plane(im)
        repair=smooth((p-.29)/.14)
        dot(im,2,4,RED,13,True)
        dot(im,2,1+3*repair,GREEN if repair==1 else RED,12)
        if repair==1:
            dot(im,2,4,GREEN,17,True)
            dot(im,2,4,GREEN,10)
        text(im,(1220,345),"Repair one value" if p>.27 else "At input two",46)
        math(im,(1220,465),r'\widetilde f(2)=4' if repair==1 else 'f(2)=1',58,GREEN if repair==1 else RED)
        math(im,(1220,600),r'\lim_{x\to2} f(x)=4',52)
    elif p<.75:
        plane(im,"g")
        dot(im,2,5,GREEN,12)
        math(im,(1210,350),'g(x)=x^2+1',63,CYAN)
        math(im,(1210,510),r'\lim_{x\to2}g(x)=g(2)=5',49,GREEN)
    else:
        plane(im,"h")
        dot(im,2,4,RED,13,True)
        dot(im,2,2,BLUE,12)
        math(im,(1200,340),r'h(x)=x+2,\quad x<2',47,GOLD)
        math(im,(1200,445),r'h(x)=x,\quad x\geq2',47,BLUE)
        math(im,(1200,595),r'4\,\ne\,2',64,RED)


def summary(im,p):
    for i,(s,c) in enumerate((("Follow both sides to find the limit.",CYAN),("Read the filled point for the assigned value.",GOLD),("Continuity requires both to exist and agree.",GREEN))):
        text(im,(150,255+i*130),s,52,c)
    text(im,(150,757),"M3 course brief   •   Visual teaching reference: 3Blue1Brown",32)
    text(im,(150,822),"Music: original synthesized ambient score   •   Voice: ElevenLabs George",32)
    text(im,(150,887),"ChatGPT assisted with script, mathematical graphics and code.",30,MUTED)


def frame(scene,p):
    im=Image.new("RGB",(1920,1080),BG)
    text(im,(145,48),f"M3  /  {scene+1:02}/06",25,CYAN)
    text(im,(145,97),TITLES[scene],60)
    if scene==0:
        text(im,(145,987),"Shanmukha Sai Chakali  •  E25B070810",30)
    (hook,tolerance,trackers,algebra,interpret,summary)[scene](im,p)
    return im
