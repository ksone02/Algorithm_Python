n = int(input())
box = [0] * 100008
box[1] = 1
box[2] = 2

for i in range(3, n+1):
    box[i] = (box[i - 1] + box[i - 2]) % 10007

print(box[n])