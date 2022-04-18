def dfs(elements, start, k):
    if k == 0:
        results.append(elements[:])
        return
    for i in range(start, n+1):
        elements.append(i)
        dfs(elements, i+1, k-1)
        elements.pop()