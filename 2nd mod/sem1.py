words = input().split(' ')
long = ''
for i in words:
    if len(i) > len(long):
        long = i
print(long.replace('c', 'p'))