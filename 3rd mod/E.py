old = input()
new = ''
for i in old:
    if i == 'A':
        new += 'T'
    elif i == 'G':
        new += 'C'
    elif i == 'T':
        new += 'A'
    else:
        new += 'G'
print(new[::-1])
