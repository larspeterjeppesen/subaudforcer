import os
import subprocess as sp
import pandas as pd
from io import StringIO

#Get file format
fileformat = input("Input video file format of your files: ")
if (fileformat[0] != '.'):
    fileformat = '.' + fileformat

#Get list of media files to edit
files = [f for f in os.listdir('.') if os.path.isfile(f) and f[-4:] == fileformat]

#Audio selection
cmd = 'ffprobe -loglevel error -select_streams a -show_entries stream=index:stream_tags=language,title -of csv=p=0 "{file}"'.format(file=files[0])
audoutput = sp.getoutput(cmd)
audoutput = pd.read_csv(StringIO(audoutput), names=['number', 'language', 'title'])
audoutput['number'] -= audoutput['number'][0]
print("----- Audio Selection -----")
print(audoutput.to_string(index=False))
aid = input("Input number of desired audio: ")

#Subtitle selection
cmd = 'ffprobe -loglevel error -select_streams s -show_entries stream=index:stream_tags=language,title -of csv=p=0 "{file}"'.format(file=files[0])
suboutput = sp.getoutput(cmd)
suboutput = pd.read_csv(StringIO(suboutput), names=['number', 'language', 'title'])
suboutput['number'] -= suboutput['number'][0]
print('----- Subtitle Selection -----')
print(suboutput.to_string(index=False))
sid = input("Input number of desired subtitle: ")

#Modify forced/default audio/subtitle tracks
cmd = 'ffmpeg -y -i \"{file}\" -map 0 -c copy -disposition:a -default-forced -disposition:a:{aid} default+forced -disposition:s -default-forced -disposition:s:{sid} default+forced \"{file}.out{fileformat}\"'

print('Starting format...')
for f in files:
    f_cmd = cmd.format(file=f, aid = aid, sid = sid, fileformat = fileformat)
    output = sp.getoutput(f_cmd)
    os.chmod(f, 0o777)
    os.remove(f)
    os.rename(f+'.out{fileformat}'.format(fileformat=fileformat), f)
    print('Converted', f)

print('Finished converting all files')
