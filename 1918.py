import sys
s = sys.stdin.readline()

def solution(string):
    ans = []
    newStr = []
    for i in string:
        if i.isalpha():
            ans.append(i)
        else:
            if i == "*" or i == "/" or i == "+" or i == '-':
                while(len(newStr) != 0 and priority(newStr[0]) >= priority(i)):
                    ans.append(newStr.pop(0))
                newStr.insert(0, i)
            elif i == "(":
                newStr.insert(0, i)
            elif i == ")":
                while(len(newStr) != 0 and newStr[0] != "("):
                    ans.append(newStr.pop(0))
                newStr.pop(0)
                
    while len(newStr) != 0:
        ans.append(newStr.pop(0))
    print(''.join(s for s in ans))

def priority(opr):
    if opr == "(" or opr == ")":
        return 0
    elif opr == "+" or opr == "-":
        return 1
    elif opr == "*" or opr == "/":
        return 2
    return -1

solution(s);