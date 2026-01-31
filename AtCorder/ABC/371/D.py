"""
AtCorder.ABC.371.D の Docstring
数直線上に N 個の村があります。i 番目の村は座標 X 
i
​	
  にあり、P 
i
​	
  人の村人がいます。

Q 個のクエリに答えてください。i 番目のクエリは以下の形式です。

整数 L 
i
​	
 ,R 
i
​	
  が与えられる。座標が L 
i
​	
  以上 R 
i
​	
  以下の村に住んでいる村人の人数の総数を求めよ。
制約
1≤N,Q≤2×10 
5
 
−10 
9
 ≤X 
1
​	
 <X 
2
​	
 <…<X 
N
​	
 ≤10 
9
 
1≤P 
i
​	
 ≤10 
9
 
−10 
9
 ≤L 
i
​	
 ≤R 
i
​	
 ≤10 
9
 
入力される数値は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N
X 
1
​	
  … X 
N
​	
 
P 
1
​	
  … P 
N
​	
 
Q
L 
1
​	
  R 
1
​	
 
⋮
L 
Q
​	
  R 
Q
​	
  
出力
Q 行出力せよ。

i (1≤i≤Q) 行目には、i 番目のクエリに対する答えを出力せよ。

入力例 1
Copy
4
1 3 5 7
1 2 3 4
4
1 1
2 6
0 10
2 2
出力例 1
Copy
1
5
10
0
1 番目のクエリについて考えます。座標が 1 以上 1 以下の村は、座標 1 にある村で、村人は 1 人います。よって答えは 1 です。

2 番目のクエリについて考えます。座標が 2 以上 6 以下の村は、座標 3 にある村と座標 5 にある村で、村人はそれぞれ 2 人と 3 人います。よって答えは 2+3=5 です。

入力例 2
Copy
7
-10 -5 -3 -1 0 1 4
2 5 6 5 2 1 7
8
-7 7
-1 5
-10 -4
-8 10
-5 0
-10 5
-8 7
-8 -3
出力例 2
Copy
26
15
7
26
18
28
26
11

"""
from bisect import bisect_left,bisect_right

N = int(input())
X = list(map(int,input().split()))
P = list(map(int,input().split()))

S = [0]#累積和
for p in P:
    S.append(S[-1]+p)

Q = int(input())
for _ in range(Q):
    L,R = map(int,input().split())
    l = bisect_left(X,L)
    r = bisect_right(X,R)
    print(S[r] - S[l])