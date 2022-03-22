import math
import sys

n = 1000000
array = [True for i in range(n+1)]

for i in range(2,int(math.sqrt(n))+1):
    if array[i]:
        j = 2
        while i*j<=n:
            array[i*j] = False
            j += 1

while True:
    N = int(sys.stdin.readline())
    if not N:
        break
    for i in range(3, len(array)):
        if array[i] and array[N-i]:
            print(f"{N} = {i} + {N-i}")
            break