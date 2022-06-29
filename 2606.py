import sys
com = int(sys.stdin.readline())
net = int(sys.stdin.readline())

link = [[] for i in range(com)]
for _ in range(net):
    s, e = map(int, sys.stdin.readline().rstrip().split(" "))
    link[s - 1].append(e - 1)
    link[e - 1].append(s - 1)

visit = [0] * com
def dfs(v):
    if visit[v] > 0:
        return
    visit[v] = 1
    for i in link[v]:
        dfs(i)

dfs(0)
if(visit.count(1) == 1):
    print(0)
else:
    print(visit.count(1) - 1)