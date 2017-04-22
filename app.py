# import the necessary packages
import numpy as np
import argparse
import cv2
from cv2 import cv
import time

cap = cv2.VideoCapture(0) # Set Capture Device, in case of a USB Webcam try 1, or give -1 to get a list of available devices

# cap.set(3,1280)
# cap.set(4,720)


while(True):
	ret, frame = cap.read()


	output = frame.copy()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	gray = cv2.GaussianBlur(gray,(5,5),0);
	gray = cv2.medianBlur(gray,5)

	gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,3.5)

	kernel = np.ones((2,2), np.uint8)
	gray = cv2.erode(gray,kernel,iterations = 1)

	gray = cv2.dilate(gray,kernel,iterations = 1)

	circles = cv2.HoughCircles(gray, cv.CV_HOUGH_GRADIENT, 1, 200, param1=30, param2=45, minRadius=0, maxRadius=0)

	if circles is not None:
		circles = np.round(circles[0, :]).astype("int")

		for (x, y, r) in circles:
			cv2.circle(output, (x, y), r, (0, 255, 0), 4)
			# cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
			#time.sleep(0.5)
			# print "Column Number: "
			# print x
			# print "Row Number: "
			# print y
			# print "Radius is: "
			# print r

	# Display the resulting frame
	# 	cv2.imshow('gray',gray)
    	cv2.imshow('frame',output)
 	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()