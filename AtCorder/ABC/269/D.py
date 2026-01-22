import sys
sys.setrecursionlimit(10**7)

# Union-Find (DSU)
parent = []
size = []

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if size[a] < size[b]:
        a, b = b, a
    parent[b] = a
    size[a] += size[b]


# ---- 入力 ----
n = int(input())

# C++ と同じサイズ
mem = [[0] * 2010 for _ in range(2010)]

x = [0] * (n + 1)
y = [0] * (n + 1)

parent = [i for i in range(n + 1)]
size = [1] * (n + 1)

# 六角格子の6方向
dx6 = [-1, -1, 0, 0, 1, 1]
dy6 = [-1, 0, -1, 1, 0, 1]

for i in range(1, n + 1):
    xi, yi = map(int, input().split())
    xi += 1005
    yi += 1005
    x[i] = xi
    y[i] = yi
    mem[xi][yi] = i

# ---- 近傍を見て union ----
for i in range(1, n + 1):
    for k in range(6):
        nx = x[i] + dx6[k]
        ny = y[i] + dy6[k]
        if mem[nx][ny] > 0:
            union(i, mem[nx][ny])

# ---- 連結成分数を数える ----
res = 0
for i in range(1, n + 1):
    if find(i) == i:
        res += 1

print(res)
