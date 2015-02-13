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
            string = ""
            for i in range(2, len(data)):
                string += data[i] + " "
            out += name + " place_holder " + string + "\n"

        output.write(out)
roster.close()
output.close()
