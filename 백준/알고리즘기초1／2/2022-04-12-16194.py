N = int(input())

d = [10000001] * (N+1)
P = [0] + list(map(int,input().split()))
d[0] = 0

for i in range(1,N+1):
    for j in range(1,i+1):
        d[i] = min(d[i],d[i-j]+P[j])
print(d[N])