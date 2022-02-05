#!/usr/bin/env python3

# A program I wrote to finally convert all of those old "AQXZ.mp3" files
# retrieved from my old 3rd gen ipod to their actual name

# 02 Feb 2022: update - removed dependency on ffmpeg to convert and instead 
# read metadata from mp4-type files; also fixed a bug where some files would be
# overwritten
# 18 Sep 18 Update: Fixed some issues with initial file move causing files to get lost
# Further Refinement with the title change and sort functions
# Output list of files that could not have their title fixed to a text file for manual work 
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
from mutagen.easymp4 import EasyMP4
from mutagen.wave import WAVE


# gather all the 'FGYZ.mp3' files into one folder: 'tempunsorted'

forbiddenregex = re.compile('["*/:<>\?\\\|\+,.;=\[\]]') #based on https://en.wikipedia.org/wiki/Filename#Comparison_of_filename_limitations

def collectmus():
        print("\n collecting music files...?")
        
        os.makedirs("tempunsorted")
        x = [os.path.join(r,file) for r,d,f in os.walk(".") for file in f]
        for i in x:
                head, tail = os.path.split(i)
                if re.match(r'^[A-Z]{4}',tail):
                        os.rename(i,os.path.join('tempunsorted',i[2:5] + tail))
        print("\nMusic files moved to folder 'tempunsorted'")


def getsongobject(file):
        mp4_extensions = ["m4a", "m4p", "m4v"]
        if any(file.endswith(ext) for ext in mp4_extensions):
                songobject = EasyMP4(file)
        elif file.endswith(".wav"):
                songobject = WAVE(file)
        else: #assumes other files are mp3
                songobject = EasyID3(file)
        return songobject


# the main function which changes the name 
def titlechange():
        thelist = os.listdir()
        errorlist = []
        for i in [s for s in thelist if re.match("^F[0-9]{2}[A-Z]{4}\.", s)]:
                try:
                        song = getsongobject(i)
                        title = song['title']
                        title = re.sub(forbiddenregex, '', title[0]).strip()
                        newtitle = title+i[-4:] #assumes 3 char file extensions
                        shutil.move(i, newtitle) 
                except:
                        errorlist.append(i)

        if len(errorlist) > 0:
                file = open('filenameerrors.txt','w')
                file.write('File Name Errors: \n')
                for i in errorlist:
                        file.write(i + '\n')
                file.close()

        return errorlist


def sortbyartist():
        errorlist = []
        thelist = os.listdir()
        for i in [s for s in thelist if s != "filenameerrors.txt"]:
                try:
                        song = getsongobject(i)
                        artist = re.sub(forbiddenregex, '', ''.join(song['artist'])).strip()
                        if not os.path.isdir(artist):
                                os.mkdir(artist)
                        album = re.sub(forbiddenregex, '', ''.join(song['album'])).strip()
                        artistalbum = artist + '/' + album
                        if not os.path.isdir(artistalbum):
                                os.mkdir(artistalbum)
                        shutil.move(i, artistalbum)

                except: errorlist.append(i)

        if len(errorlist) > 0:
                file = open('filemoveerrors.txt','w')
                file.write('File Move Errors: \n')
                for i in errorlist:
                        file.write(i + '\n')
                file.close()




collectmus()

os.chdir('tempunsorted')

titlechange()

sortbyartist()

print("\n\nDone!")
