N,M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
result = []

def dfs():
    if len(result) == M:
        print(*result)
        return 
    pre = 0
    for i in range(N):
        if pre == nums[i]:
            continue
        result.append(nums[i])
        pre = nums[i]
        dfs()
        result.pop()
dfs()
