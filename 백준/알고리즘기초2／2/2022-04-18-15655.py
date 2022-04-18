N,M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()

result = []

def dfs(start):
    if len(result) == M:
        print(*result)
    for i in range(start, N):
        result.append(nums[i])
        dfs(i+1)
        result.pop()

dfs(0)