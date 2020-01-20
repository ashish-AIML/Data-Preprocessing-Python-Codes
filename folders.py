import os
import shutil
import glob

PATH = "M:\\BaiduNetdiskDownload\\CASIA-FASD\\CASIA_faceAntisp\\sample\\spoof\\20\\"


# for folder in os.listdir(dir):
#     # print(each)
#     # videos= glob.glob(dir+folder+'/*.avi')
#     # print(videos)



for file in os.listdir(PATH):
    if file.endswith(".avi"):
        # print(file)
        t1= file.split('.')[0]
        path = os.path.join(PATH, file)
        # print(path)
        # print(file)
        t=file.split('.')[0]
        path1= os.path.join(PATH, t)
        # print(path1)
        # print(t)
        d= os.mkdir(path1)
        if t == t1:
            shutil.move(path, path1)


