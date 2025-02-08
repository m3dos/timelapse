#!/usr/bin/env python3
import subprocess
import os

# Directory where your images are stored.
images_dir = "timelapse_images"

# Build the ffmpeg command as a list.
ffmpeg_command = [
    "ffmpeg",
    "-framerate", "15",
    "-start_number", "79",
    "-i", os.path.join(images_dir, "time_lapse_%05d.jpg"),
    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",
    "timelapse.mp4"
]

print("Running ffmpeg command:")
print(" ".join(ffmpeg_command))

try:
    subprocess.run(ffmpeg_command, check=True)
    print("Timelapse video created successfully!")
except subprocess.CalledProcessError as e:
    print("An error occurred while running ffmpeg:")
    print(e)
