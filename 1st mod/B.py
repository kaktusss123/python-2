num = int(input())
for i in range(1, num):
    if (i % 15 == 0):
        print('Fizz Buzz', end=', ')
    elif (i % 3 == 0):
        print('Fizz', end=', ')
    elif (i % 5 == 0):
        print('Buzz', end=', ')
    else:
        print(i, end=', ')
if (num % 15 == 0):
    print('Fizz Buzz')
elif (num % 3 == 0):
    print('Fizz')
elif (num % 5 == 0):
    print('Buzz')
else:
    print(num)
