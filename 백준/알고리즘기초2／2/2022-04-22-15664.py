N,M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
result = []

def dfs(start):
    if len(result) == M:
        print(*result)
    pre = 0
    for i in range(start,N):
        if pre == nums[i]:
            continue
        result.append(nums[i])
        pre = nums[i]
        dfs(i+1)
        result.pop()

dfs(0)