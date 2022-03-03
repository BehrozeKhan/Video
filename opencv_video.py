import numpy as ny
import cv2

print("Video Capture in Opencv Python")
cap = cv2.VideoCapture(0)
while(True):
	retina,frame = cap.read()
	frame = cv2.resize(frame,(0,0), fx = 0.50, fy = 0.75)
	cv2.imshow("Frame Window", frame)

	ch = cv2.waitKey(3)
	if ch == ord('b'):
		break
cap.release()
cv2.destroyAllWindows()
