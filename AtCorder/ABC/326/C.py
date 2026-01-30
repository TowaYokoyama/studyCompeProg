"""
AtCorder.326.C の Docstring
問題文
高橋くんは数直線上に N 個のプレゼントを置きました。そのうち i 個目のプレゼントは座標 A 
i
​	
  に置かれました。

あなたは数直線上の長さ M の半開区間 [x,x+M) を選び、そこに含まれるプレゼントを全て獲得します。
より詳しくは、以下の手順でプレゼントを獲得します。

まず、実数 x をひとつ選択する。
その後、プレゼントのうち置かれている座標が x≤A 
i
​	
 <x+M を満たすものを全て獲得する。
最大でいくつのプレゼントを獲得することができますか?

制約
入力は全て整数
1≤N≤3×10 
5
 
1≤M≤10 
9
 
0≤A 
i
​	
 ≤10 
9
 
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
答えを整数として出力せよ。

入力例 1
Copy
8 6
2 3 5 7 11 13 17 19
出力例 1
Copy
4
例えば、半開区間 [1.5,7.5) を指定します。
このとき、座標 2,3,5,7 にある 4 つのプレゼントを全て獲得することができ、これが獲得可能な最大の個数です。

入力例 2
Copy
10 1
3 1 4 1 5 9 2 6 5 3
出力例 2
Copy
2
同一の座標に複数のプレゼントが置いてあることもあります。

入力例 3
Copy
10 998244353
100000007 0 1755647 998244353 495 1000000000 1755648 503 1755649 998244853
出力例 3
Copy
7
"""
from bisect import bisect_left 
N,M = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
ans = 0
#左端をA[i]に固定
for i in range(N):
    #A[i]+M未満の最初の位置を探す
    right = bisect_left(A,A[i]+M)
    
    # ③ [A[i], A[i]+M) に入る個数
    cnt = right - i 
    
    ans = max(ans,cnt)
    
print(ans)

N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

ans = 0
r = 0

for l in range(N):
    # 条件を満たす限り r を右へ
    while r < N and A[r] < A[l] + M:
        r += 1
    
    # [l, r) が条件を満たす
    ans = max(ans, r - l)

print(ans)
