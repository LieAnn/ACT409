# USAGE
# python example.py --source images/ocean_sunset.jpg --target images/ocean_day.jpg

# import the necessary packages
from color_transfer import color_transfer
import numpy as np
import argparse
import cv2

def show_image(title, image, width = 300):
	# resize the image to have a constant width, just to
	# make displaying the images take up less screen real
	# estate
	r = width / float(image.shape[1])
	dim = (width, int(image.shape[0] * r))
	resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

	# show the resized image
	cv2.imshow(title, resized)

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--source", required = True,
	help = "Path to the source image dir")

ap.add_argument("-t", "--target", required = True,
	help = "Path to the target image")

args = vars(ap.parse_args())

# load the images
targetvid = cv2.VideoCapture(args["target"])
sourceDir = args["source"] 
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
fps = targetvid.get(cv2.CAP_PROP_FPS)
res = (int(targetvid.get(cv2.CAP_PROP_FRAME_WIDTH)), int(targetvid.get(cv2.CAP_PROP_FRAME_HEIGHT)))
out = cv2.VideoWriter('output.mp4', fourcc, fps, res)

#totalFrame = int(targetvid.get(cv2.CAP_PROP_FRAME_COUNT))
totalFrame = int(fps) * 12
angrySrc = cv2.imread(sourceDir + "angry.jpg")
disgustedSrc = cv2.imread(sourceDir + "disgusted.jpg")
fearfulSrc = cv2.imread(sourceDir + "fearful.jpg")
happySrc = cv2.imread(sourceDir + "happy.jpg")
sadSrc = cv2.imread (sourceDir + "sad.jpg")
surprisedSrc = cv2.imread (sourceDir + "surprised.jpg")

frameiter = 0
processtimer = 0

while (targetvid.isOpened()):
    frameiter += 1
    ret, frame = targetvid.read()

    if not ret:
        break

    if frameiter > totalFrame:
        break

    if processtimer < ((frameiter / totalFrame) * 100):
        print(str(processtimer) + "%")
        processtimer += 5

    if frameiter < (totalFrame / 6):
        transfer = color_transfer(angrySrc, frame)
    elif frameiter < (totalFrame / 6 * 2):
        transfer = color_transfer(disgustedSrc, frame)
    elif frameiter < (totalFrame / 6 * 3):
        transfer = color_transfer(fearfulSrc, frame)
    elif frameiter < (totalFrame / 6 * 4):
        transfer = color_transfer(happySrc, frame)
    elif frameiter < (totalFrame / 6 * 5):
        transfer = color_transfer(sadSrc, frame)
    else:
        transfer = color_transfer(surprisedSrc, frame)
    out.write(transfer)

targetvid.release()
out.release()
cv2.destroyAllWindows()
