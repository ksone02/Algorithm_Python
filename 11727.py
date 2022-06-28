n = int(input())
box = [0] * 100008
box[1] = 1

for i in range(2, n+1):
    if i % 2 == 0:
        box[i] = (2 * box[i - 1] + 1) % 10007
    else:
        box[i] = (2 * box[i - 1] - 1) % 10007

print(box[n])