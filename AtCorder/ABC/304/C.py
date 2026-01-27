"""
題文
1,2,…,N の番号がついた N 人の人が二次元平面上におり、人 i は座標 (X 
i
​	
 ,Y 
i
​	
 ) で表される地点にいます。

人 1 がウイルスに感染しました。ウイルスに感染した人から距離が D 以内にいる人にウイルスはうつります。

ただし、距離はユークリッド距離、すなわち 2 点 (a 
1
​	
 ,a 
2
​	
 ) と (b 
1
​	
 ,b 
2
​	
 ) に対し、この 2 点間の距離が 
(a 
1
​	
 −b 
1
​	
 ) 
2
 +(a 
2
​	
 −b 
2
​	
 ) 
2
 
​	
  であるものとして定められています。

十分に時間が経過した、すなわち人 i がウイルスに感染しているならば 人 i との距離が D 以内にいるすべての人がウイルスに感染している状態になったときに、各 i について人 i がウイルスに感染しているか判定してください。

制約
1≤N,D≤2000
−1000≤X 
i
​	
 ,Y 
i
​	
 ≤1000
i

=j のとき (X 
i
​	
 ,Y 
i
​	
 )

=(X 
j
​	
 ,Y 
j
​	
 )
入力はすべて整数
入力
入力は以下の形式で標準入力から与えられる。

N D
X 
1
​	
  Y 
1
​	
 
X 
2
​	
  Y 
2
​	
 
⋮
X 
N
​	
  Y 
N
​	
 
出力
N 行出力せよ。i 行目には、人 i がウイルスに感染しているならば Yes を、そうでないならば No を出力せよ。

入力例 1
Copy
4 5
2 -1
3 1
8 8
0 5
出力例 1
Copy
Yes
Yes
No
Yes
人 1 と人 2 の距離は  
5
​	
  であるため、人 2 はウイルスに感染します。
また、人 2 と人 4 の距離は 5 であるため、人 4 はウイルスに感染します。
人 3 は距離 5 以内に人がいないので、ウイルスに感染することはありません。

入力例 2
Copy
3 1
0 0
-1000 -1000
1000 1000
出力例 2
Copy
Yes
No
No
入力例 3
Copy
9 4
3 2
6 -1
1 6
6 5
-2 -3
5 3
2 -3
2 1
2 6
出力例 3
Copy
Yes
No
No
Yes
Yes
Yes
Yes
Yes
No
"""
from collections import deque
N,D = map(int,input().split())

points = []
for _ in range(N):
    x,y = map(int,input().split())
    points.append((x,y))
#print(points)
#[(2, -1), (3, 1), (8, 8), (0, 5)]
visited = [False] * N 
visited[0] = True #人１がウイルスになってる

def bfs():
  queue = deque([0])
  while queue:
    v = queue.popleft()
    x1, y1 = points[v]
    
    for u in range(N):
      if not visited[u]:
        x2,y2 = points[u]
        if (x1-x2)**2 + (y1-y2) ** 2 <= D*D:
          visited[u] = True 
          queue.append(u)

bfs()

for i in range(N):
  if visited[i]:
     print("Yes")
  else:
    print("No")