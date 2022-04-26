from collections import deque

N,M,K,X = map(int,input().split())

graph = [[] for _ in range(N+1)]
queue = deque()

for _ in range(M):
    A, B = map(int,input().split())
    graph[A].append(B)

distance = [-1] * (N+1)
distance[X] = 0
queue.append(X)

while queue:
    now = queue.popleft()
    for v in graph[now]:
        if distance[v] == -1:
            distance[v] += distance[now]
        queue.append(v)

check = False
for i in range(1,N+1):
    if distance[i] == K:
        print(i)
        check = False

if check == False:
    print(-1)

