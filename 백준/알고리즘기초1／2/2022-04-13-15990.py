T = int(input())
d = [[0]*3 for _ in range(100001)]

d[1] = [1, 0, 0]
d[2] = [0, 1, 0]
d[3] = [1, 1, 1]

for i in range(4,100001):
    for j in range(3):
        d[i][j] = (sum(d[i-j-1]) - d[i-j-1][j])%1000000009

for _ in range(T):
    n = int(input())
    print(sum(d[n])%1000000009)