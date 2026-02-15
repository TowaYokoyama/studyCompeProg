"""
AtCorder.ABC.445.C の Docstring
マス 1, マス 2,…, マス N の N 個のマスが 1 列に並んでいます。 マス i には整数 A 
i
​	
 (i≤A 
i
​	
 ≤N) が書かれています。

s=1,2,…,N のそれぞれについて、以下の問題を解いてください。

はじめ、マス s に駒を置く。「駒が置かれているマスに書かれている整数を x として、駒をマス x に移動させる」という操作を 10 
100
  回行った後、駒が置かれているマスの番号を出力する。
制約
1≤N≤5×10 
5
 
i≤A 
i
​	
 ≤N (1≤i≤N)
入力はすべて整数
入力
入力は以下の形式で標準入力から与えられる。

N
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
s=1,2,…,N に対する答えを、この順に空白を区切りとして一行に出力せよ。

入力例 1
Copy
7
2 4 7 5 5 6 7
出力例 1
Copy
5 5 7 5 5 6 7
s=1 のとき、駒は以下の図のように移動します。



駒がマス 5 に置かれているとき、操作が行われても駒は移動しないため、s=1 のときの答えは 5 となります。

入力例 2
Copy
5
1 2 3 4 5
出力例 2
Copy
1 2 3 4 5
駒が一度も移動しないこともあります。

入力例 3
Copy
15
11 3 10 7 15 10 10 11 11 13 11 12 14 14 15
出力例 3
Copy
11 14 14 14 15 14 14 11 11 14 11 12 14 14 15
"""
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
A = [0] + list(map(int, input().split()))

# ans[i] = i から 10^100 回後にいるマス
ans = [-1] * (N + 1)

def solve(i):
    # すでに計算済みなら返す
    if ans[i] != -1:
        return ans[i]
    
    # 自己ループならそこが答え
    if A[i] == i:
        ans[i] = i
        return i
    
    # 次へ進む
    ans[i] = solve(A[i])
    return ans[i]

for i in range(1, N + 1):
    solve(i)

print(*ans[1:])


from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# 0-indexにする
A = [a-1 for a in A]

# 逆グラフ
rev = [[] for _ in range(N)]
for i in range(N):
    rev[A[i]].append(i)

ans = [-1] * N
queue = deque()

# 自己ループを初期化
for i in range(N):
    if A[i] == i:
        ans[i] = i
        queue.append(i)

# BFS
while queue:
    v = queue.popleft()
    for nv in rev[v]:
        if ans[nv] == -1:
            ans[nv] = ans[v]
            queue.append(nv)

# 1-indexに戻す
print(*(a+1 for a in ans))
