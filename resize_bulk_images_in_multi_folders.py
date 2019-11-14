from PIL import Image
import os, sys

path = "/media/syed/ubuntu/Mustafa/Bintex-Images-Backup/new-72-original/"
dirs = os.listdir( path )
# print(dirs)
import glob
# print(glob.glob(path+dirs[1]+'/*.jpg'))
cnt=0
def resize():
    for folder in dirs:
        os.mkdir(folder) 
        images=glob.glob(path+folder+'/*.jpg')
        print("********************")
        for image in images:
            # print("***********"+image)
            if os.path.isfile(image):
                im = Image.open(image)
                f, e = os.path.splitext(image)
                # print(folder)
                x = f
                x=x[78:]
                print(x)
                imResize = im.resize((416,329), Image.ANTIALIAS)
                imResize.save(folder+'/' +x+ '.jpg', 'JPEG', quality=90)
                # exit()
resize()
