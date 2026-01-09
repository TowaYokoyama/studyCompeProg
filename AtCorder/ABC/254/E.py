"""
AtCorder.ABC.254.E の Docstring
行時間制限: 3.5 sec / メモリ制限: 1024 MiB

配点 : 
500 点

問題文
N 頂点 
M 辺の単純無向グラフがあり、各頂点には 
1,…,N と番号が付けられています。 
i=1,…,M に対し、 
i 番目の辺は頂点 
a 
i
​
  と頂点 
b 
i
​
  を結びます。また、各頂点の次数は 
3 以下です。

i=1,…,Q に対し、次のクエリに答えてください。

頂点 
x 
i
​
  との距離が 
k 
i
​
  以下であるような頂点の番号の総和を求めよ。
制約
1≤N≤1.5×10 
5
 
0≤M≤min( 
2
N(N−1)
​
 , 
2
3N
​
 )
1≤a 
i
​
 <b 
i
​
 ≤N
i

=j ならば 
(a 
i
​
 ,b 
i
​
 )

=(a 
j
​
 ,b 
j
​
 )
与えられるグラフの各頂点の次数は 
3 以下
1≤Q≤1.5×10 
5
 
1≤x 
i
​
 ≤N
0≤k 
i
​
 ≤3
入力はすべて整数
入力
入力は以下の形式で標準入力から与えられる。

N 
M
a 
1
​
  
b 
1
​
 
⋮
a 
M
​
  
b 
M
​
 
Q
x 
1
​
  
k 
1
​
 
⋮
x 
Q
​
  
k 
Q
​
 
出力
Q 行出力せよ。 
i 行目には 
i 番目のクエリへの答えを出力せよ。

入力例 1
Copy
6 5
2 3
3 4
3 5
5 6
2 6
7
1 1
2 2
2 0
2 3
4 1
6 0
4 3
出力例 1
Copy
1
20
2
20
7
6
20
1 番目のクエリでは、頂点 
1 との距離が 
1 以下であるような頂点は頂点 
1 のみなので 
1 が答えです。
2 番目のクエリでは、頂点 
2 との距離が 
2 以下であるような頂点は頂点 
2,3,4,5,6 なのでこれらの総和の 
20 が答えになります。
3 番目以降のクエリも同様にして答えを求められます
"""
from collections import deque

# --- 入力 ---
N, M = map(int, input().split())

# グラフ作成（隣接リスト）
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

Q = int(input())

# --- 各クエリ処理 ---
for _ in range(Q):
    x, k = map(int, input().split())

    visited = set()
    visited.add(x)

    # (頂点, 距離)
    q = deque()
    q.append((x, 0))

    ans = 0

    while q:
        v, dist = q.popleft()
        ans += v

        if dist == k:
            continue

        for nv in graph[v]:
            if nv not in visited:
                visited.add(nv)
                q.append((nv, dist + 1))

    print(ans)
