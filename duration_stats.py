'''
Stats for the duration of soundfiles
Author: Ethan Zheng
May 24 2018
'''

import glob
import wave
import contextlib

# Change path to folders where sound files are located like
# /Users/myName/Desktop/myFolder/*.wav
path = '/*.wav'   
files = glob.glob(path)   
for name in files:
    with contextlib.closing(wave.open(name,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        # Change the rounded decimals as needed
        # Here I round it to 3 decimals
        print(round(duration,3))