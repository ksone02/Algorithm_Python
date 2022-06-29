import sys
n = int(sys.stdin.readline())

d = [0, 1] + [0] * (n - 1)

for i in range(2, n+1):
    minV = 1e9
    j = 1
    while(j ** 2) <= i:
        minV = min(minV, d[i - (j ** 2)])
        j += 1
    d[i] = minV + 1

print(d[n])