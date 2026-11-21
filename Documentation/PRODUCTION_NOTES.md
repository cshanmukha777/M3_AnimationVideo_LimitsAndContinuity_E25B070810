# Production notes

The revised animation uses Pillow and FFmpeg for its editable mathematical renderer. The six scenes use eased samples and audiovisual cues. The continuity comparison changes the function name and graph together. The official brief allows custom Python animations. Six generated MP3 takes use one George library voice. No music competes with the explanation.

The plot uses a common axis scale in every graph scene. Teal marks the function, gold marks motion from the left, blue marks motion from the right, and rose highlights an assigned point when it differs from the approaching height or a continuity condition fails.

Cue times in the rendering code are specific to the included takes. To regenerate narration, open ElevenLabs Text to Speech, choose George and Multilingual v2, and generate the exact paragraphs for each scene as one take. Export MP3 at 44.1 kHz, preferably 128 kbps, and name the files scene-1.mp3 through scene-6.mp3 under Narration/audio/. Set the source-audio cue times in Code/main.py to the new paragraph starts. Render again and regenerate the storyboard.

Page 4 of the brief refers to four deliverables but its printed list only names video and code. The repository also includes the PDF storyboard from page 3 and supporting documents as required on page 1.

Before submitting, have a peer review the video for unclear transitions and verify the public repository in a private browser window. Submit its URL through the instructor's Google Form once it is shared, before the 25 November deadline.
