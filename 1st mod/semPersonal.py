def palindrom(s):
    count_of_one = 0  # количество букв, входящих нечетное число раз
    count_of_letter = 0  # Количество вхождений одной буквы
    letters = set(s)  # Создал множество из букв, чтобы исключить повторяющиеся символы
    if (len(s) % 2 == 0):  # Если длина четная, то должно быть четное количество вхождений каждой буквы
        for i in letters:  # Для каждой буквы из множества
            for k in s:
                if (k == i):  # Если буква из множества и из строки совпадают
                    count_of_letter += 1  # счетчик +1
            if (count_of_letter % 2 != 0):  # После прохода по всей строке
                return 'NO'  # Если существует хотя бы одна буква с нечетным количеством вхождений
            count_of_letter = 0
        return 'YES'
    else:                    # Если неченое, то одна буква может входить нечетное число раз
        for i in letters:
            for k in s:
                if (k == i):
                    count_of_letter += 1
            if (count_of_letter % 2 != 0):
                count_of_one += 1
            count_of_letter = 0
        if (count_of_one > 1):
            return 'NO'
        else:
            return 'YES'


print(palindrom('xoxox'))

# collections count