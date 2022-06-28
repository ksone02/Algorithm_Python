import sys
import collections
n = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split(" "))))
dict_arr = collections.Counter(arr)
m= int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split(" ")))

res = ""

for i in range(m):
    s = 0
    e = n - 1
    while s <= e:
        mid = (s+e) // 2

        if arr2[i] > arr[mid]:
            s = mid + 1
        elif arr2[i] < arr[mid]:
            e = mid - 1
        else:
            res += str(dict_arr[arr[mid]]) + " "
            break
    else: res+= "0 "

print(res)
