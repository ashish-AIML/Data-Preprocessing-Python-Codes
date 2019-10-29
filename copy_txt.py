from PIL import Image
import os, sys
import shutil

path = "/media/syed/ubuntu/Mustafa/Bintex-Images-Backup/new-72-original/"
dirs = os.listdir( path )
# print(dirs)
import glob
# print(glob.glob(path+dirs[1]+'/*.jpg'))
cnt=0
def resize():
    for folder in dirs:
        # os.mkdir(folder) 
        images=glob.glob(path+folder+'/*.txt')
        # print(images)
        for image in images:
            # print("***********"+image)
            if os.path.isfile(image):
                print(image)
                print("********************")
                # im = Image.open(image)
                # f, e = os.path.splitext(image)
                # print(folder)
                x = image
                x=x[78:]
                print(x)
                shutil.copy(image, "/media/syed/ubuntu/Mustafa/Bintex-Images-Backup/416_resized/"+folder+'/'+x)
                # imResize = im.resize((200,158), Image.ANTIALIAS)
                # imResize.save(folder+'/' +x+ '.jpg', 'JPEG', quality=90)
                # exit()
resize()
