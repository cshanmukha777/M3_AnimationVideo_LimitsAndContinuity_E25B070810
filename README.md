# Limits and Continuity

**Final video (1.4×, 3:34)** · [Watch M3_Limits_and_Continuity_1_4x.mp4](https://drive.google.com/file/d/1vjdrGkKUSzoacc3ZCEr43ZkQ7luTXziS/view)

## Building the five-minute practice cut

The editable source lives in _Code/. Run from the directory containing this README. Install Python 3.10+, the DejaVu Sans font, FFmpeg and ffprobe. The included takes are the six ElevenLabs George recordings. The original harmonic bed is synthesized at build time.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python _Code/main.py
python _Code/storyboard.py
```

The first render command creates Video/M3_Limits_and_Continuity_Video.mp4, with 1.5× narration and five silent practice checks, including the pitch-preserved narration and music. To reproduce the soundtrack before the speed adjustment:

```sh
PYTHONPATH=_Code python -c 'from pathlib import Path; from main import narration; narration(Path("."))'
ffmpeg -y -i voice.wav -f lavfi -i 'aevalsrc=0.17*(sin(2*PI*130.8128*t)+0.6*sin(2*PI*195.9977*t)+0.45*sin(2*PI*261.6256*t))*(0.65+0.35*sin(2*PI*t/19)):s=48000:d=300' -filter_complex '[1:a]volume=-27dB,afade=t=in:d=2,afade=t=out:st=297:d=3[bed];[0:a][bed]amix=inputs=2:duration=first:normalize=0' -ar 48000 -ac 2 -c:a aac -b:a 128k mix.m4a
```

Scene landmarks are 0:00, 0:44, 1:43, 2:35, 3:35 and 4:39. Musical tones use a root, fifth and octave. The closing frame credits the synthesized music. The renderer fits the voice to the original five-minute timeline before accelerating the six narrated segments to a combined 3:20. Five 20-second practice checks bring the practice cut to 5:00. Each check gives eight seconds to think and 12 seconds to read the answer.

## Mathematics

For every nearby input distinct from 2, the quotient equals x + 2, hence the absolute output error from 4 equals the absolute input error from 2. Any positive epsilon permits delta equal to epsilon here. The original assigned value is 1. Raising this point depicts redefining the function at 2. The parabola has limit and value 5, while the jump has left limit 4 and right limit 2.
