import sys

input = sys.stdin.readline
Left = list(input().rstrip())
Right = []
N = int(input())

for i in range(N):
    command = input().split()
    if command[0] == 'L':
        if Left:
            Right.append(Left.pop())
        else:
            continue
    elif command[0] == 'D':
        if Right:
            Left.append(Right.pop())
        else:
            continue
    elif command[0] == 'B':
        if Left:
            Left.pop()
        else:
            continue
    else:
        Left.append(command[1])

print("".join(Left + list(reversed(Right))))