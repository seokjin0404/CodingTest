import sys

bars = sys.stdin.readline().rstrip()
cut, answer = 0, 0

for i,s in enumerate(bars):
    if s == '(':
        cut += 1
    if s == ')':
        if bars[i-1] =='(':
            cut -= 1
            answer += cut
        else:
            cut -= 1
            answer += 1

print(answer)