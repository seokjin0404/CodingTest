N = int(input())

# for i in range(N):
#     s = input().split()
#     for word in s:
#         print(word[::-1], end = " ")

for i in range(N):
    s = input().split()
    for word in s:
        stack = list(word)
        for chr in word:
            print(stack.pop(), end = "")
        print(end = " ")