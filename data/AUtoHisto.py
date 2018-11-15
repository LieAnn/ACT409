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
line = line.split(',')[5:22]
csvfile2.write(','.join(line) + '\n')

AUr = [0] * 17
AUc = [0] * 17

numofframe = 0

for line in csvfile:
    line = line.split(',')
    numofframe = numofframe + 1
    AUv = list(map(float, line[5:22]))
    for idx, value in enumerate(AUv):
        AUr[idx] = AUr[idx] + value
        if value != 0.0:
            AUc[idx] = AUc[idx] + 1

AUr = list(map(str, AUr))
AUc = list(map(str, AUc))

csvfile2.write(','.join(AUr) + '\n');
csvfile2.write(','.join(AUc) + '\n');



csvfile.close()
