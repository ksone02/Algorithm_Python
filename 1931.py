import sys
n = int(sys.stdin.readline())
timetable = []

for _ in range(n):
    s, e = map(int, sys.stdin.readline().rstrip().split(" "))
    timetable.append([s, e])

timetable.sort(key = lambda x: (x[0], x[1]))

res = [timetable[0]]
a = timetable[0]
for i in range(1, n):
    if timetable[i][1] < a[1]:
        res.pop()
        a = timetable[i]
        res.append(a)
        continue
    if timetable[i][0] >= a[1]:
        a = timetable[i]
        res.append(a)
print(len(res))