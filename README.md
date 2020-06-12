# Music Sorting

A program I wrote to finally convert all of those old "AQXZ.mp3" files retrieved from my old 3rd gen ipod to their actual name. After running this program, the music files are renamed to "songname.mp3" then all the songs are sorted into a folder by artist. Additionally, any m4a files are converted to mp3 (old m4a files are stored in a separate folder, so they are not deleted).

Preview:

![A preview of the program in action](https://github.com/Tclack88/blog/blob/gh-pages/assets/music-sort/sorting.gif?raw=true)

To read more about the insights gained during the development of this, read my [blog entry](https://tclack88.github.io/blog/code/2019/05/24/music-sort.html) on it.

non-standard libraries and programs required:
```
        mutagen                -  sudo pip3 install mutagen
       *avconv                 -  sudo apt-get install libav-tools
        ffmpeg                 -  sudo apt install ffmpeg
   \*avconv is deprecated for later versions of ubuntu, so ffmpeg replaces it
```

## Instructions of operations
`CAUTION: you probably should test this on a copied subsample of your music just in case. If something interrupts the process, you won't lose your data, it'll just exist in some weird middle step and you'll have to revert to manual labeling, something I assume you'd want to avoid`

Be sure to have installed the dependencies above, then download and place `sortmus.py` in the directory containing all the 'F##' folders which contain the music files. That's the assumed file structure we're dealing with. If you've long since deleted those and collected them elsewhere, just place the `sortmus.py` program in a directory with another directory you can call `F00` (or a favorite 2 digit number of your choice) then run it! In a matter of seconds it will all be renamed and sorted into a new folder called `tempunsorted`. At this point, that name will be a misnomer, but feel free to place it or reorganize it however you please.

## What happens in the process

### Step 1
songs (files of the form A-Z.mp3 or A-Z.m4a such as 'FGYZ.mp3') are gathered into one folder: 'tempunsorted'

### Step 2

Any m4a files are duplicated into an mp3 file and an original copy of the m4a file is moved into a directory titled 'oldm4a'

### Step 3
The id3 tags are read and the songs renamed according to the artist in the tag

### Step 4
The songs are iterated through and a list of unique artist names is created, a directory is created for each uniquly listed artist and the songs are then sorted into their respective directories.
