#delete file
import os
import os.path

fname=input("enter file name")
if os.path.exists(fname):
    if os.path.isfile(fname):
        os.remove(fname)
    else:
        print("this is a folder")
else:
    print("file is not exist")
