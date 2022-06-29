dictionary = {}
for i in range(26):
    dictionary[97+i]=i+1

n = int(input())
s = input()

res = 0

for i in range(n):
    res += dictionary[ord(s[i])]*31**i

print(res % 1234567891)