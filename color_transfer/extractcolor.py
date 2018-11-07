# USAGE
# python example.py --source images/ocean_sunset.jpg --target images/ocean_day.jpg

# import the necessary packages
import numpy as np
import cv2
import sys

def image_stats(image):
	"""
	Parameters:
	-------
	image: NumPy array
		OpenCV image in L*a*b* color space

	Returns:
	-------
	Tuple of mean and standard deviations for the L*, a*, and b*
	channels, respectively
	"""
	# compute the mean and standard deviation of each channel
	(l, a, b) = cv2.split(image)
	(lMean, lStd) = (l.mean(), l.std())
	(aMean, aStd) = (a.mean(), a.std())
	(bMean, bStd) = (b.mean(), b.std())

	# return the color statistics
	return [lMean, lStd, aMean, aStd, bMean, bStd]


video = sys.argv[1]
cap = cv2.VideoCapture(video)

csvfilename = video[:video.rfind('.')] + ".csv"

csvfile = open(csvfilename, 'w')

csvfile.write("frame,LMean,LStd,AMean,AStd,BMean,BStd\n");

framenum = 1
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
progress = 0

while (1):
    ret, frame = cap.read()

    labframe = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

    labstats = list(map(str, image_stats(labframe)))

    csvline = str(framenum) + "," + ",".join(labstats) + "\n";

    csvfile.write(csvline)

    framenum = framenum + 1
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

    if int(100 * framenum / length) > progress:
        progress = progress + 10
        print(str(progress) + "% ")

    if framenum == length:
        break

cap.release()
cv2.destroyAllWindows()
