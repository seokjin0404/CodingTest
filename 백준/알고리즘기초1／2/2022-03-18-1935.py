N = int(input())
eq = input()
alpha = [int(input()) for i in range(N)]

stack = []
for s in eq:
    if s.isalpha():
        stack.append(alpha[ord(s) - ord('A')])
    elif s == '+':
        stack.append(stack.pop(-2) + stack.pop())
    elif s == '-':
        stack.append(stack.pop(-2) - stack.pop())
    elif s == '*':
        stack.append(stack.pop(-2) * stack.pop())
    else:
        stack.append(stack.pop(-2)/stack.pop())

print(f'{stack.pop():.2f}')