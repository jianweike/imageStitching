# import the necessary packages
import argparse
import imutils
import cv2
import numpy as np
import time
 
DISPLAY_KEYPOINTS = 0
OUTPUT_PATH = './picked_calibration/'

#vidcap1 = cv2.VideoCapture('../data/vidwriter/output1.avi')
#vidcap2 = cv2.VideoCapture('../data/vidwriter/output2.avi')
#vidcap3 = cv2.VideoCapture('../data/vidwriter/output3.avi')
#vidcap4 = cv2.VideoCapture('../data/vidwriter/output4.avi')


vidcap1 = cv2.VideoCapture('../data/7_18_17/calibrationvids/output1.avi')
vidcap2 = cv2.VideoCapture('../data/7_18_17/calibrationvids/output2.avi')
vidcap3 = cv2.VideoCapture('../data/7_18_17/calibrationvids/output3.avi')
vidcap4 = cv2.VideoCapture('../data/7_18_17/calibrationvids/output4.avi')


#vidcap1 = cv2.VideoCapture(1)
#vidcap2 = cv2.VideoCapture(2)
#vidcap3 = cv2.VideoCapture(3)
#vidcap4 = cv2.VideoCapture(4)

if DISPLAY_KEYPOINTS:
    #descriptor = cv2.xfeatures2d.SIFT_create()
    descriptor = cv2.xfeatures2d.SURF_create()


cc = 0
# load the two images and resize them to have a width of 400 pixels
# (for faster processing)
for k in range(0,5):
	success1,image1 = vidcap1.read()
	success2,image2 = vidcap2.read()
	success3,image3 = vidcap3.read()
	success4,image4 = vidcap4.read()

while ((success1 & success2) & (success3 & success4)):
	print "success \n"
	

 
	# stitch the images together to create a panorama
	result1 = np.concatenate((image1,image2),axis=1)
	result2 =np.concatenate((image3,image4),axis=1)
	result = np.concatenate((result1,result2),axis=0)

        if DISPLAY_KEYPOINTS:
            (kps, features) = descriptor.detectAndCompute(result, None)
	
	
            cv2.drawKeypoints(result,kps,result)
	
	# show the images
	cv2.imshow("Result", result)

	if cv2.waitKey(100) & 0xFF == ord('p'):
		print OUTPUT_PATH+'output1.jpg'
		cv2.imwrite(OUTPUT_PATH+'output1/'+str(cc)+'.jpg',image1)
		cv2.imwrite(OUTPUT_PATH+'output2/'+str(cc)+'.jpg',image2)
		cv2.imwrite(OUTPUT_PATH+'output3/'+str(cc)+'.jpg',image3)
		cv2.imwrite(OUTPUT_PATH+'output4/'+str(cc)+'.jpg',image4)

	cc =cc +1
	if cv2.waitKey(100) & 0xFF == ord('q'):
		break
	#cv2.waitKey(0)

	success1,image1 = vidcap1.read()
	success2,image2 = vidcap2.read()
	success3,image3 = vidcap3.read()
	success4,image4 = vidcap4.read()


