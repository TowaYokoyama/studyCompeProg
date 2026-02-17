"""
AtCorder.ADT.all1600~2.16.G の Docstring
整数 N が与えられます。以下の条件を満たす N 以下の正整数の組 (i,j) の個数を求めてください。

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
(1,1),(1,4),(2,2),(3,3),(4,1),(4,4) の 6 個が条件を満たします。

(2,3) は 2×3=6 が平方数でないため条件を満たしません。

入力例 2
Copy
254
出力例 2
Copy
896
"""

"""
i = (平方部分) × (平方じゃない部分)
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

a = []
for _ in range(M):
    c = int(input())
    arr = list(map(int, input().split()))
    a.append(arr)

ans = 0

# 0 から (1<<M)-1 まで全部試す
for b in range(1 << M):
    s = set()

    for i in range(M):
        if (b >> i) & 1:
            for x in a[i]:
                s.add(x)

    if len(s) == N:
        ans += 1

print(ans)
