import sys
e, s, m = map(int, sys.stdin.readline().rstrip().split(" "))
e1, s1, m1 = 0, 0, 0
count = 0
while True:
    if e1 == e and s1 == s and m1 == m:
        break
    count += 1
    if e1 < 15:
        e1 += 1
    else:
        e1 = 1

    if s1 < 28:
        s1 += 1
    else: 
        s1 = 1

    if m1 < 19:
        m1 += 1
    else:
        m1 = 1
print(count)