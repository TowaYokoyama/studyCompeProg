"""
AtCorder.ABC.266.C の Docstring
問題文
2 次元座標平面があります。x 軸正方向を右向き、y 軸正方向を上向きとします。

この平面上に自己交差のない四角形があります。
4 つの頂点の座標は反時計回りに (A 
x
​	
 ,A 
y
​	
 ),(B 
x
​	
 ,B 
y
​	
 ),(C 
x
​	
 ,C 
y
​	
 ),(D 
x
​	
 ,D 
y
​	
 ) です。

この四角形が凸であるか判定してください。

なお、四角形の 4 つの内角が全て 180 度未満であるとき、かつ、その時に限り、その四角形は凸であるといいます。

制約
−100≤A 
x
​	
 ,A 
y
​	
 ,B 
x
​	
 ,B 
y
​	
 ,C 
x
​	
 ,C 
y
​	
 ,D 
x
​	
 ,D 
y
​	
 ≤100
入力に含まれる値は全て整数である
与えられる 4 点は四角形の 4 頂点を反時計回りに並べたものである
与えられる 4 点のなす四角形は自己交差がなく退化していない。すなわち
どの 2 頂点も同じ座標にない
どの 3 頂点も同一直線上にない
隣接しない 2 辺は共有点を持たない
入力
入力は以下の形式で標準入力から与えられる。

A 
x
​	
  A 
y
​	
 
B 
x
​	
  B 
y
​	
 
C 
x
​	
  C 
y
​	
 
D 
x
​	
  D 
y
​	
 
出力
与えられる四角形が凸なら Yes、凸でないなら No を出力せよ。

入力例 1
Copy
0 0
1 0
1 1
0 1
出力例 1
Copy
Yes
与えられた四角形は正方形であり、4 つの内角は全て 90 度です。したがって、この四角形は凸です。

図

入力例 2
Copy
0 0
1 1
-1 0
1 -1
出力例 2
Copy
No
角 A が 270 度です。したがって、この四角形は凸ではありません。

図
"""

def cross(ax,ay,bx,by):
  return ax * by - ay * bx

A = tuple(map(int,input().split()))
B =  tuple(map(int,input().split()))
C =  tuple(map(int,input().split()))
D =   tuple(map(int,input().split()))

points = [A,B,C,D]
ok = True
for i in range(4):
  x1,y1 = points[i]
  x2,y2 = points[(i+1)%4]
  x3,y3 = points[(i+2)%4]
  
  #ベクトル
  v1x, v1y = x2 - x1, y2 - y1
  v2x, v2y = x3 - x2, y3 - y2
  
  if cross(v1x, v1y, v2x, v2y):
    ok = False 
    break 
  
print("Yes" if ok else "No")