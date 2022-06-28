import sys
minN = int(sys.stdin.readline())
maxN = int(sys.stdin.readline())

so = []
for i in range(minN, maxN+1):
    tmp = 0
    if i == 1:
        continue
    else:
        for j in range(2, i):
            if(i % j == 0):
                tmp = 1
        if tmp == 0:
            so.append(i)

if len(so) == 0:
    print(-1)
else:
    print(str(sum(so)) + '\n' + str(min(so)))