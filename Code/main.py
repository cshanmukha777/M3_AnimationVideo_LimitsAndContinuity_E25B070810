"""Render the six narrated chapters with FFmpeg.

Cue times are source-audio seconds. Playback is slowed slightly for a
classroom pace. Visuals change on the same adjusted timeline as the voice.
"""
from bisect import bisect_right
from itertools import accumulate
from pathlib import Path
import argparse
import math
import subprocess
import tempfile

from PIL import Image
from graphics import HEIGHT, WIDTH
from scenes import frame

ROOT = Path(__file__).resolve().parents[1]
SPEED = 0.84
LEAD = 0.65
TAILS = (2, 2, 2, 2, 2, 5)
CUES = ((13.25,), (13.3, 25.1), (11.7, 22.4), (14.45, 28.5),
        (19.3, 39.3), (10.55,))
FPS = 24


def duration(path):
    result = subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "csv=p=0", str(path)], text=True)
    return float(result)


def render(output):
    audio = [ROOT / "Narration" / "audio" / f"scene-{i+1}.mp3" for i in range(6)]
    counts = [math.ceil((LEAD + duration(path)/SPEED + TAILS[i])*FPS)
              for i, path in enumerate(audio)]
    with tempfile.TemporaryDirectory() as directory:
        directory = Path(directory)
        soundtrack = directory / "soundtrack.m4a"
        mix = [
            f"[{i}:a]aresample=48000,atempo={SPEED},"
            f"adelay={round(LEAD*1000)},apad,atrim=duration={count/FPS}[a{i}]"
            for i, count in enumerate(counts)
        ]
        mix.append("".join(f"[a{i}]" for i in range(6)) +
                   "concat=n=6:v=0:a=1,loudnorm=I=-17:TP=-2:LRA=8[out]")
        command = ["ffmpeg", "-loglevel", "error", "-y"]
        for path in audio:
            command.extend(("-i", str(path)))
        subprocess.run(command + ["-filter_complex", ";".join(mix), "-map", "[out]",
                       "-ar", "48000", "-c:a", "aac", "-b:a", "80k", str(soundtrack)],
                       check=True)
        output.parent.mkdir(parents=True, exist_ok=True)
        command = [
            "ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo",
            "-pixel_format", "rgb24", "-video_size", f"{WIDTH}x{HEIGHT}",
            "-framerate", str(FPS), "-i", "pipe:0", "-i", str(soundtrack),
            "-map", "0:v", "-map", "1:a", "-pix_fmt", "yuv420p",
            "-c:v", "libx264", "-preset", "ultrafast", "-crf", "24",
            "-threads", "3", "-c:a", "copy", "-movflags", "+faststart", str(output),
        ]
        with subprocess.Popen(command, stdin=subprocess.PIPE) as encoder:
            previous = None
            last_scene_frame = None
            picture = None
            pixels = b""
            for scene, count in enumerate(counts):
                boundaries = [0, *(LEAD + t/SPEED for t in CUES[scene]), count/FPS]
                print(f"Rendering scene {scene+1}: {count/FPS:.2f}s", flush=True)
                for index in range(count):
                    t = index/FPS
                    beat = bisect_right(boundaries, t) - 1
                    elapsed = t-boundaries[beat]
                    span = boundaries[beat+1]-boundaries[beat]
                    fraction = min(1, elapsed/(span*0.76))
                    progress = round(fraction*fraction*(3-2*fraction), 2)
                    static = scene in (1, 5) or scene == 0 and beat == 1 or scene == 3 and beat < 2
                    key = (scene, beat, 0 if static else progress)
                    if key != previous:
                        picture = frame(*key)
                        pixels = picture.tobytes()
                        previous = key
                    if last_scene_frame is not None and t < 0.42:
                        encoder.stdin.write(Image.blend(last_scene_frame, picture, t/0.42).tobytes())
                    else:
                        encoder.stdin.write(pixels)
                last_scene_frame = picture
            encoder.stdin.close()
            if encoder.wait() != 0:
                raise RuntimeError("Video encoding failed")
    return list(accumulate(count/FPS for count in counts))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "Video" / "M3_Limits_and_Continuity_Video.mp4")
    options = parser.parse_args()
    print("Scene end times:", render(options.output))
