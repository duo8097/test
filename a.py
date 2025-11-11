from math import gcd
N = int(input())
a = int(input())
b = int(input())
l = a * b // gcd(a, b)
res = N - (N // a + N // b - N // l)
print(res)
