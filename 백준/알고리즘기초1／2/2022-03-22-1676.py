cnt = 0
N = int(input())
while N >= 5:
    cnt += N//5
    N //= 5
print(cnt)
