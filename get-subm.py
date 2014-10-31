from subprocess import call
from os import listdir
from os.path import isfile, join

roster = open("roster_file")
logins = []
#read logins
for line in roster:
    logins.append(line[:len(line) - 1])

#create folder
call(["mkdir", "submission"])
for login in logins:
    call(["get-subm", "proj1-1",login])
    call(["mkdir", "submission/" + login])
    call(["mv", "proj1_1A.txt", "submission/" + login])
    call(["mv", "MY.PARTNERS", "submission/" + login])
roster.close()
#compress submission
# call(["tar", "zcvf", "archive.tar.gz", "submission/"])
