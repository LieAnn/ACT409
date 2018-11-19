import sys

csvfilename = sys.argv[1]
csvfile = open(csvfilename,'r')
newfilename = csvfilename[:csvfilename.rfind('.')] + "_FE2.csv"
newfile = open(newfilename,'w')

firstline = ["frame","FE01","FE02","FE03","FE04","FE05","FE06\n"]
'''
Happy - 12,25
Sad - 4, 15
Fearful - 1,4,20,25
Angry - 4,7,23
Surprised - 1,25,26 - deleted
Disgusted - 9,10,17
neutral -- ??
'''
newfile.write(','.join(firstline))


class FErecord:
    def __init__ (self, frame, FEs):
        self.frame = frame
        self.FEs = FEs

FErecs = []
maxidx = []

csvfile.readline()
for line in csvfile:
    line = line.split(',')
    if float(line[3]) < 0.9:
        continue
    if int(line[4]) == 0:
        continue
    AUs = list(map(float, line[5:22]))
    # AU num : 1,2,4,5,6,7,9,10,12,14,15,17,20,23,25,26,45
    # index  : 0 1 2 3 4 5 6  7  8  9 10 11 12 13 14 15 16
    FEs = [AUs[4] * 0.4 + AUs[8] * 0.3 + AUs[14] * 0.3,
            (AUs[2] + AUs[10])/2.0,
            (AUs[0]+AUs[2] + AUs[12] + AUs[14])/4.0,
            (AUs[2] + AUs[5] + AUs[13])/3.0,
            0,#(AUs[0] + AUs[14] + AUs[15])/3.0,
            (AUs[6] + AUs[7] + AUs[11])/3.0]

    frame = int(line[0])
    FErecs.append(FErecord(frame,FEs))
    #get only max value
    maxv = 0
    maxi = 0
    for idx, ele in enumerate(FEs):
        if ele > maxv:
            maxv = ele
            maxi = idx

    maxidx.append(maxi)

domFE = maxidx[0]
domcount = 0
for idx, maxvs in enumerate(maxidx):
    if domFE == maxvs:
        domcount = domcount + 1
    else:
        if domcount < 4:
            for idx2 in range(domcount):
                tmpFEs = FErecs[idx-idx2-1].FEs
                tmpFEs[domFE] = 0
                FErecs[idx-idx2-1].FEs = tmpFEs
        domcount = 1
        domFE = maxvs

for idx, rec in enumerate(FErecs):
    frame = rec.frame
    curFEs = rec.FEs
    maxv = 0
    maxi = 0
    for idx, ele in enumerate(curFEs):
        if ele > maxv:
            maxv = ele
            maxi = idx

    for idx in range(len(curFEs)):
        if idx != maxi:
            curFEs[idx] = 0

    
    newfile.write(",".join(list(map(str,[frame] + curFEs))) + "\n") 


csvfile.close()
newfile.close()
