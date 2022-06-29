import sys
N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split(" "))))
white = 0
blue = 0 

def cut(arr, N):
    global white, blue
    check = list(set(sum(arr, [])))
    if len(check) == 1:
        if check[0] == 0: white += 1
        elif check[0] == 1: blue += 1
    else:
        div = N // 2
        for i in range(0, N, div):
            for j in range(0, N, div):
                cut([row[j:j+div] for row in arr[i:i+div]], div)
            
cut(arr, N)
print(white)
print(blue)
