from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title :",yt.title)

print("View :", yt.view)

yd = yt.stream.get_highest_resolution()

yd.Download('./YTfolder')