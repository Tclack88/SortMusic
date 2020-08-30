#!/usr/bin/env python3

# A program I wrote to finally convert all of those old "AQXZ.mp3" files
# retrieved from my old 3rd gen ipod to their actual name

# 30 Aug 2020: update -- Code is now OS neutral. 
# For windows without python installed/ for non-programers, an executable has 
# been provided which has all it needs except for ffmpeg which will need to be 
# downloaded separately and added to the PATH.
# one set of instructions I found from a cursory google search: 
# https://www.thewindowsclub.com/how-to-install-ffmpeg-on-windows-10

# Instructions of operations
# directory containing all the 'F##' folders which contain the music files
#
# non-standard libraries and programs required:
#        mutagen                -  sudo pip3 install mutagen
#        avconv                 -  sudo apt-get install libav-tools
#        ffmpeg                 -  sudo apt install ffmpeg
#   avconv is deprecated for later versions of ubuntu, so ffmpeg replaces it
# ***For Windows users, ffmpeg must be installed and added to PATH***
import os
import re
import shutil
from mutagen.easyid3 import EasyID3


# gather all the 'FGYZ.mp3' files into one folder: 'tempunsorted'


def collectmus():
        print("\n collecting music files...?")
        
        os.makedirs("tempunsorted/oldm4a")
        x = [os.path.join(r,file) for r,d,f in os.walk(".") for file in f]
        for i in x:
                head, tail = os.path.split(i)
                if re.match(r'^[A-Z]{4}',tail):
                        os.rename(i,os.path.join('tempunsorted',tail))
        print("\nMusic files moved to folder 'tempunsorted'")





# convert any m4a files to mp3 files so the id3 tags will be read properly
def m4a2mp3():
        print("\nconverting all m4a files to mp3...")
        x = [file for r,d,f in os.walk(".") for file in f]
        filesremoved = []
        for i in x:
                if i.endswith(".m4a"):
                        altcommand = f'ffmpeg -i "{i}" "{i[:-4]}.mp3"' 
                        print(altcommand)
                        os.system(altcommand)
                        filesremoved.append(i)
                        shutil.move(i,'oldm4a') 
        print("The following files were converted to mp3:")
        for i in filesremoved:
                print(i)
        print("\nConversion Complete, m4a files moved to oldm4a folder")






# the main function which changes the name 
def titlechange():
        thelist = os.listdir()
        errorlist = []
        for i in thelist:
                if re.match(r'^[A-Z]{4}[.mp3]{4}',i):
                        try:
                                song = EasyID3(i)
                                title = song['title']
                                newtitle = title[0]+'.mp3'
                                shutil.move(i, newtitle) 
                        except:
                                errorlist.append(i)

        return errorlist






def sortbyartist():
        artistlist = []
        errorlist1 = []
        errorlist2 = []
        thelist = os.listdir()
        for i in thelist:
                try:
                        song = EasyID3(i)
                        artist = song['artist']
                        if artist not in artistlist:
                                artistlist.append(artist)
                                
                except:
                        errorlist1.append(i)

        for i in artistlist:
                os.mkdir(i[0])
        for i in thelist:
                try:
                        song = EasyID3(i)
                        artist = song['artist']
                        shutil.move(i, artist[0])
                except:
                        errorlist2.append(i)




collectmus()

os.chdir('tempunsorted')

m4a2mp3()

titlechange()

sortbyartist()

print("\n\nDone!")

