"""
AtCorder.awc.awc0004.E の Docstring
問題文
高橋君は N 個の整数からなる数列 A=(A 
1
​	
 ,A 
2
​	
 ,…,A 
N
​	
 ) を持っています。各要素 A 
i
​	
  は負の値をとることもあります。

高橋君はこの数列から連続する区間を選び、その要素の総和がちょうど整数 K に等しくなるようにしたいと考えています。ここで K は目標とする総和の値です。そのような区間の選び方が何通りあるかを求めてください。

より正確には、1≤l≤r≤N を満たす整数の組 (l,r) であって、

A 
l
​	
 +A 
l+1
​	
 +⋯+A 
r
​	
 =K

を満たすものの個数を求めてください。

制約
1≤N≤2×10 
5
 
−10 
9
 ≤K≤10 
9
 
−10 
9
 ≤A 
i
​	
 ≤10 
9
 
入力はすべて整数
入力
Copy
N K
A 
1
​	
  A 
2
​	
  ⋯ A 
N
​	
 
1 行目には、数列の要素数を表す整数 N と、目標とする総和の値を表す整数 K が、スペース区切りで与えられる。
2 行目には、数列の各要素を表す整数 A 
1
​	
 ,A 
2
​	
 ,…,A 
N
​	
  が、スペース区切りで与えられる。
出力
条件を満たす整数の組 (l,r) の個数を 1 行で出力せよ。

入力例 1
Copy
5 5
1 2 3 4 5
出力例 1
Copy
2
入力例 2
Copy
6 3
1 -1 2 3 -2 4
出力例 2
Copy
3
入力例 3
Copy
10 0
1 -1 0 0 2 -2 0 3 -3 0
出力例 3
Copy
28
"""
from collections import defaultdict 

N,K =map(int,input().split())
A = list(map(int,input().split()))

count = defaultdict(int)
count[0] = 1 
prefix = 0
ans = 0

for a in A:
  prefix+=a 
  ans += count[prefix - K]
  count[prefix] += 1
  
print(ans)