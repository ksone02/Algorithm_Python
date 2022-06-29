import sys
n = int(sys.stdin.readline())

for i in range(n):
    if i == 0:
        print(" " * (n - 1) + "*")
    elif i == n - 1:
        print("* " * (i) + "*")
    else:
        print(" " * (n - 2 - i) + " *" * (i + 1))
