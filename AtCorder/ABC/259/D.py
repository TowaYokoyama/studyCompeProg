"""
AtCorder.ABC.259.D の Docstring
xy -平面上の N 個の円が与えられます。 i=1,2,…,N について、i 番目の円は点 (x 
i
​	
 ,y 
i
​	
 ) を中心とする半径 r 
i
​	
  の円です。

N 個の円のうち少なくとも 1 つ以上の円の円周上にある点のみを通って、点 (s 
x
​	
 ,s 
y
​	
 ) から点 (t 
x
​	
 ,t 
y
​	
 ) に行くことができるかどうかを判定してください。

制約
1≤N≤3000
−10 
9
 ≤x 
i
​	
 ,y 
i
​	
 ≤10 
9
 
1≤r 
i
​	
 ≤10 
9
 
(s 
x
​	
 ,s 
y
​	
 ) は N 個の円のうち少なくとも 1 つ以上の円の円周上にある
(t 
x
​	
 ,t 
y
​	
 ) は N 個の円のうち少なくとも 1 つ以上の円の円周上にある
入力はすべて整数
入力
入力は以下の形式で標準入力から与えられる。

N
s 
x
​	
  s 
y
​	
  t 
x
​	
  t 
y
​	
 
x 
1
​	
  y 
1
​	
  r 
1
​	
 
x 
2
​	
  y 
2
​	
  r 
2
​	
 
⋮
x 
N
​	
  y 
N
​	
  r 
N
​	
 
出力
点 (s 
x
​	
 ,s 
y
​	
 ) から点 (t 
x
​	
 ,t 
y
​	
 ) に行くことができる場合は Yes を、そうでない場合は No を出力せよ。 ジャッジは英小文字と英大文字を厳密に区別することに注意せよ。

入力例 1
Copy
4
0 -2 3 3
0 0 2
2 0 2
2 3 1
-3 3 3
出力例 1
Copy
Yes


例えば、下記の経路で点 (0,−2) から点 (3,3) へ行くことができます。

点 (0,−2) から 1 つ目の円の円周上を反時計回りに通って点 (1,− 
3
​	
 ) へ行く。
点 (1,− 
3
​	
 ) から 2 つ目の円の円周上を時計回りに通って点 (2,2) へ行く。
点 (2,2) から 3 つ目の円の円周上を反時計回りに通って点 (3,3) へ行く。
よって、Yes を出力します。

入力例 2
Copy
3
0 1 0 3
0 0 1
0 0 2
0 0 3
出力例 2
Copy
No


少なくとも 1 つ以上の円の円周上にある点のみを通って点 (0,1) から点 (0,3) に行くことはできないので No を出力します。


"""
from collections import deque

N = int(input())
sx, sy, tx, ty = map(int, input().split())

circles = []
for _ in range(N):
    x, y, r = map(int, input().split())
    circles.append((x, y, r))

# どの円がスタート・ゴールを含むか
start = -1
goal = -1

for i in range(N):
    x, y, r = circles[i]
    if (sx - x) ** 2 + (sy - y) ** 2 == r ** 2:
        start = i
    if (tx - x) ** 2 + (ty - y) ** 2 == r ** 2:
        goal = i

# BFS
visited = [False] * N
q = deque([start])
visited[start] = True

while q:
    v = q.popleft()
    if v == goal:
        print("Yes")
        exit()

    x1, y1, r1 = circles[v]

    for i in range(N):
        if visited[i]:
            continue
        x2, y2, r2 = circles[i]

        dx = x1 - x2
        dy = y1 - y2
        d2 = dx * dx + dy * dy

        # 円が接する or 交差している条件
        if (r1 - r2) ** 2 <= d2 <= (r1 + r2) ** 2:
            visited[i] = True
            q.append(i)

print("No")
