import sys

N, K = map(int, sys.stdin.readline().split())

answer = []
people = [str(i+1) for i in range(N)]
idx = 0
for i in range(N):
    idx += K - 1
    if idx >= len(people):
        idx %= len(people)
    answer.append(people.pop(idx))

print("<" + ", ".join(answer) + ">")