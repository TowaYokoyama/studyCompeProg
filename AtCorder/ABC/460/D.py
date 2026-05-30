"""
問題文
H 行 W 列のマス目があります。このマス目の上から i 行目、左から j 列目のマスをマス (i,j) と呼びます。

すべてのマスは白または黒で塗られています。マス目の情報は H 個の長さ W の文字列 S 
1
​	
 ,S 
2
​	
 ,…,S 
H
​	
  によって与えられ、S 
i
​	
  の j 文字目が . のときマス (i,j) は白で、S 
i
​	
  の j 文字目が # のときマス (i,j) は黒で塗られています。

あなたは、以下の操作を 10 
100
  回行います。

すべてのマスに対して同時に以下の規則で色の塗り替えを行う。
操作前に白く塗られているマスは、そのマスに隣接する黒く塗られているマスが存在するとき、またそのときに限り黒く塗り替える。ただし、マス (x,y) とマス (x 
′
 ,y 
′
 ) が隣接しているとは、片方のマスがもう片方のマスの 8 近傍にある、すなわち max(∣x−x 
′
 ∣,∣y−y 
′
 ∣)=1 であることを指す。
操作前に黒く塗られているマスは、白く塗り替える。
操作を終えた後に各マスが何色で塗られているか求めてください。

制約
1≤H×W≤10 
6
 
H,W は正整数
S 
i
​	
  は ., # からなる長さ W の文字列
入力
入力は以下の形式で標準入力から与えられる。

H W
S 
1
​	
 
S 
2
​	
 
⋮
S 
H
​	
 
出力
H 行出力せよ。

各行に ., # からなる長さ W の文字列を 1 つずつ出力せよ。

i 行目の文字列の j 文字目は 10 
100
  回の操作を行った後にマス (i,j) が白で塗られているとき . に、黒で塗られているとき # になるようにせよ。

入力例 1
Copy
3 4
#.#.
.#..
#...
出力例 1
Copy
#.#.
.#..
#..#
はじめ、マス目は以下のようになっています。



1 回操作を行うと、マス目は以下のようになります。



10 
100
  回操作を行うと、マス目は以下のようになります。



入力例 2
Copy
3 3
###
###
###
出力例 2
Copy
...
...
...
入力例 3
Copy
5 7
.#.....
.......
..#....
.......
....#..
出力例 3
Copy
.#.##.#
....#..
#.#.###
#.....#
###.#.#
"""
from collections import deque

H, W = map(int, input().split())
S = [list(input().strip()) for _ in range(H)]

INF = 10**18
dirs = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

def bfs(target):
    dist = [[INF] * W for _ in range(H)]
    q = deque()

    for i in range(H):
        for j in range(W):
            if S[i][j] == target:
                dist[i][j] = 0
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if 0 <= nx < H and 0 <= ny < W:
                if dist[nx][ny] == INF:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    return dist


# 最近黒距離
dist_black = bfs('#')

# 最近白距離
dist_white = bfs('.')

ans = [['.'] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            d = dist_white[i][j]

            if d == INF:
                ans[i][j] = '.'
            elif d % 2 == 1:
                ans[i][j] = '#'
            else:
                ans[i][j] = '.'

        else:
            d = dist_black[i][j]

            if d == INF:
                ans[i][j] = '#'
            elif d % 2 == 1:
                ans[i][j] = '.'
            else:
                ans[i][j] = '#'

for row in ans:
    print(''.join(row))