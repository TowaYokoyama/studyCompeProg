"""
AtCorder.ABC.436.D の Docstring
D - Teleport Maze   / 
実行時間制限: 2 sec / メモリ制限: 1024 MiB

配点 : 400 点

問題文
H 行 W 列のマス目からなる迷路があります。 上から i 行目、左から j 列目のマスを (i,j) と表記します。 マス (i,j) がどのようなマスであるかは文字 S 
i,j
​	
  として与えられ、各文字の意味は以下の通りです。

. : 空きマス
# : 障害物マス
英小文字（a - z）: ワープマス
迷路内では、以下の二種類の行動を好きな順序で何回でも行うことができます。

歩行：現在いるマスから上下左右の四方向のいずれかに 1 マス分進んだマスへ移動する。ただし、障害物マスへ移動することや、マス目の外に移動することはできない。
ワープ：ワープマスにいるとき、そのワープマスと同じ文字が書かれたワープマスのうちいずれか好きなマスへと移動する。
マス (1,1) からマス (H,W) へ移動することが可能かどうか判定し、可能ならばそれに必要な最小の合計行動回数を求めてください。

制約
1≤H,W≤1000
H×W≥2
H,W は整数
S 
i,j
​	
  は ., #, または英小文字のいずれか
S 
1,1
​	
 

= #
S 
H,W
​	
 

= #
入力
入力は以下の形式で標準入力から与えられる。

H W
S 
1,1
​	
 S 
1,2
​	
 …S 
1,W
​	
 
⋮
S 
H,1
​	
 S 
H,2
​	
 …S 
H,W
​	
 
出力
マス (1,1) からマス (H,W) へ移動することが可能ならばそれに必要な最小の合計行動回数を、不可能ならば -1 を出力せよ。

入力例 1
Copy
3 4
..a.
####
ba#b
出力例 1
Copy
5
以下のように行動することで、マス (1,1) からマス (3,4) へ移動することができます。

マス (1,1) からマス (1,2) へ歩行によって移動する。
マス (1,2) からマス (1,3) へ歩行によって移動する。
マス (1,3) からマス (3,2) へワープによって移動する。
マス (3,2) からマス (3,1) へ歩行によって移動する。
マス (3,1) からマス (3,4) へワープによって移動する。
このときの合計行動回数は 5 回であり、これが最小です。

入力例 2
Copy
3 4
..a.
####
b.#b
出力例 2
Copy
-1
マス (1,1) からマス (3,4) へ移動することは不可能です。

入力例 3
Copy
4 4
xxxx
xxxx
xxxx
xxxx
出力例 3
Copy
1
入力例 4
Copy
7 11
u..#y..#...
k..#.z.#.k.
iju#...#x..
###########
..x#.t.#..n
abc#y..#...
..z#..t#.y.
出力例 4
Copy
12

"""
from collections import deque 
H,W = map(int, input().split())
S = [list(input()) for _ in range(H)]
# 文字ごとのワープ地点を記録
wrap = {chr(ord('a')+ i):[] for i in range(26)}

for i in range(H):
    for j in range(W):
        if 'a' <= S[i][j]<='z':
            wrap[S[i][j]].append((i,j))
        
        
#距離配列(初期値は-1)
dist =[[-1]*W for _ in range(H)]
dist[0][0] = 0

#BFSキュー
q = deque()
q.append((0,0))

#ワープを使ったかどうか
used_wrap = {k:False for k in wrap}
#移動方向
dirs = [(1,0),(-1,0),(0,1),(0,-1)]

while q:
    r,c =  q.popleft()
    #ゴールに着いたら最短
    
    if (r,c) == (H-1,W-1):
        print(dist[r][c])
        exit()
        
    #ほこう
    for dr,dc in dirs:
        nr,nc = r+dr, c+dc
        if 0<=nr<H and 0<=nc<W:
            if S[nr][nc] != "#" and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr,nc))
                
    #ワープ
    ch = S[r][c]
    if 'a' <= ch <= 'z' and not used_wrap[ch]:
        for nr,nc in wrap[ch]:
            if dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr,nc))
#この文字のワープ地点はもう使わない
        used_wrap[ch] = True
#到達不可能
print(-1)