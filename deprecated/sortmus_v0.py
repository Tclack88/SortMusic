#!/usr/bin/env python3

# A program I wrote to finally convert all of those old "AQXZ.mp3" files
# retrieved from my old 3rd gen ipod to their actual name

# Instructions of operations
# directory containing all the 'F##' folders which contain the music files
#
# non-standard libraries and programs required:
#        mutagen                -  sudo pip3 install mutagen
#        avconv                 -  sudo apt-get install libav-tools
#        ffmpeg                 -  sudo apt install ffmpeg
#   avconv is deprecated for later versions of ubuntu, so ffmpeg replaces it
import os
import re
from mutagen.easyid3 import EasyID3


# gather all the 'FGYZ.mp3' files into one folder: 'tempunsorted'


def collectmus():
        print("\n collecting music files...?")
        
        os.system("mkdir -p tempunsorted/oldm4a")
        x = [os.path.join(r,file) for r,d,f in os.walk(".") for file in f]
        for i in x:
                if re.match(r'^[./]{2}[/F,0-9]{4}[A-Z]{4}',i):
                        command = "mv "+i+" tempunsorted"
                        os.system(command)
        print("\nMusic files moved to folder 'tempunsorted'")





# convert any m4a files to mp3 files so the id3 tags will be read properly
def m4a2mp3():
        print("\nconverting all m4a files to mp3...")
        quote = """ " """
        q = quote[1]
        x = [file for r,d,f in os.walk(".") for file in f]
        filesremoved = []
        for i in x:
                if i.endswith(".m4a"):
                        #command = "avconv -i "+q+i+q+' '+q+i[:-4]+".mp3"+q
                        altcommand = "ffmpeg -i "+q+i+q+' '+q+i[:-4]+".mp3"+q
                        os.system(altcommand)
                        filesremoved.append(i)
                        command2 = "mv "+i+" oldm4a"
                        os.system(command2)
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
                                newtitle = newtitle.replace('"','\\"')
                                # Fixes errors for litteral "
                                command = """mv %s "%s" """ % (i,newtitle)
                                os.system(command)
                        except:
                                errorlist.append(i)

        return errorlist






def sortbyartist():
        quote = """ " """
        q = quote[1]    
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
                command = "mkdir "+q+i[0]+q
                os.system(command)
        for i in thelist:
                try:
                        song = EasyID3(i)
                        artist = song['artist']
                        # fix errors from litteral " in song
                        i = i.replace('"','\\"')
                        command = "mv "+q+i+q+" "+q+artist[0]+q
                        os.system(command)
                except:
                        errorlist2.append(i)



collectmus()

os.chdir('tempunsorted')

m4a2mp3()

titlechange()

sortbyartist()


print("\n\nDone!")

