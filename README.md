# Limits and Continuity

**Linear Algebra and Calculus (M3)**  
Shanmukha Sai Chakali · E25B070810

[Watch or download the MP4](Video/M3_Limits_and_Continuity_Video.mp4) · [Storyboard PDF](Storyboard/M3_Animation_Storyboard.pdf) · [Viva preparation](Documentation/VIVA_PREPARATION.md)

By the end of this video, the viewer will be able to understand the behaviour of a function near a point, calculate a limit, distinguish a function's limit from its actual value, and determine whether a function is continuous at a given point.

The six scenes follow a pair of moving points toward a missing point, factor a quotient to recover the limiting height, and compare three explicitly named functions. The example f keeps its assigned value f(2) = 1. The separate parabola g(x) = x² + 1 is continuous at 2, with value and limit 5. The jump h has unequal one-sided limits.

## Reproduce the video

Use Python 3.10 or later, FFmpeg with libx264 and AAC, FFprobe, and DejaVu Sans. Make sure both FFmpeg executables are on your PATH. On Linux install the DejaVu font package. On macOS install DejaVu Sans and make its regular and bold TTF files discoverable by Pillow. If necessary, set Pillow's font search path by placing the TTF files in your working directory.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python Code/main.py
python Code/storyboard.py
```

The video command uses the six existing MP3 takes in `Narration/audio/`. The renderer maps the source-audio cue times to adjusted playback time and normalizes the combined narration. The storyboard generator uses the same cue schedule and scene renderer.

## Files

| Path | Content |
|---|---|
| `Video/` | Final H.264 MP4 with AAC narration |
| `Code/` | Editable scene functions, graph and drawing helpers, renderer and storyboard generator |
| `Storyboard/` | Six-scene storyboard PDF with timed narration and mathematical direction |
| `Narration/` | Script, machine-readable text cues and six source takes |
| `Documentation/` | Requirement map, mathematical checks, production notes, viva and credits |

## Credits

ChatGPT assisted with scripting, custom visuals, code and documentation. ElevenLabs generated the English voice-over using a library voice called George. The graphs and layouts were drawn for this project. Visual teaching inspiration came from 3Blue1Brown. The course brief established the assignment requirements. No background music is used. See [AI disclosure](Documentation/AI_DISCLOSURE.md) and [references](Documentation/REFERENCES.md).
