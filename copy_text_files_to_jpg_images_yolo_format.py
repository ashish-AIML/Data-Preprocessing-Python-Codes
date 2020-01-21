import os
import glob
import numpy as np
from collections import Counter 
# one = []
# array_numbers = []
# x = os.chdir('/media/syed/ubuntu/ashish/frames_extract/sample/frames_real/')
# for txt_images in glob.glob("*.txt"):
# 	array_numbers.append(txt_images)
# 	# txt_many_images = int(txt_images.split('_')[0])
# 	# print(txt_images)


# # print(array_numbers)


# count = 0 
# for z in range(1,61):
# 	for x in array_numbers:
# 		# print(x)
# 		number = x.split('_')[0]
# 		print('*******************')
# 		print(z)
# 		print(number)
# 		print('*************')
		# if z == number:
		# 	count = count + 1
		# 	print(count)



# temp_array = []
# print(array_numbers)
# n= np.asarray(array_numbers)
# x= np.sort(n)
# # print(x)
# length_numbers = []
# d = Counter(x)
# count = 1
# for i in x:
# 	count = count + 1
# 	if i != count:
# 		length_numbers.append(d[i])
# 		print('{} has occurred {} times'.format(i, d[i])) 
# 	else:
# 		pass



# print(len(length_numbers))


# set_vale = set(length_numbers)
# print(length_numbers)









# txt_values = []
# for x in range(1,61):	# f= open('/media/syed/ubuntu/ashish/frames_extract/sample/frames_real/' + str(name_txt) + ".txt" , "w")
# 	img = ("/media/syed/ubuntu/ashish/frames_extract/sample/labelled_images/real_full_part/" +str(x)+ "_frame90.txt")
# 	text_lable= open(img, 'r')
# 	text_copy= text_lable.read() 
# 	# print(img)
# 	txt_values.append(text_copy)
# print(len(txt_values))

from shutil import copyfile
x = os.chdir('/media/syed/ubuntu/ashish/frames_extract/sample/dataset/frames_spoof/')
for txt_images in glob.glob("*.jpg"):
	fID = txt_images.split('_')[0]
	# print(fID)
	txtname = txt_images.split(".")[0]
	if int(fID) <= 60:
		copyfile('/media/syed/ubuntu/ashish/frames_extract/sample/dataset/labelled_images/spoof_part_1/'+str(fID)+'_frame50.txt', '/media/syed/ubuntu/ashish/frames_extract/sample/dataset/copyed/fake/1/'+txtname+'.txt')
	elif int(fID) >60 and int(fID) <= 120:
		copyfile('/media/syed/ubuntu/ashish/frames_extract/sample/dataset/labelled_images/spoof_part_2/'+str(fID)+'_frame50.txt', '/media/syed/ubuntu/ashish/frames_extract/sample/dataset/copyed/fake/2/'+txtname+'.txt')
	elif int(fID) > 120:
		copyfile('/media/syed/ubuntu/ashish/frames_extract/sample/dataset/labelled_images/spoof_part_3/'+str(fID)+'_frame50.txt', '/media/syed/ubuntu/ashish/frames_extract/sample/dataset/copyed/fake/3/'+txtname+'.txt')
	# print(txtname)
	# if not os.path.exists("/media/syed/ubuntu/ashish/frames_extract/sample/dataset/copyed/real/"+str(fID)):
	# 	os.makedirs("/media/syed/ubuntu/ashish/frames_extract/sample/dataset/copyed/real/"+str(fID))
	# for i in range(51):