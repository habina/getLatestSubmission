from subprocess import call
from os import listdir
from os.path import isfile, join
mypath = "./submission"
for f in listdir(mypath):
    print(f)
    path = mypath + "/" + f + "/MY.PARTNERS"
    call(["sublime", path])
