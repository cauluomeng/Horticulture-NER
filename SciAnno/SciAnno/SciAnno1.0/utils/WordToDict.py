
f1 = "C:\\Users\\dell\\Desktop\\plant.txt"

def WordToDict(f1):
    f = open(f1,"r+",encoding="utf-8")
    f.seek(0)
    lst = []
    for line in f.readlines():
        line1 = line.split("\n")
        lst.append(line1[0])
        #print(lst)
        for i in range(len(lst)):
            s1 = str(lst[i])
            s2 = s1.rstrip()
            s = s2.replace(s2,'[@'+s2+'#Plant*]')
            print(s)
        f.writelines('\n' +s)

WordToDict(f1)

