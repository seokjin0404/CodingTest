S = input()
stack = []
for i in range(len(S)):
    stack.append(S[i:])
print(*sorted(stack), sep = '\n')