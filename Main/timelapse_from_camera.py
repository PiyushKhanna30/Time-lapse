import cv2
import numpy as np
import time
import os
import datetime
import shutil


def rescale(frame,percent=30):
	(h,w,c)=frame.shape
	dim=(int(w*percent/100) ,int(h*percent/100))
	return cv2.resize(frame,dim)

def images_to_video(out,name,delete_images=True):
	for i in range (name):
		img=cv2.imread("images/"+str(i)+".jpg")
		out.write(img)
	if delete_images:
		for i in range (name):
			os.remove("images/"+str(i)+".jpg")
		shutil.rmtree("images/")

cap=cv2.VideoCapture(0)
name=0

seconds_duration = 60
now=datetime.datetime.now()
finish_time = now + datetime.timedelta(seconds=seconds_duration)#used for calculating differences in dates and also can be used for date manipulations 

if not os.path.exists('images'):
    os.makedirs('images')

while datetime.datetime.now() < finish_time:
	_,frame=cap.read()
	frame=rescale(frame,50)
	cv2.imwrite("images/"+str(name)+".jpg",frame)
	name+=1
	time.sleep(.25)
	if cv2.waitKey(1)==ord('q'):
		break

fourcc=cv2.VideoWriter_fourcc(*'XVID')
img=cv2.imread("images/"+str(0)+".jpg")
out=cv2.VideoWriter('my_timelapse.avi',fourcc,20,(img.shape[1],img.shape[0]))
images_to_video(out,name,True)


out.release()
cap.release()
cv2.destroyAllWindows()