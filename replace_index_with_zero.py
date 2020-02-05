import os

path="/home/ozbek/Desktop/text_re_3/"
for f in os.listdir(path):
    with open(os.path.join(path,f), 'r+') as file :
        filedata = file.readlines()
        for x in filedata:
            # print(x[0])
            replaced= x[0].replace(x[0], '0')
            edit= replaced + x[1:]
            # print(edit)
            file.write(edit)
# with open('/home/ozbek/Desktop/text_re_3/00018.txt', "w") as f:
        # for line in f: