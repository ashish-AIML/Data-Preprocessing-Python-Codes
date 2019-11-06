
import os

path = '/media/syed/ubuntu/Mustafa/Bintex-Images-Backup/train/'

files = []
cnt=0
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    # print(r)


    for file in f:
        print(r)
        cnt+=1
        # print(file)
        # for s in file:
        #     # print(s)
        if '.xml' in file:
            # print(file)
            # files.append(os.path.join(r, file))
            s = open(r+'/'+file).read()
            s = s.replace('2048.0', '2048')
            f = open(r+'/'+file, 'w')
            f.write(s)
            f.close()

# for f in files:
#     print(f)