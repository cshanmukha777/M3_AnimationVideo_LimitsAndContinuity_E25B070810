import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

from art import BG, CYAN, GOLD, GREEN, WHITE, text, math, line

BOUNDARIES = (0, 864, 2256, 3408, 4872, 6432, 7200)
CHECKS = (
    ("Read the missing point", "What are the approaching height and the assigned height?",
     r'\lim_{x\to 2} f(x)=4,\qquad f(2)=1',
     "The open circle marks the approaching height. The filled point gives the value."),
    ("Choose an input tolerance", "If the output must be within 0.2 of 4, how close should x be to 2?",
     r'\epsilon=0.2,\qquad \delta=0.2',
     "The line has slope one, so the input and output distances are equal."),
    ("Compare the two approaches", "What happens to the heights at x = 1.99 and x = 2.01?",
     r'f(1.99)=3.99,\qquad f(2.01)=4.01',
     "One output approaches four from below. The other approaches four from above."),
    ("Find the rule that applies", "After cancelling, can we use x + 2 to find the original value at x = 2?",
     r'x\ne 2\;:\; f(x)=x+2,\qquad f(2)=1',
     "Cancellation requires a nonzero denominator. The separate rule still gives one."),
    ("Test the jump", "Could setting the filled point to height four make the jump continuous?",
     r'\lim_{x\to 2^-}h(x)=4\ne 2=\lim_{x\to 2^+}h(x)',
     "Changing one value cannot change either of the two one-sided limits."),
)


def card(index, revealed, path):
    title, question, equation, explanation = CHECKS[index]
    image = Image.new("RGB", (1920, 1080), BG)
    text(image, (145, 48), f"M3  /  {index+1:02}/06  /  PRACTICE", 25, CYAN)
    text(image, (145, 130), title, 72)
    text(image, (145, 330), question, 41, WHITE)
    line(image, (145, 460), (1775, 460), "#263344", 3)
    if revealed:
        math(image, (145, 535), equation, 78, GREEN)
        text(image, (145, 750), explanation, 35)
    else:
        text(image, (145, 570), "Think it through. The answer appears in a moment.", 39, GOLD)
    image.save(path)


def run(*args):
    subprocess.run(["ffmpeg", "-v", "error", "-y", *map(str, args)], check=True)


def extend(source, output):
    with tempfile.TemporaryDirectory() as temp:
        work = Path(temp)
        args = ["-i", source]
        filters = []
        sequence = []
        for index, (start, end) in enumerate(zip(BOUNDARIES, BOUNDARIES[1:])):
            filters.extend((
                f"[0:v]trim=start_frame={start}:end_frame={end},setpts=PTS-STARTPTS[v{index}]",
                f"[0:a]atrim=start_sample={start*4000//3}:end_sample={end*4000//3},asetpts=PTS-STARTPTS[a{index}]",
            ))
            sequence.append(f"[v{index}][a{index}]")
            if index == len(CHECKS):
                continue
            for number, seconds in enumerate((8, 12)):
                picture = work / f"{index}-{number}.png"
                card(index, bool(number), picture)
                args.extend(("-framerate", "36", "-i", picture))
                label = f"{index}{number}"
                stream = index*2+number+1
                filters.extend((
                    f"[{stream}:v]format=yuv420p,tpad=stop_mode=clone:stop={seconds*36-1}[pv{label}]",
                    f"anullsrc=r=48000:cl=stereo,atrim=duration={seconds}[pa{label}]",
                ))
                sequence.append(f"[pv{label}][pa{label}]")
        filters.append("".join(sequence)+f"concat=n={len(sequence)}:v=1:a=1[video][audio]")
        run(*args, "-filter_complex_threads", "2", "-filter_complex", ";".join(filters),
            "-map", "[video]", "-map", "[audio]", "-c:v", "libx264", "-threads", "4",
            "-preset", "veryfast", "-crf", "21", "-r", "36", "-c:a", "aac",
            "-b:a", "160k", "-t", "300", "-movflags", "+faststart", output)


if __name__ == "__main__":
    extend(*sys.argv[1:])
