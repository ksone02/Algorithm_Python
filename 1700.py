import sys
n, k = map(int, sys.stdin.readline().rstrip().split(" "))
tab = []
order = list(map(int, sys.stdin.readline().rstrip().split(" ")))

count = 0
if n < k:
    for i in range(k):
        if order[i] in tab:
            continue
        else:
            if len(tab) != n:
                tab.append(order[i])
            else:
                temp = 0
                far = 0
                for j in tab:
                    if not j in order[i:]: # tab[j]가 뒷순서에 없을 경우
                        temp = j
                        break
                    elif order[i:].index(j) > far: # 뒷순서에 있을 경우
                        far = order[i:].index(j)
                        temp = j
                tab[tab.index(temp)] = order[i]
                count += 1
    print(count)
else:
    print(0)