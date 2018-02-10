n = int(input())
lastlast = 0
last = 1
if (n == 0):
    print(lastlast)
elif (n == 1):
    print(last)
else:
    for i in range(1, n):
        newNum = last + lastlast
        lastlast = last
        last = newNum
    print(last)
