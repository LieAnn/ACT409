# USAGE
# python example.py --source images/ocean_sunset.jpg --target images/ocean_day.jpg

# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()

ap.add_argument("-t", "--target", required = True,
	help = "Path to the target image")

ap.add_argument("-s", "--sec", required = True, help = "cut from given sec to + 10s");

args = vars(ap.parse_args())

# load the images
targetvid = cv2.VideoCapture(args["target"])
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
fps = targetvid.get(cv2.CAP_PROP_FPS)
res = (int(targetvid.get(cv2.CAP_PROP_FRAME_WIDTH)), int(targetvid.get(cv2.CAP_PROP_FRAME_HEIGHT)))
out = cv2.VideoWriter('short.mp4', fourcc, fps, res)


sec = int(args["sec"]);

totalFrame = fps * (sec+10);

frameiter = 0
processtimer = 0

while (targetvid.isOpened()):
    frameiter += 1
    ret, frame = targetvid.read()
    
    if frameiter < (totalFrame * sec / (sec+10)):
        continue

    if not ret:
        break

    if frameiter > totalFrame:
        break

    if processtimer < ((frameiter / totalFrame) * 100):
        print(str(processtimer) + "% ", end = "")
        processtimer += 5

    out.write(frame)

print("")

targetvid.release()
out.release()
cv2.destroyAllWindows()
