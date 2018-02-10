n = int(input())
count = 0
for i10 in range(n + 1):
    for i5 in range(n + 1):
        for i1 in range(n + 1):
            if (i10 * 10 + i5 * 5 + i1 * 1 == n):
                count += 1
print(count)
