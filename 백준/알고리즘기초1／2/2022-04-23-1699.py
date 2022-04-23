import math
N = int(input())
maxsquare = int(math.sqrt(N))
array =[i **2 for i in range(1,maxsquare+1)]
dp = [0]*(N+1)

for i in range(1,N+1):
    dp[i] = dp[i-1] + 1
    for j in array:
        if i < j:
            break
        if dp[i] > dp[i-j] + 1:
            dp[i] = dp[i-j] + 1
print(dp[N])