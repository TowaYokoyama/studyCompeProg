"""
AtCorder.ABC.425.D の Docstring
問題文
H 行 W 列のマス目があります。上から i 行目 (1≤i≤H)、左から j 列目 (1≤j≤W) のマスをマス (i,j) と呼ぶことにします。

はじめ、マス (i,j) は S 
i,j
​	
  が # のとき黒、. のとき白で塗られています。

以下の操作を 10 
100
  回行います。

白で塗られているマスであって、そのマスに辺で隣接するマスのうちちょうど 1 つが黒で塗られているようなマスの集合を T とする。T の各マスに対して、そのマスを黒で塗る。ただし、2 つのマス (i 
1
​	
 ,j 
1
​	
 ),(i 
2
​	
 ,j 
2
​	
 ) が辺で隣接するとは、 ∣i 
1
​	
 −i 
2
​	
 ∣+∣j 
1
​	
 −j 
2
​	
 ∣=1 であることをいう。
すべての操作が終わったあとに黒く塗られているマスの個数を求めてください。

制約
2≤H,W
HW≤3×10 
5
 
H,W は整数
S 
i,j
​	
  は # または .
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
 
S 
2,1
​	
 S 
2,2
​	
 …S 
2,W
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
答えを出力せよ。

入力例 1
Copy
9 9
.........
.........
.........
.........
....#....
.........
.........
.........
.........
出力例 1
Copy
57
操作によってマス目は以下のように変化します。（上の数字は操作回数を表しており、10 回目の操作後まで表示しています。）



最終的に黒く塗られたマスは 57 個です。

入力例 2
Copy
2 2
..
..
出力例 2
Copy
0
入力例 3
Copy
10 10
..........
....#.....
#.......#.
......#...
.......#..
.....#....
..........
..........
..#...#...
.......#..
出力例 3
Copy
64
"""
H, W = map(int, input().split())
S = [list(input()) for i in range(H)]
dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def in_grid(x, y):
    return 0 <= x < H and 0 <= y < W
def count(x, y):
    c = 0
    for dx, dy in dxdy:
        nx, ny = x + dx, y + dy
        if in_grid(nx, ny) and S[nx][ny] == "#":
            c += 1
    return c
for i in range(H * W):
    if i == 0:
        T = []
        for x in range(H):
            for y in range(W):
                if S[x][y] == "." and count(x, y) == 1:
                    T.append((x, y))
    else:
        nT = []
        for x, y in T:
            for dx, dy in dxdy:
                nx, ny = x + dx, y + dy
                if in_grid(nx, ny) and S[nx][ny] == "." and count(nx, ny) == 1:
                    nT.append((nx, ny))
        T = nT
    if len(T) == 0:
        break
    for x, y in T:
        S[x][y] = "#"
ans = 0
for x in range(H):
    for y in range(W):
        ans += int(S[x][y] == "#")
print(ans)
