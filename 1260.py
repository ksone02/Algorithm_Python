import sys
from collections import deque
n, m, v = map(int, sys.stdin.readline().rstrip().split(" "))
edge = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, sys.stdin.readline().rstrip().split(" "))
    edge[s].append(e)
    edge[e].append(s)

for i in edge:
    i.sort()

d_arr = [0 for _ in range(n+1)]
def dfs(x):
    d_arr[x] = 1
    print(x, end= ' ')
    for y in edge[x]:
        if d_arr[y] == 0:
            dfs(y)

def bfs():
    queue = deque([v])
    b_arr = [0 for _ in range(n+1)]
    b_arr[v] = 1
    while queue:
        k = queue.popleft()
        print(k, end = ' ')
        for i in edge[k]:
            if not b_arr[i]:
                b_arr[i] = 1
                queue.append(i)

dfs(v)
print()
bfs()
print()