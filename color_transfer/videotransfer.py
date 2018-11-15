# USAGE
# python example.py --source images/ocean_sunset.jpg --target images/ocean_day.jpg

# import the necessary packages
from color_transfer import color_transfer
import numpy as np
import argparse
import cv2

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
res = (int(targetvid.get(cv2.CAP_PROP_FRAME_WIDTH)), int(targetvid.get(cv2.CAP_PROP_FRAME_HEIGHT)))
out = cv2.VideoWriter('output.mp4', fourcc, fps, res)

totalFrame = int(targetvid.get(cv2.CAP_PROP_FRAME_COUNT))
angrySrc = cv2.imread(sourceDir + "angry.jpg")
disgustedSrc = cv2.imread(sourceDir + "disgusted.jpg")
fearfulSrc = cv2.imread(sourceDir + "fearful.jpg")
happySrc = cv2.imread(sourceDir + "happy.jpg")
sadSrc = cv2.imread (sourceDir + "sad.jpg")
surprisedSrc = cv2.imread (sourceDir + "surprised.jpg")

font                   = cv2.FONT_HERSHEY_SIMPLEX
textloc = (10,50)
fontScale              = 1
fontColor              = (0,0,0)
lineType               = 2

frameiter = 0
processtimer = 0

# Iterating through the frames
while (targetvid.isOpened()):
    frameiter += 1
    ret, frame = targetvid.read()
    line = csvfile.readline().strip().split(',');

    if not ret:
        break

    if frameiter > totalFrame:
        break

    if len(line) <= 1:
        break

    while frameiter > int(line[0]):
        line = csvfile.readline().strip().split(',');
        if len(line) <= 1:
            break
    if len(line) <= 1:
        break

    if processtimer < ((frameiter / totalFrame) * 100):
        print(str(processtimer) + "% ", end = "", flush = True)
        processtimer += 5

    FEs = line[5:11]
    feidx = 0;
    fev = 0;
    for idx, fe in enumerate(FEs):
        if fe is not '0':
            feidx = idx
            fev = fe
    fev = str (int(float(fev) / 5 * 100)) + "%"

    if feidx == 0:
        transfer = color_transfer(happySrc, frame)
        cv2.putText(transfer, 'happy : ' + fev, textloc, font, fontScale, fontColor, lineType);
    elif feidx == 1:
        transfer = color_transfer(sadSrc,frame)
        cv2.putText(transfer, 'sad : ' + fev, textloc, font, fontScale, fontColor, lineType);
    elif feidx == 2:
        transfer = color_transfer(fearfulSrc,frame)
        cv2.putText(transfer, 'fearful : '  + fev, textloc, font, fontScale, fontColor, lineType);
    elif feidx == 3:
        transfer = color_transfer(angrySrc,frame)
        cv2.putText(transfer, 'angry : ' + fev , textloc, font, fontScale, fontColor, lineType);
    elif feidx == 4:
        transfer = color_transfer(surprisedSrc,frame)
        cv2.putText(transfer, 'surprised : ' + fev, textloc, font, fontScale, fontColor, lineType);
    elif feidx == 5:
        transfer = color_transfer(disgustedSrc,frame)
        cv2.putText(transfer, 'disgutsed : ' + fev, textloc, font, fontScale, fontColor, lineType);
    else:
        transfer = frame

    out.write(transfer)

print("")

targetvid.release()
out.release()
cv2.destroyAllWindows()
csvfile.close()
