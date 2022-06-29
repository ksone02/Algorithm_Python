import sys
t = int(sys.stdin.readline())

def fibo(num, st):
    if num == st:
        print(memo[st][0], memo[st][1])
    else:
        memo.append([memo[-1][0] + memo[-2][0], memo[-1][1] + memo[-2][1]])
        fibo(num + 1, st)

for i in range(t):
    memo = [[0, 0], [0, 1], [1, 1]]
    n = int(sys.stdin.readline())

    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        fibo(2, n)