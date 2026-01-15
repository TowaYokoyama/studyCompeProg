"""
AtCorder.ABC.430.D の Docstring
問題文
数直線があり、最初は座標 0 に人 0 がひとりで立っています。

これから、人 1,2,…,N がこの順に到着し、数直線上に立ちます。
人 i は座標 X 
i
​	
  に立ちます。なお、 X 
i
​	
 ≥1 であり、全ての人について X 
i
​	
  は相異なります。

人が到着するたびに、以下の問いに答えてください。

現在数直線に人 0,1,…,r の r+1 人が立っているとする。
このとき、 d 
i
​	
  を「人 i に最も近い別の人までの距離」と定義する。
より厳密には、 d 
i
​	
 = 
0≤j≤r,j

=i
min
​	
 ∣X 
i
​	
 −X 
j
​	
 ∣ とする。
この d の総和、すなわち  
i=0
∑
r
​	
 d 
i
​	
  を求めよ。
制約
入力は全て整数
1≤N≤5×10 
5
 
1≤X 
i
​	
 ≤10 
9
 
i

=j ならば X 
i
​	
 

=X 
j
​	
 
入力
入力は以下の形式で標準入力から与えられる。

N
X 
1
​	
  X 
2
​	
  … X 
N
​	
 
出力
N 行に出力せよ。
そのうち i ( 1≤i≤N ) 行目には、人 i が到着した時点での問いの答えを出力せよ。

入力例 1
Copy
10
5 2 7 4 108728325 390529120 597713292 322456626 845148281 812604915
出力例 1
Copy
10
7
8
8
108728326
390529121
523096670
452057486
699492475
517144218
この入力では、人が 10 人到着します。
このうち最初の 4 人について説明します。

人 1 が到着した時点で、座標 0,5 に人がいます。
求める値は 5+5=10 です。
人 2 が到着した時点で、座標 0,2,5 に人がいます。
求める値は 2+2+3=7 です。
人 3 が到着した時点で、座標 0,2,5,7 に人がいます。
求める値は 2+2+2+2=8 です。
人 4 が到着した時点で、座標 0,2,4,5,7 に人がいます。
求める値は 2+2+1+1+2=8 です。
"""
# ABC430 D
# pip install sortedcontainers が必要（AtCoderでは使えます）

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# ---- Treap (set用) ----
import random
class Node:
    __slots__ = ("k", "p", "l", "r")
    def __init__(self, k):
        self.k = k
        self.p = random.random()
        self.l = None
        self.r = None

def rotate_right(t):
    s = t.l
    t.l = s.r
    s.r = t
    return s

def rotate_left(t):
    s = t.r
    t.r = s.l
    s.l = t
    return s

def insert(t, k):
    if t is None:
        return Node(k)
    if k < t.k:
        t.l = insert(t.l, k)
        if t.l.p < t.p:
            t = rotate_right(t)
    else:
        t.r = insert(t.r, k)
        if t.r.p < t.p:
            t = rotate_left(t)
    return t

def lower_bound(t, k):
    # 最小の >=k
    res = None
    while t:
        if t.k >= k:
            res = t.k
            t = t.l
        else:
            t = t.r
    return res

def predecessor(t, k):
    # 最大の <k
    res = None
    while t:
        if t.k < k:
            res = t.k
            t = t.r
        else:
            t = t.l
    return res

# ---- 問題本体 ----
N = int(input())
X = list(map(int, input().split()))

root = None
root = insert(root, 0)

INF = 10**18
mp = {}   # mp[x] = 人xの最近接距離
res = 0

# 最初の1人
x = X[0]
root = insert(root, x)
mp[0] = x
mp[x] = x
res = 2 * x
print(res)

for x in X[1:]:
    # 左右を探す
    R = lower_bound(root, x)
    L = predecessor(root, x)

    root = insert(root, x)
    mp[x] = INF

    # 左右の人だけ更新（差分）
    for nx in (L, R):
        if nx is None:
            continue
        old = mp[nx]
        new = min(old, abs(nx - x))
        res += new - old
        mp[nx] = new
        mp[x] = min(mp[x], abs(nx - x))

    res += mp[x]
    print(res)
