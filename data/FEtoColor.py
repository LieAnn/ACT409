import sys
import numpy

csvfilename = sys.argv[1]
csvfile = open(csvfilename,'r') #FE
csvfilename2 = sys.argv[2]
csvfile2 = open(csvfilename2, 'r') #Clr

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
line = csvfile2.readline()

class LAB:
    def __init__(self, LMean,LStd, AMean,AStd,BMean,BStd):
        self.LMean = LMean
        self.LStd = LStd
        self.AMean = AMean
        self.AStd = AStd
        self.BMean = BMean
        self.BStd = BStd

def shortstr(string):
    if len(string) > 4:
        return string[:4]
    return string


LABs = [LAB(0,0,0,0,0,0)]


for line in csvfile2:
    line = line.split(',')
    line[6] = line[6].strip()
    LABv = list(map(float, line[1:]))
    LABs.append(LAB(LABv[0],LABv[1],LABv[2],LABv[3],LABv[4],LABv[5]))

LSum = [0,0,0,0,0,0]
LStdSum = [0] * 6
ASum = [0] * 6
AStdSum = [0] *6
BSum = [0] * 6
BStdSum = [0] * 6
FESum = [0] * 6

numofframe = 0
for line in csvfile:
    line = line.split(',')
    numofframe = numofframe + 1
    framenum = int(line[0])
    FEs = list(map(float, list(map(shortstr,line[5:11]))))
    if (framenum > len(LABs)):
        break
    curLAB = LABs[framenum]
    FESum = [sum(x) for x in zip(FESum, FEs)]
    tempL = [curLAB.LMean * x for x in FEs]
    LSum = [sum(x) for x in zip(LSum, tempL)]
    tempL = [curLAB.LStd * x for x in FEs]
    LStdSum = [sum(x) for x in zip(LStdSum, tempL)]
    tempA = [curLAB.AMean * x for x in FEs]
    ASum = [sum(x) for x in zip(ASum, tempA)]
    tempA = [curLAB.AStd * x for x in FEs]
    AStdSum = [sum(x) for x in zip(AStdSum, tempA)]
    tempB = [curLAB.BMean * x for x in FEs]
    BSum = [sum(x) for x in zip(BSum, tempB)]
    tempB = [curLAB.BStd * x for x in FEs]
    BStdSum = [sum(x) for x in zip(BStdSum, tempB)]

LMean = numpy.divide(LSum,FESum)
LStd = numpy.divide(LStdSum,FESum)
AMean = numpy.divide(ASum,FESum)
AStd = numpy.divide(AStdSum,FESum)
BMean = numpy.divide(BSum,FESum)
BStd = numpy.divide(BStdSum,FESum)

print(LMean)
print(LStd)
print(AMean)
print(AStd)
print(BMean)
print(BStd)
csvfile.close()
csvfile2.close()
