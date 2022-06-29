import sys
n, m = map(int, sys.stdin.readline().split(" "))
dic = {}
count = 0
li = []
for i in range(n):
    canthear = sys.stdin.readline().rstrip()
    dic[canthear] = 1
for j in range(m):
    cantsee = sys.stdin.readline().rstrip()
    if(cantsee in dic):
        li.append(cantsee)
print(len(li))
li.sort()
for i in li:
    print(i)