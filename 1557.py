n = int(input())

def squareFree(n):
    cnt = 0
    for i in range(1, int(n ** 0.5) + 1, 1):
        cnt += mu[i] * (n//(i*i))
    return cnt

mu = [0] * 1000001
mu[1] = 1
for i in range(1, 1000001):
    if mu[i]:
        for j in range(i*2, 1000001, i):
            mu[j] -= mu[i]

l, r = 0, 10**10
while  l < r - 1:
    mid = (l + r) // 2
    if squareFree(mid) < n:
        l = mid
    else:
        r = mid
print(r)