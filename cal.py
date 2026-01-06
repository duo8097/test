import math
a = int(input())
b = int(input())
gcd = math.gcd(a, b)
print(gcd)
res1 = a // gcd
res2 = b // gcd
print(res1)
print(res2)
