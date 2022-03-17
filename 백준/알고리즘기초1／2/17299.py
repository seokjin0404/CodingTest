from collections import deque
from collections import Counter

N = int(input())
A = list(map(int, input().split()))
counter = Counter(A)
NGF = [-1] * N
stack = deque()
stack.append(0)

for i in range(1,N):
    while stack and counter[A[stack[-1]]] < counter[A[i]]:
        NGF[stack.pop()] = A[i]
    stack.append(i)

print(*NGF)