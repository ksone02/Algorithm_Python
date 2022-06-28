n, m = map(int, input().split(" "))
arr = []
inp = input().split(" ")
for i in inp:
    arr.append(int(i))

s = 1
e = max(arr)

if(m == 0):
    print(e)
elif(n == 1):
    print(arr[0] - m)
else:
    while s <= e:
        cutArr = []
        mid = (s + e) // 2
        for j in arr:
            if j - mid > 0:
                cutArr.append(j-mid)
            else:
                cutArr.append(0)
        
        if sum(cutArr) > m:
            s = mid + 1
        elif sum(cutArr) < m:
            e = mid - 1
        else:
            print(mid)
            quit()

    print(e)