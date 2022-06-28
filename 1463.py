number = int(input())
d = [-1] * (number+1)
d[0] = False
d[1] = 0
def mincal(n, lst):
    if(n == 1):
        return 0
    elif(lst[n] != -1):
        return lst[n]
    else:
        if(n % 6 == 0):
            lst[n] = min(mincal(n//3, lst), mincal(n//2, lst)) + 1
        elif(n % 3 == 0):
            lst[n] = min(mincal(n//3, lst), mincal(n - 1, lst)) + 1
        elif(n % 2 == 0):
            lst[n] = min(mincal(n//2, lst), mincal(n - 1, lst)) + 1
        else:
            lst[n] = mincal(n - 1, lst) + 1
        return lst[n]
print(mincal(number, d))
