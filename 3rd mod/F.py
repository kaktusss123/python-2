import fileinput


def wc(a, f):
    if a == '-m':
        counter = 0
        for i in f:
            counter += len(i)
        # counter += len(f)
        return counter
    elif a == '-l':
        return len(f)
    elif a == '-L':
        max = 0
        for i in f:
            if (len(i) - 1 > max):
                max = len(i) - 1
        return max
    elif a == '-w':
        counter = 0
        for i in f:
            tmp = i.split()
            counter += len(tmp)
        return counter

if __name__ == '__main__':

    args = input().split(' ')
    f = []
    for line in fileinput.input():
        f.append(line)
    my_args = ['-l', '-w', '-m', '-L']
    for i in my_args:
        if i in args:
            print(wc(i, f), end=' ')
