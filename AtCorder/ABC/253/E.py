"""
AtCorder.ABC.253.E の Docstring
配点 : 
500 点

問題文
長さ 
N の整数からなる数列 
A=(A 
1
​
 ,…,A 
N
​
 ) であって、以下の条件を全て満たすものは何通りありますか？

1≤A 
i
​
 ≤M 
(1≤i≤N)

∣A 
i
​
 −A 
i+1
​
 ∣≥K 
(1≤i≤N−1)

ただし、答えは非常に大きくなることがあるので、答えを 
998244353 で割った余りを求めてください。

制約
2≤N≤1000
1≤M≤5000
0≤K≤M−1
入力は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N 
M 
K
出力
答えを 
998244353 で割った余りを出力せよ。

入力例 1
Copy
2 3 1
出力例 1
Copy
6
条件を満たす数列は以下の 
6 つです。

(1,2)
(1,3)
(2,1)
(2,3)
(3,1)
(3,2)
入力例 2
Copy
3 3 2
出力例 2
Copy
2
条件を満たす数列は以下の 
2 つです。

(1,3,1)
(3,1,3)
入力例 3
Copy
100 1000 500
出力例 3
Copy
657064711
答えを 
998244353 で割った余りを出力してください。

"""
"""


2≤N≤1000
1≤M≤5000
0≤K≤M−1
入力は全て整数


"""
N, M, K = map(int, input().split())
MOD = 998244353

# dp[x] = 現在の長さで、最後が x の通り数
dp = [0] * (M + 1)
for x in range(1, M + 1):
    dp[x] = 1

for _ in range(N - 1):
    # prefix[i] = dp[1] + ... + dp[i]
    prefix = [0] * (M + 1)
    for i in range(1, M + 1):
        prefix[i] = (prefix[i - 1] + dp[i]) % MOD

    total = prefix[M]
    ndp = [0] * (M + 1)

    if K == 0:
        for y in range(1, M + 1):
            ndp[y] = total
    else:
        for y in range(1, M + 1):
            # ダメ: |x-y| < K → x ∈ [y-K+1, y+K-1]
            l = max(1, y - K + 1)
            r = min(M, y + K - 1)
            bad = (prefix[r] - prefix[l - 1]) % MOD
            ndp[y] = (total - bad) % MOD

    dp = ndp

print(sum(dp) % MOD)
