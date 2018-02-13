import operator

zp = {
    "Mark": 90000000,
    "Vasya": 100,
    "Anton": 16000,
    "Marina": 50000,
    "Goga": 24043,
    "Ivan": 7000,
    "Joji": 4000
}

a = sorted(zp.items(), key=operator.itemgetter(1))
for i in a:
    if (i[1] >= 10000):
        print(i[0] + ' ' + str(i[1]))
