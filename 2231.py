n = int(input())
checkLen = len(str(n))

if n > 17:
    s = 9 * checkLen
    start = n - s
else:
    s = 0
    start = 0


while start != n + 1:
    tmp = start
    for i in str(start):
        tmp += int(i)
    if tmp == n:
        print(start)
        break
    else:
        start += 1
if start == n+1:
    print(0)
