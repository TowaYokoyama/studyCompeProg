"""
AtCorder.ABC.433.D の Docstring
整数 x,y に対して f(x,y) を以下のように定義します。

先頭に余分な 0 を付けない十進表記の x,y をそれぞれ文字列として解釈しこの順に連結して得られる文字列を S としたときの、 S を十進表記の整数として解釈した値。
例えば f(12,3)=123 、f(100,40)=10040 です。

正整数 N,M と長さ N の正整数列 A=(A 
1
​	
 ,A 
2
​	
 ,…,A 
N
​	
 ) が与えられます。

以下の条件を全て満たす整数の組 (i,j) の個数を求めてください。

1≤i,j≤N
f(A 
i
​	
 ,A 
j
​	
 ) は M の倍数
制約
1≤N≤2×10 
5
 
1≤M≤10 
9
 
1≤A 
i
​	
 ≤10 
9
 
入力される値は全て整数
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
条件を全て満たす整数の組 (i,j) の個数を出力せよ。

入力例 1
Copy
2 11
2 42
出力例 1
Copy
2
(i,j)=(1,1) のとき： f(A 
1
​	
 ,A 
1
​	
 )=22 は 11 の倍数です。
(i,j)=(1,2) のとき： f(A 
1
​	
 ,A 
2
​	
 )=242 は 11 の倍数です。
(i,j)=(2,1) のとき： f(A 
2
​	
 ,A 
1
​	
 )=422 は 11 の倍数ではありません。
(i,j)=(2,2) のとき： f(A 
2
​	
 ,A 
2
​	
 )=4242 は 11 の倍数ではありません。
以上より、条件を全て満たす整数の組は (i,j)=(1,1),(1,2) の 2 つです。したがって、 2 を出力してください。

入力例 2
Copy
4 7
2 8 16 183
出力例 2
Copy
4
入力例 3
Copy
5 5
1000000000 1000000000 1000000000 1000000000 1000000000
出力例 3
Copy
25
入力例 4
Copy
12 13
80 68 862370 82217 8 56 5 168 672624 6 286057 11864
"""
N,M = map(int,input().split())
A = list(map(int,input().split()))

pow10 = [1] * 11
for i in range(1, 11):
    pow10[i] = (pow10[i - 1] * 10) % M

# 桁数ごとに (A[j] % M) の個数をカウント
# cnt[d] は dict: 余り -> 個数
from collections import defaultdict
cnt = [defaultdict(int) for _ in range(11)]

for a in A:
    d = len(str(a))
    cnt[d][a % M] += 1

ans = 0

# i を全探索、d は 1..10
for a in A:
    for d in range(1, 11):
        need = (-a * pow10[d]) % M
        ans += cnt[d].get(need, 0)

print(ans)
    
import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

# cnt[d][r] = 桁数 d、A[j] % M == r の個数
cnt = [defaultdict(int) for _ in range(11)]

for a in A:
    d = len(str(a))
    cnt[d][a % M] += 1

ans = 0

for a in A:
    for d in range(1, 11):
        # 10^d % M をその場で計算（前計算しない）
        need = (-a * pow(10, d, M)) % M
        ans += cnt[d].get(need, 0)

print(ans)
    