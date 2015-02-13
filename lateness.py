from subprocess import call
from os import listdir
from os.path import isfile, join

f = open("./late_roster")
my_f = open("./roster_login_only")


logins = f.readlines()
lst = []
for line in logins:
  if "cs61c" in line:
    lst.append(line[:len(line)-2])

my_logins = my_f.readlines()
lst2 = []
for line in my_logins:
  lst2.append(line[:len(line)-2])
print(lst2)
lst3 = []
for item in lst:
  if item in lst2:
    lst3.append(item)
print(lst3)