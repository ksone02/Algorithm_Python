import sys
N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split(" "))))


one = 0
zero = 0
mone = 0
def cut(arr, N):
    global one, zero, mone
    newArr = []
    check = list(set(sum(arr, [])))
    if len(check) == 1:
        if 1 in check: one += 1
        elif 0 in check: zero += 1
        elif -1 in check: mone += 1
    else:
        div = N // 3
        for i in range(0, N, div):
            for j in range(0, N, div):
                cut([row[j:j+div] for row in arr[i:i+div]], div)
            
cut(arr, N)

print(mone)
print(zero)
print(one)