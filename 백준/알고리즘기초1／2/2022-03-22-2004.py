n,m = map(int, input().split())
r = n-m

def cnt_num(x,number):
    cnt = 0
    while x >= number:
        cnt += x // number
        x //= number
    return cnt

print(min(cnt_num(n,5) - cnt_num(m,5) - cnt_num(r,5),
          cnt_num(n,2) - cnt_num(m,2) - cnt_num(r,2)))