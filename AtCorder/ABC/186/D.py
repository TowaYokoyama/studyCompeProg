"""
AtCorder.ABC.186.D の Docstring
N 個の整数 A 
1
​	
 ,…,A 
N
​	
  が与えられます。

1≤i<j≤N を満たす全ての i,j の組についての ∣A 
i
​	
 −A 
j
​	
 ∣ の和を求めてください。

すなわち、 
i=1
∑
N−1
​	
  
j=i+1
∑
N
​	
 ∣A 
i
​	
 −A 
j
​	
 ∣ を求めてください。

制約
2≤N≤2×10 
5
 
∣A 
i
​	
 ∣≤10 
8
 
A 
i
​	
  は整数である。
入力
入力は以下の形式で標準入力から与えられる。

N
A 
1
​	
  … A 
N
​	
 
出力
答えを出力せよ。

入力例 1
Copy
3
5 1 2
出力例 1
Copy
8
∣5−1∣+∣5−2∣+∣1−2∣=8 です。

入力例 2
Copy
5
31 41 59 26 53
出力例 2
Copy
176
"""
N = int(input())
A = list(map(int,input().split()))

A.sort()

sum_left = 0
ans = 0

for j in range(N):
    ans += A[j] * j - sum_left
    sum_left += A[j]

print(ans)
