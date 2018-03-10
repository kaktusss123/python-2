def weakness(s):
    if len(s) < 8:
        return 'weak'
    if s.lower() == s or s.upper() == s:
        return 'weak'
    if s.lower().find('anna') != -1:
        return 'weak'
    has_digit = False
    for i in s:
        if i.isdigit():
            has_digit = True
            break
    if not has_digit:
        return 'weak'
    letters = {}
    letters = set(letters)
    for i in s:
        letters.add(i)
    if len(letters) < 4:
        return 'weak'
    return 'strong'


password = input()
print(weakness(password))
