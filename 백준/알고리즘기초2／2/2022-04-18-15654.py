N, M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
result = []

def dfs():
    if len(result) == M:
        print(*result)
        return
    for n in nums:
        if n not in result:
            result.append(n)
            dfs()
            result.pop()
dfs()