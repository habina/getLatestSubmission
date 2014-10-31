from subprocess import call
from os import listdir
from os.path import isfile, join

roster = open("roster_file", "r")
output = open("output", "w")
#read logins
logins = roster.readlines()
for info in logins:
    data = info.split()
    path = "submission/" + data[0] + "/MY.PARTNERS"
    partner = open(path)
    for line in partner:
        pair_login = line.split()
        out = ""
        for name in pair_login:
            out += name + " place_holder " + data[2] + "\n"
        output.write(out)
# print(logins)
roster.close()
output.close()
# for line in roster:
#     print(line)

#create folder
# call(["mkdir", "submission"])
# for login in logins:
#     call(["get-subm", "proj1-1",login])
#     call(["mkdir", "submission/" + login])
#     call(["mv", "proj1_1A.txt", "submission/" + login])
#     call(["mv", "MY.PARTNERS", "submission/" + login])
#compress submission
# call(["tar", "zcvf", "archive.tar.gz", "submission/"])
