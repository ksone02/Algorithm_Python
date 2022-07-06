n = int(input())
parti = ['zzzz'] * n
comp = ['zzzz'] * n
for _ in range(n):
    parti[_] = input()
for _ in range(n-1):
    comp[_] = input()

ans = ''
par = sorted(parti)
com = sorted(comp)

for i in range(len(par)):
    if par[i] != com[i]:
        ans = par[i]
        break
print(ans)