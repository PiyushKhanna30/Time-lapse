import cv2
import numpy as np
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

cap=cv2.VideoCapture("road_car_view.avi")
name=0

time_within_each_frame = datetime.datetime.now()
if not os.path.exists('images'):
    os.makedirs('images')

while cap.isOpened():
	ret,frame=cap.read()
	if ret:
		frame=rescale(frame,50)
		if(datetime.datetime.now()>=time_within_each_frame):
			time_within_each_frame=datetime.datetime.now()+datetime.timedelta(seconds=.25)
			cv2.imwrite("images/"+str(name)+".jpg",frame)
			name+=1
		cv2.imshow("frame",frame)
		if cv2.waitKey(1)==ord('q'):
			break
	else:
		break

fourcc=cv2.VideoWriter_fourcc(*'XVID')
img=cv2.imread("images/"+str(0)+".jpg")
out=cv2.VideoWriter('my_timelapse_from_video.avi',fourcc,20,(img.shape[1],img.shape[0]))
images_to_video(out,name,True)

out.release()
cap.release()
cv2.destroyAllWindows()