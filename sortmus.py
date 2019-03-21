#!/usr/bin/env python3

# A program I wrote to finally convert all of those old "AQXZ.mp3" files
# retrieved from my old 3rd gen ipod to their actual name

# Instructions of operations, comment out all but 'collectmus()' in the 
# directory containing all the 'F##' folders which contain the music files
# then uncomment everything and comment out 'collectmus()' and move program
# to the directory 'tempunsorted' and run the rest of it
# NOTE: The above may not be true. test later, but os.chdir() seems to be
# the trick to getting this all done in one step

# NOTE: The following were run in stages, to be done all at once, this must
# be edited further
# non-standard libraries and programs required:
#	 mutagen		-  sudo pip3 install mutagen
#	 avconv			-  sudo apt-get install libav-tools

import os
import re
from mutagen.easyid3 import EasyID3


# gather all the 'FGYZ.mp3' files into one folder: 'tempunsorted'


def collectmus():
	print("\n collecting music files...?")
	
	os.system("mkdir tempunsorted")
	os.system("mkdir tempunsorted/oldm4a")

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
			command = "avconv -i "+q+i+q+' '+q+i[:-4]+".mp3"+q
			os.system(command)
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
				command = """mv %s "%s" """ % (i,newtitle)
				os.system(command)
				#print(command)
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
			command = "mv "+q+i+q+" "+q+artist[0]+q
			os.system(command)
		except:
			errorlist2.append(i)



collectmus()

os.system("cd tempunsorted")
# Can't get this directory change to work, so this has to be done in 2 steps :/
m4a2mp3()

titlechange()

sortbyartist()


print("\n\nDone!")

