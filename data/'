import sys

csvfilename = sys.argv[1]
csvfile = open(csvfilename,'r')
newfilename = csvfilename[:csvfilename.rfind('.')] + "_FE.csv"
newfile = open(newfilename,'w')

firstline = ["frame","FE01","FE02","FE03","FE04","FE05","FE06\n"]
'''
OUT OF DATE
Happy - 12,25
Sad - 4, 15
Fearful - 1,4,20,25
Angry - 4,7,23
Surprised - 1,25,26 - **deleted**
Disgusted - 9,10,17
neutral -- ??
'''
newfile.write(','.join(firstline))


class FErecord:
    def __init__ (self, frame, FEs):
        self.frame = frame
        self.FEs = FEs

FErecs = []

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
    FEs = [AUs[4] * 0.2 + AUs[8] * 0.5 + AUs[14] * 0.3,
            AUs[0] * 0.2 + AUs[2] * 0.3 + AUs[4] * 0.1 + AUs[10] * 0.1 + AUs[11] * 0.3,
            AUs[0] * 0.1 + AUs[1] * 0.2 +AUs[2] * 0.1 + AUs[3] * 0.2+ AUs[12]  * 0.2 + AUs[14] * 0.2,
            AUs[2] * 0.4 + AUs[5] * 0.3 +  AUs[11] * 0.3,
            0, #(AUs[0] + AUs[14] + AUs[15])/3.0,
            (AUs[6] + AUs[7] + AUs[11])/3.0]

    frame = int(line[0])
    FErecs.append(FErecord(frame,FEs))

for idx, rec in enumerate(FErecs):
    frame = rec.frame
    curFEs = rec.FEs
    
    newfile.write(",".join(list(map(str,[frame] + curFEs))) + "\n") 


csvfile.close()
newfile.close()
