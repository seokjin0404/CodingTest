# 내 풀이
# S = input()
# stack = []
# first = [-1] * 26
# cnt = 0
# for c in S:
#     if c not in stack:
#         stack.append(c)
#         first[ord(c) - ord('a')] = cnt
#         cnt += 1
#     else:
#         pass
# print(*first)

"""
find 함수
문자열에서 사용할 수 있는데. 찾는 문자가 존재하면 해당 위치의 index를 반환한다.
여러 개 있다면 맨 처음 찾은 문자의 index를 반환하고, 존재하지 않는다면 -1을 반환한다.
"""
word = input()
alphabet = list(range(ord('a'),ord('z')+1))

for x in alphabet:
    print(word.find(chr(x)), end = " ")

"""
index 함수
리스트에 찾고자 하는 값이 있으면 인덱스르 반환하는데,
리스트에 해당하는 값이 존재하지 않으면 오류가 발생한다.
"""
# word = list(input())
# abc = "abcdefghijklmnopqrstuvwxyz"

# for c in abc:
#     if c in word:
#         print(word.index(c), end = " ")
#     else:
#         print(-1, end = " ")