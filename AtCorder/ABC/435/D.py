"""
AtCorder.ABC.435.D の Docstring
問題文
N 頂点 M 辺の有向グラフが与えられます。
頂点には 1 から N の番号がついており、i 番目の辺は頂点 X 
i
​	
  から頂点 Y 
i
​	
  への有向辺です。
最初全ての頂点は白色です。

Q 個のクエリが与えられるので順に処理してください。クエリは以下の 2 種類のいずれかです。

1 v：頂点 v を黒色にする
2 v：頂点 v から辺を辿って黒色の頂点に到達可能かどうか判定する
制約
1≤N≤3×10 
5
 
0≤M≤3×10 
5
 
1≤Q≤3×10 
5
 
1≤X 
i
​	
 ,Y 
i
​	
 ≤N
自己辺をもたない。すなわち X 
i
​	
 

=Y 
i
​	
 
多重辺をもたない。すなわち (X 
i
​	
 ,Y 
i
​	
 ) は相異なる
クエリにおいて 1≤v≤N
入力は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N M
X 
1
​	
  Y 
1
​	
 
⋮
X 
M
​	
  Y 
M
​	
 
Q
query 
1
​	
 
⋮
query 
Q
​	
 
query 
i
​	
  は i 番目のクエリを表し、以下のいずれかの形式で与えられる。

1 v
2 v
出力
2 種類目のクエリの個数を q として q 行出力せよ。

i 行目には、i 番目の 2 種類目のクエリにおいて到達可能なら Yes、到達不可能なら No と出力せよ。

入力例 1
Copy
5 6
1 2
2 3
3 1
4 5
1 4
2 5
5
1 3
2 1
2 4
1 5
2 4
出力例 1
Copy
Yes
No
Yes
最初、与えられたグラフは下図一番左の通りです。
1 番目のクエリにより頂点 3 が黒色になり、下図中央のようになります。
2 番目のクエリにおいて、頂点 1 から黒色の頂点 3 に到達可能です。
3 番目のクエリにおいて、頂点 4 から黒色の頂点に到達することはできません。
4 番目のクエリにより頂点 5 が黒色になり、下図右のようになります。

"""
from collections import deque 
N,M = map(int,input().split())
# 逆グラフを作る
rev = [[] for _ in range(N)]
for _ in range(M):
    x,y = map(int,input().split())
    x -=1
    y-=1
    rev[y].append(x) #逆向き
    
Q = int(input())

#good[v] = vから黒に到達できるか
good = [False] * N

#BFS用キュー
q = deque()

#クエリ処理
for _ in range(Q):
    t,v = map(int,input().split())
    v-=1
    
    if t == 1:
        #vを黒にする
        if not good[v]:
            good[v] = True
            q.append(v)
            
            #逆グラフでbfs
            while q:
                cur = q.popleft()
                for nxt in rev[cur]:
                    if not good[nxt]:
                        good[nxt] = True
                        q.append(nxt)
                        
    else:
        #到達可能か？
        print("Yes" if good[v] else "No")