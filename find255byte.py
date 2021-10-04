from os import listdir
from os.path import isfile, join
mypath = "./"

files = listdir(mypath)

for f in files:
  fullpath = join(mypath, f)
  if isfile(fullpath):
    if len(f.encode('utf-8')) > 255:
        print(f)