import sys
n = int(sys.stdin.readline())
arr = []
res = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))

for i in range(n):
    tmp = 0
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            tmp += 1
    res.append(tmp + 1)
print(*res)
