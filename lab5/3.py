import re
with open("row.txt", "r", encoding= "utf-8") as row:
    file = row.read()
a = re.findall(r"[a-zа-я]+_[a-zа-я]+" , file)
for i in a:
    print (i, end=" ")