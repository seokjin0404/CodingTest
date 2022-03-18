import sys

while True:
    line = sys.stdin.readline().rstrip('\n')
    # line = input()
    if not line:
        break
    l,u,d,s = 0,0,0,0
    for each in line:
        if each.islower():
            l += 1
        elif each.isupper():
            u += 1
        elif each.isdigit():
            d += 1
        elif each.isspace():
            s += 1
    print(f"{l} {u} {d} {s}")

'''
input()은 파일의 끝에 EOF가 발생하기 때문에
try except를 사용해야하고
sys.stdin.readline()은 빈 문자열을 반환한다.
https://joewithtech.tistory.com/26
https://y00n-lee.tistory.com/9
'''