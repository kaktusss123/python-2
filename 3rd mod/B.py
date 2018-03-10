def is_palindrom(s):
    for i in range(len(s)):
        if s[i] != s[-i - 1]:
            return False
    return True


if __name__ == '__main__':
    s = input()
    found = False
    for i in range(len(s) - 1):
        if is_palindrom(s[i:]) or is_palindrom(s[:len(s) - i]):
            print(i)
            found = True
            break

    if not found:
        print(len(s) - 1)
