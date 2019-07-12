# Music Sorting

A program I wrote to finally convert all of those old "AQXZ.mp3" files retrieved from my old 3rd gen ipod to their actual name. After running this program, the music files are renamed to "songname.mp3" then all the songs are sorted into a folder by artist. Additionally, any m4a files are converted to mp3 (old m4a files are stored in a separate folder, so they are not deleted).

To read more about the insights gained during the development of this, read my [blog entry](https://tclack88.github.io/blog/code/2019/05/24/music-sort.html) on it.

non-standard libraries and programs required:
        mutagen                -  sudo pip3 install mutagen
       *avconv                 -  sudo apt-get install libav-tools
        ffmpeg                 -  sudo apt install ffmpeg
   \*avconv is deprecated for later versions of ubuntu, so ffmpeg replaces it


## Instructions of operations
place `sortmus.py` in the directory containing all the 'F##' folders which contain the music files

non-standard libraries and programs required:
	mutagen                -  sudo pip3 install mutagen
	avconv                 -  sudo apt-get install libav-tools
	ffmpeg                 -  sudo apt install ffmpeg
	avconv is deprecated for later versions of ubuntu, so ffmpeg replaces it


## What happens in the process

### Step 1
songs (files of the form A-Z.mp3 or A-Z.m4a such as 'FGYZ.mp3') are gathered into one folder: 'tempunsorted'

### Step 2

Any m4a files are duplicated into an mp3 file and an original copy of the m4a file is moved into a directory titled 'oldm4a'

### Step 3
The id3 tags are read and the songs renamed according to the artist in the tag

### Step 4
The songs are iterated through and a list of unique artist names is created, a directory is created for each uniquly listed artist and the songs are then sorted into their respective directories.
