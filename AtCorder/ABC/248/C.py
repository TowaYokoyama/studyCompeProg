"""
AtCorder.ABC.248.C の Docstring
問題文
長さ N の整数からなる数列 A=(A 
1
​	
 ,…,A 
N
​	
 ) であって、以下の条件を全て満たすものは何通りありますか？

1≤A 
i
​	
 ≤M (1≤i≤N)

i=1
∑
N
​	
 A 
i
​	
 ≤K

ただし、答えは非常に大きくなることがあるので、答えを 998244353 で割った余りを求めてください。

制約
1≤N,M≤50
N≤K≤NM
入力は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N M K
出力
答えを 998244353 で割った余りを出力せよ。

入力例 1
Copy
2 3 4
出力例 1
Copy
6
条件を満たす数列は以下の 6 つです。

(1,1)
(1,2)
(1,3)
(2,1)
(2,2)
(3,1)
入力例 2
Copy
31 41 592
出力例 2
Copy
798416518
答えを 998244353 で割った余りを出力してください。
"""
import sys

MOD = 998244353

N, M, K = map(int, input().split())

dp = [[0] * (K + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    for j in range(K + 1):
        if dp[i][j] == 0:
            continue
        for k in range(1, M + 1):
            if j + k <= K:
                dp[i + 1][j + k] = (dp[i + 1][j + k] + dp[i][j]) % MOD

ans = sum(dp[N][1:K + 1]) % MOD
print(ans)
