import sys

def combinations_3(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in combinations_3(array[i:], r-1):
                yield [array[i]] + next

n = int(sys.stdin.readline())
cardPrice = list(map(int, input().split(" ")))

array = [i for i in range(1, len(cardPrice) + 1)]
arr = []
for i in range(1, len(array)+1):
    res = list(combinations_3(array, i))
    for j in res:
        if sum(j) == n:
            arr.append(j)

arr2 = []
for k in arr:
    arr3 = []
    for l in k:
        arr3.append(cardPrice[l - 1])
    arr2.append(sum(arr3))

print(max(arr2))