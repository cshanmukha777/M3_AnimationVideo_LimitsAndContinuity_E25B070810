import argparse
import math
import subprocess
import tempfile
from pathlib import Path

from scenes import frame

ROOT=Path(__file__).resolve().parents[1]
FPS=24
DURATIONS=(36,58,48,61,65,32)
REVEALS=(.65,.76,.71,.72,.44,.74)
AMBIENT="aevalsrc=0.17*(sin(2*PI*130.8128*t)+0.6*sin(2*PI*195.9977*t)+0.45*sin(2*PI*261.6256*t))*(0.65+0.35*sin(2*PI*t/19)):s=48000:d=300"


def ffmpeg(*args):
    subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-y",*map(str,args)],check=True)


def length(path):
    return float(subprocess.check_output(["ffprobe","-v","error","-of","csv=p=0",
        "-show_entries","format=duration",path],text=True))


def narration(directory):
    parts=[]
    for i,seconds in enumerate(DURATIONS):
        voice=ROOT/"Narration"/"audio"/f"scene-{i+1}.mp3"
        path=directory/f"part-{i}.wav"
        tempo=length(voice)/(seconds-1.50)
        ffmpeg("-i",voice,"-af",f"atempo={tempo},adelay=750,apad,atrim=duration={seconds}",
               "-ar","48000","-ac","1",path)
        parts.append(path)
    track=directory/"voice.wav"
    ffmpeg(*(v for path in parts for v in ("-i",path)),"-filter_complex",
           "concat=n=6:v=0:a=1,loudnorm=I=-17:TP=-2:LRA=8","-ar","48000",track)
    return track


def render(output):
    output.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory() as directory:
        stereo=Path(directory)/"mix.m4a"
        voice=narration(Path(directory))
        ffmpeg("-i",voice,"-f","lavfi","-i",AMBIENT,"-filter_complex",
               "[1:a]volume=-27dB,afade=t=in:d=2,afade=t=out:st=297:d=3[bed];[0:a][bed]amix=inputs=2:duration=first:normalize=0",
               "-ar","48000","-ac","2","-c:a","aac","-b:a","128k",stereo)
        cmd=["ffmpeg","-loglevel","error","-y","-f","rawvideo","-pix_fmt","rgb24",
             "-s","1920x1080","-r",str(FPS),"-i","pipe:0","-i",str(stereo),"-vf","setsar=1",
             "-c:v","libx264","-pix_fmt","yuv420p","-threads","3","-preset","ultrafast",
             "-crf","22","-c:a","copy","-movflags","+faststart",str(output)]
        with subprocess.Popen(cmd,stdin=subprocess.PIPE) as encoder:
            for i,seconds in enumerate(DURATIONS):
                previous=None
                for n in range(seconds*FPS):
                    time=n/FPS
                    motion=time-min(.75,max(0,time-seconds*REVEALS[i]))
                    p=round(min(1,motion/(seconds-.75)),3)
                    if i==5:
                        p=1
                    if p!=previous:
                        pixels=frame(i,p).tobytes()
                        previous=p
                    encoder.stdin.write(pixels)
            encoder.stdin.close()
            if encoder.wait():
                raise RuntimeError("Encoding failed")


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,default=ROOT/"Video"/"M3_Limits_and_Continuity_Video.mp4")
    render(parser.parse_args().output)
