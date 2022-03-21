S = input()

for c in S:
    if c.islower():
        print(chr(ord('a') +(ord(c) - ord('a') + 13)%26), end = "")
    elif c.isupper():
        print(chr(ord('A') + (ord(c) - ord('A') + 13)%26), end = "")
    else:
        print(c, end = "")