"""
AtCorder.ADT.217.All1600~.D の Docstring
xy 平面上に N 人の人 1,2,…,N がおり、人 i は座標 (X 
i
​	
 ,Y 
i
​	
 ) にいます。
このうち、 K 人の人 A 
1
​	
 ,A 
2
​	
 ,…,A 
K
​	
  に同じ強さの明かりを持たせます。
座標 (x,y) にいる人が強さ R の明かりを持っている時、その明かりによって中心 (x,y) 、半径 R の円の内部全体(境界を含む)が照らされます。
すべての人が少なくとも 1 つの明かりによって照らされるために必要な明かりの強さの最小値を求めてください。

制約
入力は全て整数
1≤K<N≤1000
1≤A 
1
​	
 <A 
2
​	
 <⋯<A 
K
​	
 ≤N
∣X 
i
​	
 ∣,∣Y 
i
​	
 ∣≤10 
5
 
i

=j ならば (X 
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
入力
入力は以下の形式で標準入力から与えられる。

N K
A 
1
​	
  A 
2
​	
  … A 
K
​	
 
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
答えを実数として出力せよ。
出力された解と想定解との絶対誤差または相対誤差が 10 
−5
  以下であるならば、出力は正しいと見なされる。

入力例 1
Copy
4 2
2 3
0 0
0 1
1 2
2 0
出力例 1
Copy
2.23606797749978969
この入力では人が 4 人おり、そのうち人 2,3 が明かりを持ちます。
R≥ 
5
​	
 ≈2.236068 である時、すべての人が少なくとも 1 つの明かりによって照らされます。

入力例 2
Copy
2 1
2
-100000 -100000
100000 100000
出力例 2
Copy
282842.712474619009
入力例 3
Copy
8 3
2 6 8
-17683 17993
93038 47074
58079 -57520
-41515 -89802
-72739 68805
24324 -73073
71049 72103
47863 19268
出力例 3
Copy
130379.280458974768
"""
import math

N, K = map(int, input().split())
A = list(map(int, input().split()))
A = [a-1 for a in A]  # 0-index化

coords = []
for _ in range(N):
    x, y = map(int, input().split())
    coords.append((x, y))

answer = 0

for i in range(N):
    x1, y1 = coords[i]
    min_dist = float('inf')
    
    for a in A:
        x2, y2 = coords[a]
        dx = x1 - x2
        dy = y1 - y2
        dist = math.sqrt(dx*dx + dy*dy)
        min_dist = min(min_dist, dist)
    
    answer = max(answer, min_dist)

print(answer)
