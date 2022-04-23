N,M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
result = []
visited = [False] * N
def dfs():
    if len(result) == M:
        print(*result)
        return
    pre = 0
    for i in range(N):
        if pre == nums[i]:
            continue
        if visited[i]:
            continue
        result.append(nums[i])
        visited[i] = True
        pre = nums[i]
        dfs()
        result.pop()
        visited[i] = False
dfs()