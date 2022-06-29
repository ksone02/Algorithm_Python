import sys
n, m = map(int, sys.stdin.readline().rstrip().split(" "))
visit = [0] * n

def dfs(v):
    if visit[v] > 0:
        return
    visit[v] = 1
    for i in link[v]:
        dfs(i)

link = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split(" "))
    link[u - 1].append(v - 1)
    link[v - 1].append(u - 1)

r = 0
for i in range(n):
    if visit[i] == 0:
        r += 1
        dfs(i)

print(r)
