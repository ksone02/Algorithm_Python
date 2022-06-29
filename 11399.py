import sys
n = int(sys.stdin.readline())

p = list(map(int, sys.stdin.readline().rstrip().split(" ")))

p.sort()
temp = 0
for i in range(n):
    temp += sum(p[0: i + 1])

print(temp)