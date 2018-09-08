import os

# I file devono essere della stessa misura
"""
es.:
img01.PNG
img02.PNG
img03.PNG

"""

print("Le immagini devono essere im01.PNG img02.PNG ecc., il file audio si chiama Gismo.mp3")


def save():
    os.system("ffmpeg -r 1/60 -i img%02d.PNG -i Gismo.mp3 -vcodec mpeg4 -y movie4.mp4")


def png_mp3_mp4(mp3):
    os.system("ffmpeg -r 1/60 -i img%02d.png -i " + mp3 + " -vcodec mpeg4 -y movie4.mp4")


def save2():
    os.system("ffmpeg -r 1/5 -start_number 0 -i F:\_img\5bs\img%02d.PNG -c:v libx264 -r 30 -pix_fmt yuv420p out.mp4")


def img_n_audio():
    os.system("ffmpeg -i img01.PNG -i fiddle.wav -vcodec mpeg4 -y movie3.mp4")


def img_n_audio2():
    os.system("ffmpeg -loop 1 -i img01.PNG -i fiddle.wav -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest out.mp4")


print(*os.listdir(), sep("\n"))
png_mp3_mp4(input("Nome del file mp3: "))
os.system("movie4.mp4")
