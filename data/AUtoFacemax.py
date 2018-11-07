import sys

csvfilename = sys.argv[1]
csvfile = open(csvfilename,'r')
newfilename = csvfilename[:csvfilename.rfind('.')] + ".FE2.csv"
newfile = open(newfilename,'w')

firstline = csvfile.readline().split(',')
firstline = firstline[:5] + ["FE01","FE02","FE03","FE04","FE05","FE06","FE07\n"]
'''
Happy - 12,25
Sad - 4, 15
Fearful - 1,4,20,25
Angry - 4,7,23
Surprised - 1,25,26
Disgusted - 9,10,17
neutral -- ??
'''
newfile.write(','.join(firstline))

for line in csvfile:
    line = line.split(',')
    if float(line[3]) < 0.9:
        continue
    if int(line[4]) == 0:
        continue
    AUs = list(map(float, line[5:22]))
    # AU num : 1,2,4,5,6,7,9,10,12,14,15,17,20,23,25,26,45
    # index  : 0 1 2 3 4 5 6  7  8  9 10 11 12 13 14 15 16
    FEs = [(AUs[8]+AUs[14])/2.0, (AUs[2] + AUs[10])/2.0, (AUs[0]+AUs[2] + AUs[12] + AUs[14])/4.0,
            (AUs[2] + AUs[5] + AUs[13])/3.0, (AUs[0] + AUs[14] + AUs[15])/3.0, (AUs[6] + AUs[7] + AUs[11])/3.0]

    maxv = 0
    maxi = 0
    for idx, ele in enumerate(FEs):
        if ele > maxv:
            maxv = ele
            maxi = idx

    for i in range(len(FEs)):
        if maxi != i:
            FEs[i] = 0
    
    newline = line[:5] + list(map(str,FEs))
    newfile.write(",".join(newline) + ",0\n")

csvfile.close()
newfile.close()
