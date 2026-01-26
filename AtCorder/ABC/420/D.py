"""
AtCorder.ABC.420.D の Docstring
H 行 W 列のグリッドがあります。上から i 行目、左から j 列目のマス目を (i,j) と表します。各マスの状態は文字 A 
i,j
​	
  で表され、意味は以下の通りです。

. ：空きマス。
# ：障害物マス。
S ：スタートマス。
G ：ゴールマス。
o ：開いたドアのマス。
x ：閉じたドアのマス。
? ：スイッチマス。
高橋君は、 1 回の操作で今いるマスから上下左右に隣り合う、障害物マスでも閉じたドアでもないマスへ移動することができます。

また、スイッチマスに移動する度に全ての開いたドアのマスは閉じたドアのマスに、閉じたドアのマスは開いたドアのマスに変わります。

高橋君がはじめスタートマスにいる状態からゴールマスにいる状態にするよう操作できるか判定し、可能な場合は必要な操作回数の最小値を求めてください。

制約
1≤H,W≤500
H,W は整数
A 
i,j
​	
  は ., #, S, G, o, x, ? のいずれか
S と G は A 
i,j
​	
  にそれぞれちょうど 1 つずつ存在する
入力
入力は以下の形式で標準入力から与えられる。

H W
A 
1,1
​	
 A 
1,2
​	
 ⋯A 
1,W
​	
 
A 
2,1
​	
 A 
2,2
​	
 ⋯A 
2,W
​	
 
⋮
A 
H,1
​	
 A 
H,2
​	
 ⋯A 
H,W
​	
 
出力
高橋君がはじめスタートマスにいる状態からゴールマスにいる状態するよう操作できる場合は必要な操作回数の最小値を、できない場合は −1 を出力せよ。

入力例 1
Copy
2 4
S.xG
#?o.
出力例 1
Copy
5
(1,1) から順に (1,2),(2,2),(1,2),(1,3),(1,4) と移動するよう操作することで 5 回の操作でゴールマスにいる状態にすることができます。

入力例 2
Copy
1 5
So?oG
出力例 2
Copy
-1
どのように操作してもゴールマスにいる状態にすることはできません。したがって、 −1 を出力してください。

入力例 3
Copy
5 5
Sx?x?
o#o#x
?o?o?
x#x#o
?x?oG
出力例 3
Copy
10
"""
from collections import deque 
H,W = map(int,input().split())
g = [list(input())for _ in range(H)]
"""
. ：空きマス。
# ：障害物マス。
S ：スタートマス。
G ：ゴールマス。
o ：開いたドアのマス。
x ：閉じたドアのマス。
"""
dirs = [(-1,0),(1,0),(0,-1),(0,1)]  # 上下左右
for i in range(H):
    for j in range(W):
        if g[i][j] == 'S':
            sx, sy = i, j
        if g[i][j] == 'G':
            gx, gy = i, j

def bfs(sx, sy, gx, gy):
    INF = -1
    dist = [[[INF]*2 for _ in range(W)] for _ in range(H)]

    q = deque()
    q.append((sx, sy, 0))      # (x, y, door_state)
    dist[sx][sy][0] = 0

    while q:
        x, y, state = q.popleft()
        d = dist[x][y][state]

        if (x, y) == (gx, gy):
            return d

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < H and 0 <= ny < W):
                continue

            cell = g[nx][ny]
            if cell == '#':
                continue

            next_state = state
            if cell == '?':
                next_state ^= 1

            if cell == 'o' and next_state == 1:
                continue
            if cell == 'x' and next_state == 0:
                continue

            if dist[nx][ny][next_state] == INF:
                dist[nx][ny][next_state] = d + 1
                q.append((nx, ny, next_state))

    return -1

print(bfs(sx, sy, gx, gy))
