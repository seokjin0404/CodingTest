s=[]
pm=[]
n = int(input())
cnt = 1
is_break = False

for i in range(n):
    num = int(input())
    while num >= cnt:
        s.append(cnt)
        pm.append("+")
        cnt+=1
    if s[-1] == num:
        s.pop()
        pm.append("-")
    else:
        is_break = True
if not is_break:
    for i in pm:
        print(i)
else:
    print("NO")