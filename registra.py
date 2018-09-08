import os


def registra_senza_audio():
    os.system("""ffmpeg -y -rtbufsize 100M -f gdigrab -framerate 30 -probesize 10M -draw_mouse 1 -i desktop -c:v libx264 -r 30 -preset ultrafast -tune zerolatency -crf 25 -pix_fmt yuv420p "video output.mp4" """)


def registra_con_audio():
    "Metti -r 15 per avere sicronizzato audio e video"
    os.system("""ffmpeg -y -rtbufsize 200M -f gdigrab -thread_queue_size 1024 -probesize 10M -r 15 -draw_mouse 1 -i desktop -f dshow -channel_layout stereo -thread_queue_size 1024 -i audio="Cube pro Virtual In 3/4 (CubePro WDM Audio)" -c:v libx264 -r 15 -preset ultrafast -tune zerolatency -crf 25 -pix_fmt yuv420p -c:a aac -strict -2 -ac 2 -b:a 128k "video output.mp4" """)


print("""
    1. senza audio
    2. con audio""")

if input("> ") == "1":
    registra_senza_audio()
else:
    registra_con_audio()
