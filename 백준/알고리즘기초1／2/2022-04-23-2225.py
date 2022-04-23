N,K = map(int,input().split())

dp = [[0,i] + [0]*(N-1) for i in range(K+1)]
dp[1] = [1]*(N+1)

for i in range(2,K+1):
    for j in range(2, N+1):
        dp[i][j] =dp[i][j-1] + dp[i-1][j]

print(dp[K][N]%1000000000)