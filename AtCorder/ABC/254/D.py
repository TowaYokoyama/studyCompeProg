"""
AtCorder.ABC.254.D の Docstring

D - Together Square  / 
実行時間制限: 2 sec / メモリ制限: 1024 MiB

配点 : 
400 点

問題文
整数 
N が与えられます。以下の条件を満たす 
N 以下の正整数の組 
(i,j) の個数を求めてください。

i×j は平方数である。
制約
1≤N≤2×10 
5
 
N は整数である。
入力
入力は以下の形式で標準入力から与えられる。

N
出力
答えを出力せよ。

入力例 1
Copy
4
出力例 1
Copy
6
(1,1),(1,4),(2,2),(3,3),(4,1),(4,4) の 
6 個が条件を満たします。

(2,3) は 
2×3=6 が平方数でないため条件を満たしません。

入力例 2
Copy
254
出力例 2
Copy
896
"""
N = int(input())
from collections import defaultdict

def square_free(x):
    """x の平方因子をすべて取り除いた値を返す"""
    i = 2
    while i * i <= x:
        while x % (i * i) == 0:
            x //= i * i
        i += 1
    return x

cnt = defaultdict(int)

# 各 i を square-free に変換して数える
for i in range(1, N + 1):
    sf = square_free(i)
    cnt[sf] += 1

# 同じ square-free を持つもの同士は全部ペアOK
ans = 0
for v in cnt.values():
    ans += v * v

print(ans)