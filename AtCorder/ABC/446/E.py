"""
問題文
0≤x,y≤M−1 を満たす整数組 
(x,y) のうち、以下の漸化式で表される無限長の数列 
(s 
1
​
 ,s 
2
​
 ,…) が 
M の倍数を全く含まないようなものは何通りありますか？

s 
1
​
 =x
s 
2
​
 =y
s 
n
​
 =As 
n−1
​
 +Bs 
n−2
​
  (
n≥3)
制約
2≤M≤1000
0≤A,B≤M−1
入力される値はすべて整数
入力
入力は以下の形式で標準入力から与えられる。

M 
A 
B
出力
答えを 
1 行に出力せよ。

入力例 1
Copy
4 1 2
出力例 1
Copy
7
問題文中の条件を満たす整数組は 
(x,y)=(1,1),(1,3),(2,1),(2,2),(2,3),(3,1),(3,3) の 
7 通りです。

たとえば 
(x,y)=(2,1) としたとき、対応する数列は 
(2,1,5,7,17,31,65,127,…) となります。この数列は 
4 の倍数を全く含みません。よって、
(x,y)=(2,1) は問題文中の条件を満たします。

一方で 
(x,y)=(3,2) としたとき、対応する数列は 
(3,2,8,12,28,52,108,212,…) となります。この数列の第 
3 項は 
8 であり、これは 
4 の倍数です。よって、
(x,y)=(3,2) は問題文中の条件を満たしません。

入力例 2
Copy
446 1 1
出力例 2
Copy
0
問題文中の条件を満たす整数組は存在しません。

入力例 3
Copy
1000 784 385
出力例 3
Copy
995373
"""
import sys
from collections import deque

input = sys.stdin.readline

M, A, B = map(int, input().split())

# 頂点数は M^2
# 頂点番号は x*M + y で管理
edges = [[] for _ in range(M * M)]

# 逆辺を作る
for x in range(M):
    for y in range(M):
        # (x, y) <- (y, (A*y + B*x) % M)
        k = (x * B + y * A) % M
        from_state = y * M + k
        to_state = x * M + y
        edges[from_state].append(to_state)

# BFS
visited = [False] * (M * M)
queue = deque()

# 初期状態：0 を含む状態
for x in range(M):
    for y in range(M):
        if x == 0 or y == 0:
            v = x * M + y
            visited[v] = True
            queue.append(v)

# BFS 実行
while queue:
    v = queue.popleft()
    for u in edges[v]:
        if not visited[u]:
            visited[u] = True
            queue.append(u)

# 答えカウント
ans = 0
for x in range(M):
    for y in range(M):
        if not visited[x * M + y]:
            ans += 1

print(ans)