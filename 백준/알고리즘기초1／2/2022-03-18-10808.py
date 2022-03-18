S = input()
counter = [0] * 26
for c in S:
    counter[ord(c) - ord('a')] += 1

print(*counter)

# ord는 python 내장 함수로 해당 값을 ASCII 코드로 변환한다.