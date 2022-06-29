import sys
n, m = map(int, sys.stdin.readline().rstrip().split(" "))
dic = {}
for i in range(1, n+1):
    pocketmon = sys.stdin.readline().rstrip()
    dic[i] = pocketmon
newDict = {v:k for k,v in dic.items()}
print(dic)
print(newDict)
for j in range(m):
    quest = sys.stdin.readline().rstrip()
    if not quest.isalpha():
        quest = int(quest)
        print(dic[quest])
    else:
        print(newDict[quest])