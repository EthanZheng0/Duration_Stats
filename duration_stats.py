'''
Stats for the duration of soundfiles
Author: Ethan Zheng
May 24 2018
'''

import glob
import wave
import contextlib

files = glob.glob('*.wav')
files.sort()
listDuration = []
for name in files:
        print(name)
        with contextlib.closing(wave.open(name,'r')) as f:
                frames = f.getnframes()
                rate = f.getframerate()
                duration = frames / float(rate)

                # Change the rounded decimals as needed
                # Here I round it to 3 decimals
                l = [name, round(duration,3)]
                listDuration.append(l)

fileName = "_duration.txt"
print("\nDuration data output as " + fileName)
fileOutput = open(fileName, 'w')
for i in range(len(listDuration)):
        for j in range(len(listDuration[i])):
                fileOutput.write(str(listDuration[i][j]) + '\t')
        fileOutput.write('\r')
