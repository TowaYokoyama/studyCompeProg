"""
問題文
長さ N の正整数列 A=(A 
1
​	
 ,A 
2
​	
 ,…,A 
N
​	
 ) および整数 x,y が与えられます。
次の条件をすべて満たすように、xy 座標平面上に N+1 個の点 p 
1
​	
 ,p 
2
​	
 ,…,p 
N
​	
 ,p 
N+1
​	
  を配置することができるか判定してください。(同じ座標に 2 個以上の点を配置してもよいです。)

p 
1
​	
 =(0,0)
p 
2
​	
 =(A 
1
​	
 ,0)
p 
N+1
​	
 =(x,y)
点 p 
i
​	
  と点 p 
i+1
​	
  の距離は A 
i
​	
  (1≤i≤N)
線分 p 
i
​	
 p 
i+1
​	
  と線分 p 
i+1
​	
 p 
i+2
​	
  のなす角は 90 度 (1≤i≤N−1)
制約
2≤N≤10 
3
 
1≤A 
i
​	
 ≤10
∣x∣,∣y∣≤10 
4
 
入力される値はすべて整数
入力
入力は以下の形式で標準入力から与えられる。

N x y
A 
1
​	
  A 
2
​	
  … A 
N
​	
 
出力
問題文の条件をすべて満たすように p 
1
​	
 ,p 
2
​	
 ,…,p 
N
​	
 ,p 
N+1
​	
  を配置することができる場合は Yes を、そうでない場合は No を出力せよ。

入力例 1
Copy
3 -1 1
2 1 3
出力例 1
Copy
Yes
xy 座標平面に p 
1
​	
 =(0,0),p 
2
​	
 =(2,0),p 
3
​	
 =(2,1),p 
4
​	
 =(−1,1) として点を配置したのが以下の図です。これは問題文の条件をすべて満たしています。



入力例 2
Copy
5 2 0
2 2 2 2 2
出力例 2
Copy
Yes
p 
1
​	
 =(0,0),p 
2
​	
 =(2,0),p 
3
​	
 =(2,2),p 
4
​	
 =(0,2),p 
5
​	
 =(0,0),p 
6
​	
 =(2,0) とすれば問題文の条件をすべて満たすことができます。同じ座標に複数の点を置いてもよいのに注意してください。

入力例 3
Copy
4 5 5
1 2 3 4
出力例 3
Copy
No
入力例 4
Copy
3 2 7
2 7 4
出力例 4
Copy
No
入力例 5
Copy
10 8 -7
6 10 4 1 5 9 8 6 5 1
出力例 5
Copy
Yes
"""
N, x, y = map(int, input().split())
A = list(map(int, input().split()))

# x方向とy方向に分ける
x_moves = A[::2]   # A1, A3, A5, ...
y_moves = A[1::2]  # A2, A4, A6, ...

# --- x方向 ---
# 最初の A1 は必ず +x に使われる
target_x = x - x_moves[0]

possible_x = {0}
for a in x_moves[1:]:
    next_set = set()
    for v in possible_x:
        next_set.add(v + a)
        next_set.add(v - a)
    possible_x = next_set

# --- y方向 ---
possible_y = {0}
for a in y_moves:
    next_set = set()
    for v in possible_y:
        next_set.add(v + a)
        next_set.add(v - a)
    possible_y = next_set

# 判定
if target_x in possible_x and y in possible_y:
    print("Yes")
else:
    print("No")
