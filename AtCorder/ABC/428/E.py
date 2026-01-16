"""
AtCorder.ABC.428.E の Docstring
問題文
頂点に 1 から N の番号がついた N 頂点の木があります。i 番目の辺は頂点 A 
i
​	
  と頂点 B 
i
​	
  を結ぶ辺です。
頂点 u と頂点 v の距離を、頂点 u と頂点 v を両端点とするパスに含まれる辺の本数として定義します。(このパスは一意に定まります)

v=1,2,…,N について次の問題を解いてください。

頂点 1,2,…,N のうち頂点 v からの距離が最大となる頂点の番号を出力してください。ただし、条件を満たす頂点が複数存在する場合は 最も番号が大きい頂点 を出力してください。
制約
2≤N≤5×10 
5
 
1≤A 
i
​	
 <B 
i
​	
 ≤N
入力で与えられるグラフは木
入力される値は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N
A 
1
​	
  B 
1
​	
 
A 
2
​	
  B 
2
​	
 
⋮
A 
N−1
​	
  B 
N−1
​	
 
出力
N 行出力せよ。i 行目には v=i の時の答えを出力せよ。

入力例 1
Copy
3
1 2
2 3
出力例 1
Copy
3
3
1
頂点 1 からの距離が最大となる点は頂点 3 です。
頂点 2 からの距離が最大となる点は頂点 1 および頂点 3 です。このうち番号が大きい頂点である頂点 3 が答えとなります。
頂点 3 からの距離が最大となる点は頂点 1 です。

入力例 2
Copy
5
1 2
2 3
2 4
1 5
出力例 2
Copy
4
5
5
5
4
"""
from collections import deque

# ---------- 入力 ----------
N = int(input())

# 隣接リスト（1-indexed）
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# ---------- BFS ----------
def bfs(start):
    """
    start から BFS して
    各頂点への距離配列 dist を返す
    """
    dist = [-1] * (N + 1)
    q = deque()
    dist[start] = 0
    q.append(start)

    while q:
        v = q.popleft()
        for nv in graph[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                q.append(nv)

    return dist

# ---------- 木の直径 ----------
# 1 から BFS → 一番遠い点 A（同距離なら番号が大きい方）
dist1 = bfs(1)
A = 1
for i in range(1, N + 1):
    if dist1[i] > dist1[A] or (dist1[i] == dist1[A] and i > A):
        A = i

# A から BFS → 一番遠い点 B（同距離なら番号が大きい方）
distA = bfs(A)
B = A
for i in range(1, N + 1):
    if distA[i] > distA[B] or (distA[i] == distA[B] and i > B):
        B = i

# B から BFS
distB = bfs(B)

# ---------- 各頂点の答え ----------
for v in range(1, N + 1):
    if distA[v] > distB[v]:
        print(A)
    elif distA[v] < distB[v]:
        print(B)
    else:
        # 距離が同じなら番号が大きい方
        print(max(A, B))
