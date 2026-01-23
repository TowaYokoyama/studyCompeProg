import sys
sys.setrecursionlimit(10**7)

N, X, Y = map(int, input().split())

# 隣接リスト
g = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

# 親を記録
parent = [-1] * (N + 1)

# DFS
stack = [X]
parent[X] = 0  # X は親なし

while stack:
    v = stack.pop()
    if v == Y:
        break
    for nv in g[v]:
        if parent[nv] == -1:
            parent[nv] = v
            stack.append(nv)

# Y から X へ親をたどる
path = []
cur = Y
while cur != 0:
    path.append(cur)
    cur = parent[cur]

# 逆順にして出力
path.reverse()
print(*path)
