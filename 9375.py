t = int(input())

for _ in range(t):
    n = int(input())
    clothes = [0] * n
    for _ in range(n):
        clothes[_] = input().split(" ")
    CloType = {}

    for c, t in clothes:
        if t not in CloType:
            CloType[t] = 2
        else:
            CloType[t] += 1
    cnt = 1
    for num in CloType.values():
        cnt *= num

    print(cnt - 1)