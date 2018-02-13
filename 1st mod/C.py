n = int(input())
count = 0
for i10 in range(n // 10 + 1):
    for i5 in range(n // 5 + 1):
        for i1 in range(n + 1):
            if (i10 * 10 + i5 * 5 + i1 * 1 == n):
                print( str(i10) + '*10 ' + str(i5) + '*5 ' + str(i1) + '*1 == ' + str(n) )
                count += 1
print(count)
