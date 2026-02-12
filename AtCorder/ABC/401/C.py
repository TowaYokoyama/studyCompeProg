"""
AtCorder.ABC.401.C の Docstring
問題文
正整数 N,K が与えられます。長さ N+1 の数列 A=(A 
0
​	
 ,A 
1
​	
 ,…,A 
N
​	
 ) の各要素の値を、以下の方法で定義します。

0≤i<K のとき、 A 
i
​	
 =1
K≤i のとき、 A 
i
​	
 =A 
i−K
​	
 +A 
i−K+1
​	
 +…+A 
i−1
​	
 
A 
N
​	
  を 10 
9
  で割ったあまりを求めてください。

制約
1≤N,K≤10 
6
 
入力される数値は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N K
出力
答えを出力せよ。

入力例 1
Copy
4 2
出力例 1
Copy
5
A 
0
​	
 =A 
1
​	
 =1 であり、A 
2
​	
 =A 
0
​	
 +A 
1
​	
 =2,A 
3
​	
 =A 
1
​	
 +A 
2
​	
 =3,A 
4
​	
 =A 
2
​	
 +A 
3
​	
 =5 となります。

入力例 2
Copy
10 20
出力例 2
Copy
1
入力例 3
Copy
1000000 500000
出力例 3
Copy
420890625
A 
N
​	
  を 10 
9
  で割ったあまりを出力することに注意してください
"""
mod = 10**9
N, K = map(int, input().split())

if N < K:
    print(1)
    exit()

A = [1]*K
window_sum = K

for i in range(K, N+1):
    new_val = window_sum % mod
    A.append(new_val)
    window_sum += new_val
    window_sum -= A[i-K]

print(A[N] % mod)
