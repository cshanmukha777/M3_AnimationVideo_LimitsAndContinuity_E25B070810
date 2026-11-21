# Revision validation

- FFprobe reported 1920 × 1080 (16:9 by frame dimensions), H.264 at 24 fps, 6,807 video frames, 48 kHz AAC and a runtime of 283.629 seconds (4:44).
- FFmpeg decoded both streams end to end with error escalation enabled. Black-frame detection reported no black interval of at least 0.1 seconds at the selected threshold. Whole-track sample peak was −1.5 dBFS and mean was −18.7 dBFS.
- Video frames from each scene, the opening and closing, and all three cases in the continuity scene were visually inspected. Rendered frames show matching labels and markers.
- Word-timed transcription matched all six narration scripts, ignoring case and punctuation. Paragraph cues lead the first spoken word by approximately 0.27–0.55 seconds after playback adjustment. This checks the spoken words and paragraph synchronization. A continuous human listening pass and peer feedback remain outstanding.
- The revised storyboard generated seven pages, with one cover and six time-coded scenes. Its previews use the same renderer and its narration uses the same source as the video.
- Independently checked 98 exact rational input samples against the analytical rules and verified the three sets of endpoint markers. See the mathematical verification document for the general proofs.
