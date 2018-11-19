# USAGE
# python example.py --source images/ocean_sunset.jpg --target images/ocean_day.jpg

# import the necessary packages
from color_transfer import color_transfer
from color_transfer import image_stats
import numpy as np
import argparse
import cv2


def mid(LAB1, LAB2, atr):
    LABr = [0,0,0,0,0,0]
    for i in range(len(LABr)):
        LABr[i] = LAB1[i] * atr + LAB2[i] * (1-atr)
    return tuple(LABr)

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--source", required = True,
	help = "Path to the source image dir")

ap.add_argument("-t", "--target", required = True,
	help = "Path to the target image")

ap.add_argument("-c", "--csv", required = True, help = "Path to the au csv file");

args = vars(ap.parse_args())

# load the images
targetvid = cv2.VideoCapture(args["target"])
sourceDir = args["source"] 
csvfile = open(args["csv"], 'r')
csvfile.readline()
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
fps = targetvid.get(cv2.CAP_PROP_FPS)
res = (int(targetvid.get(cv2.CAP_PROP_FRAME_WIDTH)), int(targetvid.get(cv2.CAP_PROP_FRAME_HEIGHT)) * 2)
out = cv2.VideoWriter('output.mp4', fourcc, fps, res)

totalFrame = int(targetvid.get(cv2.CAP_PROP_FRAME_COUNT))
angrySrc = cv2.cvtColor(cv2.imread(sourceDir + "angry.jpg"),cv2.COLOR_BGR2LAB).astype("float32")
disgustedSrc = cv2.cvtColor(cv2.imread(sourceDir + "disgusted.jpg"),cv2.COLOR_BGR2LAB).astype("float32")
sadSrc = cv2.cvtColor(cv2.imread(sourceDir + "sad.jpg"),cv2.COLOR_BGR2LAB).astype("float32")
happySrc = cv2.cvtColor(cv2.imread(sourceDir + "happy.jpg"),cv2.COLOR_BGR2LAB).astype("float32")
#surprisedSrc = cv2.cvtColor(cv2.imread(sourceDir + "surprised.jpg"),cv2.COLOR_BGR2LAB).astype("float32")
fearfulSrc = cv2.cvtColor(cv2.imread(sourceDir + "fearful.jpg"),cv2.COLOR_BGR2LAB).astype("float32")

angryStat = image_stats(angrySrc)
disgustedStat = image_stats(disgustedSrc)
fearfulStat = image_stats(fearfulSrc)
happyStat = image_stats(happySrc)
sadStat = image_stats(sadSrc)
#surprisedStat = image_stats(surprisedSrc)


font                   = cv2.FONT_HERSHEY_SIMPLEX
textloc = (10,50)
fontScale              = 0.5
fontColor              = (255,255,255)
lineType               = 2

frameiter = 0
processtimer = 0

curLAB = None

# Iterating through the frames
while (targetvid.isOpened()):
    frameiter += 1
    ret, frame = targetvid.read()
    line = csvfile.readline().strip().split(',');

    if not ret:
        break

    if frameiter > totalFrame:
        break
    
    frameLAB = image_stats(cv2.cvtColor(frame,cv2.COLOR_BGR2LAB).astype("float32"))
    if curLAB is None:
        curLAB = frameLAB

    if len(line) <= 1:
        out.write(frame)
        break

    while frameiter > int(line[0]):
        line = csvfile.readline().strip().split(',');
        if len(line) <= 1:
            break
    if len(line) <= 1:
        out.write(frame)
        break

    if processtimer < ((frameiter / totalFrame) * 100):
        print(str(processtimer) + "% ", end = "", flush = True)
        processtimer += 5

    #get max FE
    FEs = line[1:]
    feidx = 0
    fev = 0
    for idx, fe in enumerate(FEs):
        if fe is not '0':
            feidx = idx
            fev = fe
    if float(fev) <= 0.75:
        feidx = 6
    else:
        fev = str (int(float(fev) / 5 * 100)) + "%"

    #apply color transfer
    transfer = frame

    timepar = 0.97
    framepar = 0.05

    if feidx == 0:
        curLAB = mid(frameLAB, mid(curLAB, happyStat, timepar), framepar)
        cv2.putText(transfer, 'happy : ' + fev, textloc, font, fontScale, fontColor, lineType);
    elif feidx == 1:
        curLAB = mid(frameLAB, mid(curLAB, sadStat, timepar), framepar)
        cv2.putText(transfer, 'sad : ' + fev, textloc, font, fontScale, fontColor, lineType);
    elif feidx == 2:
        curLAB = mid(frameLAB, mid(curLAB, fearfulStat, timepar), framepar)
        cv2.putText(transfer, 'fearful : '  + fev, textloc, font, fontScale, fontColor, lineType);
    elif feidx == 3:
        curLAB = mid(frameLAB, mid(curLAB, angryStat, timepar), framepar)
        cv2.putText(transfer, 'angry : ' + fev , textloc, font, fontScale, fontColor, lineType);
    #elif feidx == 4:
        #curLAB = mid(frameLAB, mid(curLAB, surprisedStat, timepar), 0.1)
        #cv2.putText(transfer, 'surprised : ' + fev, textloc, font, fontScale, fontColor, lineType);
    elif feidx == 5:
        curLAB = mid(frameLAB, mid(curLAB, disgustedStat, timepar), framepar)
        cv2.putText(transfer, 'disgutsed : ' + fev, textloc, font, fontScale, fontColor, lineType);
    elif feidx == 6:
        curLAB = mid(frameLAB, mid(curLAB, frameLAB, timepar), framepar)
        cv2.putText(transfer, 'neutral' , textloc, font, fontScale, fontColor, lineType);

    transfer = color_transfer(curLAB, transfer)

    transfer= np.concatenate((frame, transfer), axis=0)

    out.write(transfer)

print("")

targetvid.release()
out.release()
cv2.destroyAllWindows()
csvfile.close()
