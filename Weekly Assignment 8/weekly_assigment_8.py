import ffmpeg
import json

output = ""

try:
    probe = ffmpeg.probe('Bath_VFX_v01.JPG')
    output = json.dumps(probe, indent=2)
except ffmpeg.Error as e:
    print('Error:', e.stderr.decode())

with open("output.txt", "w") as f:
    f.write(output)