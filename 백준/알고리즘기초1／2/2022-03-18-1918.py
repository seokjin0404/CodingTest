eq = input()
stack = []
prior = {"/" : 2, "*" : 2, "+" : 1, "-" : 1, "(" : 0}

for s in eq:
    if s.isalpha():
        print(s, end = "")
    elif s == "(":
        stack.append(s)
    elif s == ")":
        while True:
            operator = stack.pop()
            if operator == "(":
                break
            else:
                print(operator, end = "")
    else:
        while stack and prior[stack[-1]] >= prior[s]:
            print(stack.pop(), end = "")
        stack.append(s)
while stack:
    print(stack.pop(), end = "")
