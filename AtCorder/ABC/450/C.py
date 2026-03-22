"""
縦 H 行、横 W 列のグリッドがあります。
上から i 行目左から j 列目のマスは S 
i,j
​	
  が # のとき黒く、 . のとき白く塗られています。

白マスからなる四方位に連結な領域のうち、黒マスに囲まれたものの個数を求めてください。

より厳密には次の通りです。

上から i 行目左から j 列目のマスをマス (i,j) と表します。
2 つのマス (i,j),(i 
′
 ,j 
′
 ) が隣接しているとは、∣i−i 
′
 ∣+∣j−j 
′
 ∣=1 であることと定めます。
白マスの集合 C が連結であるとは、C に属するどの 2 マス c,c 
′
  に対しても、C に属する隣接するマスへの移動を繰り返すことで c から c 
′
  へ移動できることと定めます。
空でない白マスの連結な集合であって、極大なものを白マスの連結成分と定めます。
白マスの連結成分であって、グリッドの最外周（すなわち、 1 行目、 H 行目、 1 列目、 W 行目）のマスを含まないものの個数を求めてください。

制約
3≤H,W≤10 
3
 
H,W は整数
S 
i,j
​	
  は # か .
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
答えを出力せよ。

入力例 1
Copy
5 15
##########..###
#...#######.###
####....###..##
######.########
########....###
出力例 1
Copy
2
上から 2 行目左から 2,3,4 列目の 3 マスからなる領域と、上から 3 行目左から 5,6,7,8 列目及び上から 4 行目左から 7 列目の計 5 マスからなる領域の 2 個です。

入力例 2
Copy
10 22
######################
####.#################
###...################
##.###.##.....########
##.....##.####.#######
.######.#......#.....#
.######.#.####.#.#####
#########.....##.#####
################.#####
################.....#
出力例 2
Copy
4
"""
from collections import deque 
H,W = map(int,input().split())
grid = [list(input())for _ in range(H)]
# print(grid)
#4方位に"#"が存在すればok <=>外周に触れていない白連結成分
dirs = [(1,0),(0,1),(-1,0),(0,-1)]
visited = [[False]*W for _ in range(H)]
# sx,sy = 0,0
def bfs(si,sj):
    queue = deque()
    queue.append((si,sj))
    touches_edge = False#外周に触れたかどうか
    visited[si][sj] = True
    while queue:
        i,j = queue.popleft()
        if i == 0 or i == H-1 or j == W-1 or j == 0 :
            touches_edge = True #外周マスだったら記録
        for di,dj in dirs:
            ni,nj = i+di,j+dj 
            if 0<= ni < H and 0<= nj < W and not visited[ni][nj] and grid[ni][nj] == '.':
                visited[ni][nj] = True
                queue.append((ni,nj))
    return touches_edge  # ← 外周に触れたかを返す

ans = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == '.' and not visited[i][j]:
            if not bfs(i, j):  # 外周に触れなかった = 囲まれてる
                ans += 1

print(ans)