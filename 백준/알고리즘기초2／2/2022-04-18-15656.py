N,M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
result = []

def dfs():
    if len(result) == M:
        print(*result)
        return
    for i in range(N):
        result.append(nums[i])
        dfs()
        result.pop()
dfs()