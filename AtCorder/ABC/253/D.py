"""
AtCorder.ABC.253.D の Docstring
D - FizzBuzz Sum Hard  / 
実行時間制限: 2 sec / メモリ制限: 1024 MiB

配点 : 
400 点

問題文
1 以上 
N 以下の整数であって、
A の倍数でも 
B の倍数でもないものの総和を求めてください。

制約
1≤N,A,B≤10 
9
 
入力は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N 
A 
B
出力
答えを出力せよ。

入力例 1
Copy
10 3 5
出力例 1
Copy
22
1 以上 
10 以下の整数で 
3 の倍数でも 
5 の倍数でもないのは 
1,2,4,7,8 です。それらの総和は 
1+2+4+7+8=22 です。

入力例 2
Copy
1000000000 314 159
出力例 2
Copy
495273003954006262
"""
N,A,B = map(int,input().split())
total = N*(N+1)//2 #1からNまでの和の公式

for i in range(1,N+1):
    if i % A == 0 or i % B == 0:
        total -= i


print(total)    

import math

N, A, B = map(int, input().split())

def sum_mul(x):
    k = N // x
    return x * k * (k + 1) // 2

ans = (
    N * (N + 1) // 2
    - sum_mul(A)
    - sum_mul(B)
    + sum_mul(A * B // math.gcd(A, B))
)

print(ans)
