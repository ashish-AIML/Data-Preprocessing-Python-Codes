import argparse
import os

import sys

from transformer import Transformer


def test(folder_path):
    # parser = argparse.ArgumentParser(description="Formatter from ImageNet xml to Darknet text format")
    # parser.add_argument("-xml", help="Relative location of xml files directory", required=True)
    # parser.add_argument("-out", help="Relative location of output txt files directory", default="out")
    # args = parser.parse_args()
    # print(args)
    xml= folder_path 
    out= folder_path
    xml_dir = os.path.join(os.path.dirname(os.path.realpath('__file__')), xml)
    if not os.path.exists(xml_dir):
        print("Provide the correct folder for xml files.")
        sys.exit()

    out_dir = os.path.join(os.path.dirname(os.path.realpath('__file__')), out)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    if not os.access(out_dir, os.W_OK):
        print("%s folder is not writeable.")
        sys.exit()

    transformer = Transformer(xml_dir=xml_dir, out_dir=out_dir)
    transformer.transform()

path = '/media/syed/ubuntu/Mustafa/Bintex-Images-Backup/train/'

files = []
cnt=0
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    print(r)
    test(r)

    # for file in f:
    #     print(r)
    #     cnt+=1
        # print(file)
        # for s in file:
        #     # print(s)
        # if '.xml' in file:
        #     # print(file)
        #     # files.append(os.path.join(r, file))
        #     s = open(r+'/'+file).read()
        #     s = s.replace('2048.0', '2048')
        #     f = open(r+'/'+file, 'w')
        #     f.write(s)
        #     f.close()


# if __name__ == "__main__":
#     main()
