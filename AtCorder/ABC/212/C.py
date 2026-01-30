"""
AtCorder.ABC.212.C の Docstring
題文
それぞれ N 個、M 個の正整数からなる 2 つの数列 A=(A 
1
​	
 ,A 
2
​	
 ,…,A 
N
​	
 ) と B=(B 
1
​	
 ,…,B 
M
​	
 ) が与えられます。

それぞれの数列から 1 つずつ要素を選んだときの 2 つの値の差の最小値、すなわち、  
1≤i≤N
min
​	
  
1≤j≤M
min
​	
 ∣A 
i
​	
 −B 
j
​	
 ∣ を求めてください。

制約
1≤N,M≤2×10 
5
 
1≤A 
i
​	
 ≤10 
9
 
1≤B 
i
​	
 ≤10 
9
 
入力は全て整数である。
入力
入力は以下の形式で標準入力から与えられる。

N M
A 
1
​	
  A 
2
​	
  … A 
N
​	
 
B 
1
​	
  B 
2
​	
  … B 
M
​	
 
出力
答えを出力せよ。

入力例 1
Copy
2 2
1 6
4 9
出力例 1
Copy
2
それぞれの数列から 1 つずつ要素を選んだときの 2 つの値の差としてあり得るのは、 ∣1−4∣=3 、 ∣1−9∣=8 、 ∣6−4∣=2 、 ∣6−9∣=3 の 4 つです。 この中で最小である 2 を出力します。

入力例 2
Copy
1 1
10
10
出力例 2
Copy
0
入力例 3
Copy
6 8
82 76 82 82 71 70
17 39 67 2 45 35 22 24
出力例 3
Copy
3

"""
from bisect import bisect_left
N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()

ans = 10 ** 30

for a in A:
    i = bisect_left(B,a)#a を B に入れるとしたら、この位置（インデックス）
    
    if i < M:
        ans = min(ans,abs(B[i]-a))
    if i > 0:
        ans = min(ans, abs(B[i-1]-a))

print(ans)