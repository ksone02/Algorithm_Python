n = int(input())

a = [0] + [1] * 1000000
arr = []
for i in range(2, 1000001):
    if a[i] == 0:
        arr.append(i)
    if len(arr) >= n:
        break
    for j in range(i + 1, 1000001):
        if j % i**2 == 0:
            a[j] = 0

print(arr)

mu = [0] * 1000001
mu[1] = 1
for i in range(1, 1000001):
    if mu[i]:
        for j in range(i*2, 1000001, i):
            mu[j] -= mu[i]
# 0 -> 소인수 분해했을 때 지수가 2 이상인 소수가 존재
# 1 -> 지수의 합이 짝수
# -1 -> 지수의 합이 홀수


l, r = 0, 10**10
while  l < r - 1:
    mid = (l + r) // 2
    if func(mid) < n:
        l = mid
    else:
        r = mid
print(r)