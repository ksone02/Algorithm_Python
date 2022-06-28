import sys
t = int(sys.stdin.readline())

while(t > 0):
    n = input()
    arr = n.split(" ")
    arr = list(map(int, arr))
    arr.sort()
    print(arr[-3])
    t -= 1