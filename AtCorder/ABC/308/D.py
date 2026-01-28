"""
AtCorder.ABC.308.D の Docstring

問題文
H 行 W 列のグリッドがあります。 以下、上から i 行目、左から j 列目のマスを (i,j) と表記します。 グリッドの各マスには英小文字が書かれており、(i,j) に書かれた文字は与えられる文字列 S 
i
​	
  の j 文字目と一致します。

すぬけくんは、辺で隣接するマスに移動することを繰り返して (1,1) から (H,W) まで移動しようと思っています。 訪れるマス （最初の (1,1) と 最後の (H,W) を含む）に書かれた文字が、 訪れる順に s → n → u → k → e → s → n →… となるような経路が存在するか判定してください。 なお、2 つのマス (i 
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
 ) は ∣i 
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
 ∣=1 を満たすとき、またそのときに限り「辺で隣接する」といいます。

より厳密には、マスの列 ((i 
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
 ),…,(i 
k
​	
 ,j 
k
​	
 )) であって以下の条件を全て満たすものが存在するか判定してください。

(i 
1
​	
 ,j 
1
​	
 )=(1,1),(i 
k
​	
 ,j 
k
​	
 )=(H,W)
すべての t (1≤t<k) について、(i 
t
​	
 ,j 
t
​	
 ) と (i 
t+1
​	
 ,j 
t+1
​	
 ) は辺で隣接する
すべての t (1≤t≤k) について、(i 
t
​	
 ,j 
t
​	
 ) に書かれた文字は snuke の ((t−1)mod5)+1 文字目と一致する
制約
2≤H,W≤500
H,W は整数
S 
i
​	
  は英小文字からなる長さ W の文字列
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
問題文中の条件を満たす経路が存在するならば Yes を、存在しないならば No を出力せよ。

入力例 1
Copy
2 3
sns
euk
出力例 1
Copy
Yes
(1,1)→(1,2)→(2,2)→(2,3) という経路は、訪れたマスに書かれた文字が訪れた順に s → n → u → k となるため条件を満たします。

入力例 2
Copy
2 2
ab
cd
出力例 2
Copy
No
入力例 3
Copy
5 7
skunsek
nukesnu
ukeseku
nsnnesn
uekukku
出力例 3
Copy
Yes
"""
from collections import deque

H,W = map(int,input().split())
S = []
for _ in range(H):
    s = input()
    S.append(s) 

"""
s → n → u → k → e → s → n →って言うルートを通れるかどうかのお話
"""

dirs = [(1,0),(0,1),(-1,0),(0,-1)]

# visited[x][y][i] := (x,y) に snuke[i] として到達したか
visited = [[[False]*5 for _ in range(W)] for _ in range(H)]

# snuke ロジック
A = "snuke"

sx,sy = 0,0
gx,gy = H-1,W-1

# スタートが s じゃなければ無理
if S[sx][sy] != "s":
    print("No")
    exit()

def bfs(sx,sy):
    queue = deque()
    queue.append((sx, sy, 0))   # 0 = 's'
    visited[sx][sy][0] = True 

    while queue:
        x,y,i = queue.popleft()

        # ゴール到達
        if x == gx and y == gy:
            return True

        next_i = (i + 1) % 5
        next_char = A[next_i]

        for dx,dy in dirs:
            nx,ny = x+dx,y+dy 
            if 0 <= nx < H and 0 <= ny < W:
                if not visited[nx][ny][next_i] and S[nx][ny] == next_char:
                    visited[nx][ny][next_i] = True
                    queue.append((nx, ny, next_i))

    return False

if bfs(sx, sy):
    print("Yes")
else:
    print("No")
