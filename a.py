#these are my OI code -_-
n, k = map(int, input().split())
res = n
a = n
while a >= k:
    b = a // k
    res += b
    a = a % k + b
print(res)
