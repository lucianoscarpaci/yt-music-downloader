from pytube import YouTube
from pyfiglet import Figlet
import os
import opendrop

# Banner
banner = Figlet(font='bubble')
print(banner.renderText('YT MUSIC'))

# Ask to enter music link
link = input("Enter Link >")

try:
    ytube = YouTube(link)
except:
    print("Cannot Connect")
# Audio only format
thisVideo = ytube.streams.filter(only_audio=True).first()

# destination to save file

# download
try:
    save = thisVideo.download("")
except:
    print("An error was detected.")
# print file has been successfully downloaded



#opendrop send to receiver
# opendrop find
# opendrop send

