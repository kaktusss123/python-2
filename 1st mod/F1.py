n = input()
beg = int(n[0]) + int(n[1]) + int(n[2])
n = int(n)
nc = n
i = 2
while (nc % 10) + (nc % 100 // 10) + (nc % 1000 // 100) != \
        (nc // 100000) + (nc // 10000 % 10) + (nc // 1000 % 10):
    nc = n
    nc += (i // 2) * ((-1) ** i)
    i += 1
print(nc)
