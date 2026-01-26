"""
AtCorder.ABC.383.C の Docstring
tCoder社のオフィスは H 行 W 列のマス目で表されます。上から i 行目、左から j 列目のマスを (i,j) と表します。

各マスの状態は文字 S 
i,j
​	
  で表され、 S 
i,j
​	
  が # のときそのマスは壁、. のときそのマスは床、H のときそのマスは加湿器が置かれた床です。

あるマスは、ある加湿器から壁を通らず上下左右に D 回以下の移動で辿り着ける場合加湿されます。ここで、加湿器が置かれた床のマスは必ず加湿されていることに注意してください。

加湿されている床のマスの個数を求めてください。

制約
1≤H≤1000
1≤W≤1000
0≤D≤H×W
S 
i,j
​	
  は # または . または H である (1≤i≤H,1≤j≤W)
入力される数値は全て整数
入力
入力は以下の形式で標準入力から与えられる。

H W D
S 
1,1
​	
 S 
1,2
​	
 ⋯S 
1,W
​	
 
S 
2,1
​	
 S 
2,2
​	
 ⋯S 
2,W
​	
 
⋮
S 
H,1
​	
 S 
H,2
​	
 ⋯S 
H,W
​	
 
出力
答えを出力せよ。

入力例 1
Copy
3 4 1
H...
#..H
.#.#
出力例 1
Copy
5
マス (1,1),(1,2),(1,4),(2,3),(2,4) の 5 つのマスが加湿されています。

入力例 2
Copy
5 6 2
##...H
H.....
..H.#.
.HH...
.###..
出力例 2
Copy
21
入力例 3
Copy
1 6 3
...#..
出力例 3
Copy
0
加湿されるマスが存在しない場合もあります
"""
from collections import deque

H, W, D = map(int, input().split())
S = [list(input()) for _ in range(H)]

# 加湿器(H)の座標を集める
points = []
for i in range(H):
    for j in range(W):
        if S[i][j] == 'H':
            points.append((i, j))

visited = [[False] * W for _ in range(H)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    queue = deque()
    
    # 多始点BFS（全Hをスタートにする）
    for x, y in points:
        queue.append((x, y, 0))
        visited[x][y] = True

    while queue:
        x, y, d = queue.popleft()

        # D回動いたらこれ以上広げない
        if d == D:
            continue

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < H and 0 <= ny < W):
                continue
            if S[nx][ny] == '#':
                continue
            if visited[nx][ny]:
                continue

            visited[nx][ny] = True
            queue.append((nx, ny, d + 1))

# BFS 実行
bfs()

# 加湿された床マスを数える
ans = 0
for i in range(H):
    for j in range(W):
        if visited[i][j] and S[i][j] != '#':
            ans += 1

print(ans)
