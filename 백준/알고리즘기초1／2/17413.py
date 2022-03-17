import sys

S = sys.stdin.readline().rstrip()
in_tag = False

word, answer = "", ""

for s in S:
    if s == '<':
        answer += word[::-1]
        answer += '<'
        in_tag = True
        word = ''
    elif s == '>':
        in_tag = False
        word += s
        answer += word
        word = ''
    elif s == ' ':
        if in_tag:
            word += s
        else:
            answer += word[::-1]
            answer += s
            word = ''
    else:
        word += s

print(answer+word[::-1])
# word를 뒤집어서 더하는 이유는 어짜피 in_tag == True
# 일 때, word = ''이기 때문에, in_tag == False일 때만 고려하면 된다.