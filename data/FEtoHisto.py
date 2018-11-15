import sys
import numpy

csvfilename = sys.argv[1]
csvfile = open(csvfilename,'r') #FE
csvfile2 = open(csvfilename[:csvfilename.rfind('.')] + "_histo.csv", 'w')

'''
Happy - 12,25
Sad - 4, 15
Fearful - 1,4,20,25
Angry - 4,7,23
Surprised - 1,25,26
Disgusted - 9,10,17
neutral -- ??
'''

line = csvfile.readline()
line = line.split(',')[5:11]
csvfile2.write(','.join(line) + '\n')

FEr = [0] * 6
FEc = [0] * 6

numofframe = 0

for line in csvfile:
    line = line.split(',')
    numofframe = numofframe + 1
    FEv = list(map(float, line[5:11]))
    for idx, value in enumerate(FEv):
        FEr[idx] = FEr[idx] + value
        if value != 0.0:
            FEc[idx] = FEc[idx] + 1

FEr = list(map(str, FEr))
FEc = list(map(str, FEc))

csvfile2.write(','.join(FEr) + '\n');
csvfile2.write(','.join(FEc) + '\n');



csvfile.close()
