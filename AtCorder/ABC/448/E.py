"""

数 N,M が与えられるので、 ⌊N/M⌋ を 10007 で割った余りを求めてください。
ここで、 ⌊x⌋ は x 以下で最大の整数を表します。 例えば、 ⌊3.14⌋=3,⌊10⌋=10 です。

但し、この問題では N は直接与えられず、ランレングス圧縮された形で与えられます。
具体的には、 N は K 個の「数字 c 
i
​	
  と整数 l 
i
​	
  の組」からなる列で表現されます。
元の N を復元するには、以下の手順を用います。

最初、文字列 S を空文字列とする。
i=1,2,…,K について、以下を繰り返す。
S の末尾に数字 c 
i
​	
  を l 
i
​	
  個付け加える。
最終的な S をひとつの整数として解釈したとき、その整数が N である。
制約
1≤M≤10 
4
 
1≤K≤10 
5
 
c 
i
​	
  は 0,1,2,3,4,5,6,7,8,9 いずれかの数字
1≤l 
i
​	
 ≤10 
9
 
c 
1
​	
 

=0
M,K,l 
i
​	
  は整数
入力
入力は以下の形式で標準入力から与えられる。

K M
c 
1
​	
  l 
1
​	
 
c 
2
​	
  l 
2
​	
 
⋮
c 
K
​	
  l 
K
​	
 
出力
答えを出力せよ。

入力例 1
Copy
6 7
3 1
1 1
6 1
2 2
7 2
6 2
出力例 1
Copy
3797
この入力では N=316227766,M=7 です。
⌊316227766/7⌋=45175395 であり、これを 10007 で割った余りである 3797 が最終的な答えとなります。

入力例 2
Copy
1 1
1 1
出力例 2
Copy
1
入力例 3
Copy
10 9999
9 419921892
9 923650333
6 476449815
1 8837775
2 141135534
5 462618481
3 202652735
0 771538044
4 321458589
0 570032864
出力例 3
Copy
8437
"""
import sys
input = sys.stdin.readline

k, m = map(int, input().split())

mod = m * 10007

c = []
l = []

for _ in range(k):
    ci, li = map(int, input().split())
    c.append(ci)
    l.append(li)


def power(a, b):
    res = 1
    cur = a % mod
    while b > 0:
        if b & 1:
            res = (res * cur) % mod
        cur = (cur * cur) % mod
        b >>= 1
    return res


# 10^(2^d)
pow_keep = [0] * 30
pow_keep[0] = 10 % mod
for d in range(1, 30):
    pow_keep[d] = (pow_keep[d-1] * pow_keep[d-1]) % mod


# R_(2^d)
Rpow2 = [0] * 30
Rpow2[0] = 1
for d in range(1, 30):
    Rpow2[d] = (Rpow2[d-1] * pow_keep[d-1] + Rpow2[d-1]) % mod


res = 0
dgt = 0

for i in range(k-1, -1, -1):

    ce = (c[i] * power(10, dgt)) % mod

    R = 0
    for d in range(29, -1, -1):
        if l[i] & (1 << d):
            R = (R * pow_keep[d] + Rpow2[d]) % mod

    res = (res + ce * R) % mod

    dgt += l[i]


print(res // m)