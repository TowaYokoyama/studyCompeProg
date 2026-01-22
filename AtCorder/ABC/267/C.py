"""
AtCorder.ABC.267.C の Docstring

長さ N の整数列 A=(A 
1
​	
 ,A 
2
​	
 ,…,A 
N
​	
 ) が与えられます。

長さ M の A の連続部分列 B=(B 
1
​	
 ,B 
2
​	
 ,…,B 
M
​	
 ) に対する、 
i=1
∑
M
​	
 i×B 
i
​	
  の最大値を求めてください。

注記
数列の連続部分列とは、数列の先頭から 0 個以上、末尾から 0 個以上の要素を削除して得られる列のことをいいます。

例えば (2,3) や (1,2,3) は (1,2,3,4) の連続部分列ですが、(1,3) や (3,2,1) は (1,2,3,4) の連続部分列ではありません。

制約
1≤M≤N≤2×10 
5
 
−2×10 
5
 ≤A 
i
​	
 ≤2×10 
5
 
入力は全て整数。
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
 
出力
答えを出力せよ。

入力例 1
Copy
4 2
5 4 -1 8
出力例 1
Copy
15
B=(A 
3
​	
 ,A 
4
​	
 ) とした場合、 
i=1
∑
M
​	
 i×B 
i
​	
 =1×(−1)+2×8=15 となります。16 以上の値を達成することはできないため、解は 15 です。

B=(A 
1
​	
 ,A 
4
​	
 ) などを選ぶことができないことに注意してください。

入力例 2
Copy
10 4
-3 1 -4 1 -5 9 -2 6 -5 3
出力例 2
Copy
31

"""
N,M = map(int,input().split())
A = list(map(int,input().split()))

#最初の区間の値
cur = 0
for i in range(M):
    cur += (i+1) * A[i]
    
#区間和
window_sum = sum(A[:M])

ans = cur

for l in range(N-M):
    cur = cur - window_sum + M * A[l+M]
    window_sum = window_sum - A[l] + A[l+M]
    ans = max(ans,cur)
    
print(ans) 