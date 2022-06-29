from math import gcd
a, b = map(int, input().split(" "))

v = gcd(a,b)
print('1' * v)