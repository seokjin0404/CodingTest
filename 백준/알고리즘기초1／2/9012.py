N = int(input())

for _ in range(N):
    stack = []
    PS = input()
    for s in PS:
        if s == '(':
            stack.append(s)
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if stack:
            print("NO")
        else:
            print("YES")