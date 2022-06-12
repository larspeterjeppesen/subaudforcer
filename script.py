import os
import subprocess as sp
import pandas as pd
from io import StringIO

# cmd = 'ffprobe -show_entries stream=index:stream_tags=language,title test.mkv'

files = [f for f in os.listdir('.') if os.path.isfile(f) and f[-4:] == '.mkv']

#Audio
cmd = 'ffprobe -loglevel error -select_streams a -show_entries stream=index:stream_tags=language,title -of csv=p=0 "{file}"'.format(file=files[0])
audoutput = sp.getoutput(cmd)
audoutput = pd.read_csv(StringIO(audoutput), names=['number', 'language', 'title'])
audoutput['number'] -= audoutput['number'][0]
print("----- Audio Selection -----")
print(audoutput.to_string(index=False))
aid = input("Input number of desired audio: ")

#Subtitles
cmd = 'ffprobe -loglevel error -select_streams s -show_entries stream=index:stream_tags=language,title -of csv=p=0 "{file}"'.format(file=files[0])
suboutput = sp.getoutput(cmd)
suboutput = pd.read_csv(StringIO(suboutput), names=['number', 'language', 'title'])
suboutput['number'] -= suboutput['number'][0]
print('----- Subtitle Selection -----')
print(suboutput.to_string(index=False))
sid = input("Input number of desired subtitle: ")


cmd = 'ffmpeg -y -i \"{file}\" -map 0 -c copy -disposition:a -default-forced -disposition:a:{aid} default+forced -disposition:s -default-forced -disposition:s:{sid} default+forced \"{file}.out.mkv\"'

print('Starting format...')
for f in files:
    if (f[-4:] == '.mkv'):
        f_cmd = cmd.format(file=f, aid = aid, sid = sid)
        output = sp.getoutput(f_cmd)
        os.chmod(f, 0o777)
        os.remove(f)
        os.rename(f+'.out.mkv', f)
        print('Converted', f)

print('Finished converting all files')