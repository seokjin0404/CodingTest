N = int(input())
d = [[0]*10 for _ in range(101)]
d[1] = [0] + [1] * 9

for i in range(2,101):
    d[i][0] = d[i-1][1]
    for j in range(1,9):
        d[i][j] = d[i-1][j-1] + d[i-1][j+1]
    d[i][9] = d[i-1][8]

print(sum(d[N])%1000000000)