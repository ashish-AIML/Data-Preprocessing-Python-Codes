
import glob
import os
import math
import cv2
array = []
directory_name_to_save = []
path = "/media/syed/ubuntu/ashish/frames_extract/sample/real/"
uni=0
def extracter(path,uni ):
	vidcap = cv2.VideoCapture(path)
	success,image = vidcap.read()
	count = 0
	reset=0
	while success:
		try:
			# save frame as JPEG file      
			success,image = vidcap.read()
			print('Read a new frame: ', success)
			count += 1
			reset +=1
			if(reset ==10):
				cv2.imwrite("/media/syed/ubuntu/ashish/frames_extract/sample/frames_real/"+str(uni)+"_frame%d.jpg"% count, image)
				reset=0
		except Exception as e:
			break

for folder in os.listdir(path):
	print("*******************")
	print(folder)
	sub_dir= os.path.join(path, folder)
	
	for sub in os.listdir(sub_dir):
		uni +=1
		full_path=path+folder+'/'+sub
		for file in os.listdir(full_path):
			print(full_path+"/"+file)
			extracter(full_path+"/"+file,uni)

