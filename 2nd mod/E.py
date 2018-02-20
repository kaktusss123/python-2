word = input()
set_of_letters = {}
set_of_letters = set(set_of_letters)
for i in word:
    if i in set_of_letters:
        set_of_letters.remove(i)
    else:
        set_of_letters.add(i)
if len(word) % 2 == 0:
    if len(set_of_letters) > 0:
        print('NO')
    else:
        print('YES')
else:
    if len(set_of_letters) > 1:
        print('NO')
    else:
        print('YES')
