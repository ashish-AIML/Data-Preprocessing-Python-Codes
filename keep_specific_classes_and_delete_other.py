
import os




filename=[]
path="/home/ozbek/Desktop/text_re_3/"
for file in os.listdir(path):
    # print(file)
    # filename.append(file)
    # for each in filename:
        # print(type(each))
    with open(os.path.join(path,file), "r") as f:
        lines = f.readlines()
        # print(lines)
            # print(lines)
        with open(os.path.join(path,file), "w") as f:
            for line in lines:
                if line.startswith("0"):
                    f.write(line)
    
