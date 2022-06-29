import sys
import heapq
t = int(sys.stdin.readline())

def check(flag, num, key):
    if flag == "I":
        heapq.heappush(minq, (num, key))
        heapq.heappush(maxq, (num * -1, key))
        visit[key] = True
    elif flag == "D":
        if num == 1:
            while maxq and not visit[maxq[0][1]]:
                heapq.heappop(maxq)
            if maxq:
                visit[maxq[0][1]] = False
                heapq.heappop(maxq)
        elif num == -1:
            while minq and not visit[minq[0][1]]:
                heapq.heappop(minq)
            if minq:
                visit[minq[0][1]] = False
                heapq.heappop(minq)

for i in range(t):
    k = int(sys.stdin.readline())
    visit = [False] * k
    minq, maxq = [], []
    for j in range(k):
        flag, num = input().split(" ")
        num = int(num)
        check(flag, num, j)

    while minq and not visit[minq[0][1]]:
        heapq.heappop(minq)
    while maxq and not visit[maxq[0][1]]:
        heapq.heappop(maxq)

    if minq and maxq:
        print(-maxq[0][0], minq[0][0])
    else:
        print("EMPTY")
