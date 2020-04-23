import re
train_text = "于是我就给[@朱物华#Location*]校长、[@张钟俊#Location*]院长给他们写了一个报告!"
f1 = "C:\\Users\\dell\\Desktop\\plant.txt"


def test(f1, train_text):
    f = open(f1,"a+",encoding="utf-8")
    f.seek(0)
    lst = []
    for line in f.readlines():
        line1 = line.split("\n")

        lst.append(line1[0])


    entityRe = r'\[\@.*?\#.*?\*\](?!\#)'
    for match in re.finditer(entityRe, train_text):
        recognized_entity = train_text[match.span()[0]:match.span()[1]]
        if recognized_entity not in lst:
            print(recognized_entity)
            f.writelines('\n' + recognized_entity)


test(f1,train_text)

