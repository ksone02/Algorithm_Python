k, n = map(int, input().split(" "))
arr = []
for i in range(k):
    arr.append(int(input()))
s = 1
e = max(arr)

while s <= e:
        tmp = (s + e) // 2
        t = 0
        for j in arr:
            t += j // tmp
        if t < n:
            e = tmp - 1
        else:
            s = tmp + 1

print(e)

