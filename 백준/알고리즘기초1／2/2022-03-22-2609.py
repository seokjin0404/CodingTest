A, B = map(int, input().split())

a, b = A, B

while b:
    a, b = b, a%b

print(a)
print(int(A*B/a)) 