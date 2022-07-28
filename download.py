from gettext import find
from pytube import YouTube
from pyfiglet import Figlet
from tqdm import tqdm
import os
import subprocess



# Banner
banner = Figlet(font='bubble')
print(banner.renderText('YT MUSIC'))

#Save path
PATH="Save/"

#run opendrop for 22 seconds
subprocess.run(["bash", "find.sh"])
print("Done.")

# Ask to enter music link
print("incoming prompt ...")
link = input("Enter the YouTube Link =>")

for i in tqdm (range (1), desc="Downloading..."):
    try:
        ytube = YouTube(link)
    except:
        print("Cannot Connect")
    # Audio only format
    thisVideo = ytube.streams.filter(only_audio=True).first()
    try:
        save = thisVideo.download(PATH)
        #save as mp3
        base, ext = os.path.splitext(save)
        save_file = base + '.mp3'
        os.rename(save, save_file)
    except:
        print("An error was detected.")
        # print file has been successfully downloaded
        print(ytube.title + " has been successfully downloaded.")

#opendrop send to receiver
subprocess.run(["bash", "send.sh"])

