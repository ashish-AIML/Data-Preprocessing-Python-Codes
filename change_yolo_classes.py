from PIL import Image
import os, sys
import shutil

path = "/media/syed/ubuntu/Mustafa/Bintex-Images-Backup/416_resized/"
dirs = os.listdir( path )
# print(dirs)
import glob
# print(glob.glob(path+dirs[1]+'/*.jpg'))
def resize():
    cnt=0
    for folder in dirs:
        # os.mkdir(folder) 
        images=glob.glob(path+folder+'/*.txt')
        print(cnt)
        print("********************")
        c = open("classes.txt", "a")
        c.write(folder+'\n')
        # print(images)
        # print(cnt)
        for image in images:
            print("***********"+image)
            if os.path.isfile(image):
                r= open(image, 'r') 
                data = r.read().replace('\n', '')
                print("********************")
                s2 = data.split(' ', 1)[1]
                print(s2)
                s2=str(cnt) + " "+s2
                f = open(image, "w")
                f.write(s2)
                f.close()
        cnt=cnt+1
                

                # print(image)
                # exit()
                # im = Image.open(image)
                # f, e = os.path.splitext(image)
                # print(folder)
                # x = image
                # x=x[78:]
                # print(x)
                # shutil.copy(image, "/media/syed/ubuntu/Mustafa/Bintex-Images-Backup/new-72/"+folder+'/'+x)
                # imResize = im.resize((200,158), Image.ANTIALIAS)
                # imResize.save(folder+'/' +x+ '.jpg', 'JPEG', quality=90)
                # exit()
resize()
