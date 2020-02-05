
import os

filename=[]
path="/home/ozbek/Desktop/txt_files/"
for file in os.listdir(path):
    
    with open(os.path.join(path,file), "r") as f:
        lines = f.readlines()
        
        # 
        if len(lines) == 0:
            print(file)
            os.remove(os.path.join(path,file))
                    

                    