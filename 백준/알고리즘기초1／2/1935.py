N = int(input())
eq = input()
stack = []
for s in eq:
    if s.isalpha():
        num = int(input())
        stack.append(num)
    elif s == '+':
        stack.append(stack.pop(-2) + stack.pop())
    elif s == '-':
        stack.append(stack.pop(-2) - stack.pop())
    elif s == '*':
        stack.append(stack.pop(-2) * stack.pop())
    else:
        stack.append(stack.pop(-2)/stack.pop())

print(f'{stack.pop():.2f}')