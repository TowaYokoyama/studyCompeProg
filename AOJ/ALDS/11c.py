"""
AOJ.ALDS.11c の Docstring
幅優先探索
与えられた有向グラフ 
G
=
(
V
,
E
)
 について、頂点 
1
 から各頂点への最短距離 
d
（パス上の辺の数の最小値）を求めるプログラムを作成してください。各頂点には 
1
 から 
n
 までの番号がふられているものとします。頂点 
1
 からたどり着けない頂点については、距離として-1 を出力してください。

入力
最初の行に 
G
 の頂点数 
n
 が与えられます。続く 
n
 行で各頂点 
u
 の隣接リストが以下の形式で与えられます：

u
 
k
 
v
1
 
v
2
 ... 
v
k

u
 は頂点の番号、
k
 は 
u
 の出次数、
v
1
v
2
.
.
.
v
k
　は 
u
 に隣接する頂点の番号を示します。

制約
1
≤
n
≤
100
出力
各頂点について 
i
d
、
d
 を１行に出力してください。
i
d
 は頂点の番号、
d
 は頂点 
1
 からその頂点までの距離を示します。頂点番号順に出力してください。

入力例 1
4
1 2 2 4
2 1 4
3 0
4 1 3
出力例 1
1 0
2 1
3 2
4 1


"""
from collections import deque

# 入力
n = int(input())

# 隣接リスト（1-indexed）
adj = [[] for _ in range(n + 1)]

for _ in range(n):
    data = list(map(int, input().split()))
    u = data[0]
    k = data[1]
    adj[u] = data[2:]

# 距離配列（-1 = 未到達）
dist = [-1] * (n + 1)

# BFS
queue = deque()
dist[1] = 0
queue.append(1)

while queue:
    u = queue.popleft()
    for v in adj[u]:
        if dist[v] == -1:          # まだ行ってない
            dist[v] = dist[u] + 1  # 距離更新
            queue.append(v)

# 出力
for i in range(1, n + 1):
    print(i, dist[i])
