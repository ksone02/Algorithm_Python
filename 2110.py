import sys
n, m = map(int, sys.stdin.readline().split(" "))
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()

s = 1
e = arr[-1] - arr[0]
res = 0

while s <= e:
    mid = (s + e) // 2
    cnt = 1
    index = 0
    for j in range(len(arr)):
        if arr[j] - arr[index] >= mid:
            cnt += 1
            index = j
    
    if cnt >= m :
        s = mid  + 1
        res = mid
    else:
        e = mid - 1
print(res)
