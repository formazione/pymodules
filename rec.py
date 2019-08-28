import os
import glob

x = 0
def record():
	global x
	if not "H:\\ffmpeg\\output" + str(x) + ".mp4" in glob.glob("H:\\ffmpeg\\*.mp4"):
		filename = "H:\\ffmpeg\\output\\output" + str(x) + ".mp4"
	else:
		x += 1
		record()

	audio = "Microfono (8- Logitech USB Headset)"
	video_size = "1366x768"

	os.system(f"""ffmpeg -y -rtbufsize 200M -f gdigrab -thread_queue_size 1024 -probesize 10M -r 10 -draw_mouse 1 -video_size {video_size} -i desktop -f dshow -channel_layout stereo -thread_queue_size 1024 -i audio="{audio}" -c:v libx264 -r 10 -preset ultrafast -tune zerolatency -crf 25 -pix_fmt yuv420p -c:a aac -strict -2 -ac 2 -b:a 128k -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" "{filename}" """)


record()