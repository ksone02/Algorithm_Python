import sys
t = int(sys.stdin.readline())

cache = [0, 1, 2, 4] + [-1] * 12

for _ in range(t):
    n = int(sys.stdin.readline())
    if cache[n] != -1:
        print(cache[n])
    else:
        for i in range(4, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2] + cache[i - 3]
        print(cache[n])