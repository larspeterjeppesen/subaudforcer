# SubAudForcer
Change the forced audio and subtitles of all video files in a folder at once. Supports virtually any file format.

# About
This script lets you change/choose the default/forced audio and subtitle track for a set of video files. It will change all files in a folder in one go.

The script is intended for video files that have audio and subtitle tracks encoded within them. Sometimes, a specific track is forced/defaulted, meaning your favorite media player is likely to select that track by default. The point of the script is to modify those defaults. 
  
The script rewrites the entire file in the process, which means it will take a few seconds to a few minutes per file, depending on your PC and the size of the file. A program which makes the desired changes faster is possible, but is bound to be either restricted to a single file format, or much more complex.

# Disclaimer
This script is only tested on my own PC. Back up your data and use at your own risk. While the script will not modify any data outside of the folder you place it in, I do not take responsibility for anything that happens inside of it.
Should work on Windows, macOS & Linux. Only tested on Windows 10.

# Installation instructions (Windows 10)
Install python 3: https://www.python.org/downloads/

Install `ffmpeg` and `ffprobe` (Read about here: https://ffmpeg.org/about.html).  
To install:  
1. Go to https://ffmpeg.org/download.html
2. Select one of the executable files for windows
3. Save anywhere on your pc. Within the download, you should be able to find the .exe files `ffmpeg.exe` and `ffprobe.exe` (used in the next step)
4. Update `PATH` by running 
  `set PATH=%PATH%;your\path\ffmpeg.exe`
  `set PATH=%PATH%;your\path\ffprobe.exe`
  in cmd, where `your\path` is the path to the executables from step 3. You may have to run as admin.
5. Close cmd for the update to take place

The script also needs `pandas` to run. To install, run `pip install pandas` in cmd

# Before you use
The script makes the following assumptions:  
1. All video files in the folder you choose are to be converted, and are of the same file format
2. All video files contain the same choices for audio and subtitles  

# Usage
0. Backup your data. This script is not thoroughly tested (yet).
1. Place the script in the folder of the files you wish to change the forced audio and subtitles for  
2. Run the script in cmd/terminal using `python script.py`
3. Follow the instructions in the script
