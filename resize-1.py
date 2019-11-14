from PIL import Image
import os, sys

# path = "/media/syed/ubuntu/Mustafa/Bintex-Images-Backup/resize/client/"
# # dirs = os.listdir( path )
# # print(dirs)
# import glob
# # print(glob.glob(path+dirs[1]+'/*.jpg'))
# # cnt=0
# def resize():
#     for image in os.walk(path):
#         # os.mkdir(folder) 
#         # images=glob.glob(path+img+'/*.png')
#         # for image in images:
#         if os.path.isfile(image):
#             print(image)
#             im = Image.open(image)
#             f, e = os.path.splitext(image)
#             # print(folder)
#             x = f
#             # x=x[73:]
#             folder="/media/syed/ubuntu/Mustafa/Bintex-Images-Backup/resize/client/resize/"
#             print(x)
#             # imResize = im.resize((4000,2588), Image.ANTIALIAS)
#             # imResize.save(folder+'/' +x+ '.png', 'JPEG', quality=90)
#                 # exit()
# resize()

path = "source"
dirs = os.listdir( path )
def resize():
   for item in dirs:
           # print(item)
           if os.path.isfile(path+item):
               im = Image.open(path+item)
               f, e = os.path.splitext(path+item)
#                # print(e)
               imResize = im.resize((4000,2588), Image.ANTIALIAS)
               imResize.save("destination" + item , 'png', quality=90)
resize()