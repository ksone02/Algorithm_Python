import sys
n, m = map(int, input().split(" "))
int(n), int(m)
arr = [0] * n
for i in range(0, n):
    arr[i] = int(sys.stdin.readline())
for j in range(0, m):
    fir, las = map(int, input().split(" "))
    int(fir), int(las)
    newArr = arr[fir-1:las]
    newArr.sort()
    print(newArr[0])

#세그먼트트리활용
import math

tree_list = [0] * (pow(2, math.ceil(math.log(len(a), 2)) + 1)) -1 #노드의 수 -> 2^높이 - 1
def init_tree(a, tree, node, s, e):
    if  s == e:
        tree[node - 1] = s
    else:
        init_tree(a, tree, node*2, s, (s+e)//2)
        init_tree(a, tree, node*2+1, (s+e)//2+1, e)
        if a[tree[node*2-1]] < a[tree[node*2]]:
            tree[node-1] = tree[node*2-1]
        else:
            tree[node-1] = tree[node*2]