import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
card = list(map(int, sys.stdin.readline().rstrip().split(" ")))

cards = list(map(sum, list(combinations(card, 3))))
tmp = m
while True:
        try:
            res = cards[cards.index(tmp)]
            break
        except ValueError:
            tmp -= 1
            continue
print(res)