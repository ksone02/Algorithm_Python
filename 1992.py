import sys
N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(list(map(int, list(input()))))
char = ''

def cut(arr, N):
    global char
    check = list(set(sum(arr, [])))
    if len(check) == 1:
        if check[0] == 0: char += '0'
        elif check[0] == 1: char += '1'
    else:
        char += '('
        div = N // 2
        for i in range(0, N, div):
            for j in range(0, N, div):
                cut([row[j:j+div] for row in arr[i:i+div]], div)
        char += ')'
            
cut(arr, N)
print(char)
