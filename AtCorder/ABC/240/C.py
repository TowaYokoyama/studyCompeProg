"""
AtCorder.ABC.240.C の Docstring
問題文
高橋君は数直線上の座標 0 の位置にいます。

これから高橋君は N 回のジャンプを行います。i(1≤i≤N) 回目のジャンプでは、正の方向に a 
i
​	
  または b 
i
​	
  移動します。

N 回のジャンプの後に座標 X の位置にいるようにすることはできますか？

制約
1≤N≤100
1≤a 
i
​	
 <b 
i
​	
 ≤100(1≤i≤N)
1≤X≤10000
入力は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N X
a 
1
​	
  b 
1
​	
 
⋮
a 
N
​	
  b 
N
​	
 
出力
N 回のジャンプの後に座標 X の位置にいるようにすることができるならば Yes と、そうでないなら No と出力せよ。

入力例 1
Copy
2 10
3 6
4 5
出力例 1
Copy
Yes
1 回目のジャンプでは b 
1
​	
 (=6) 移動し、2 回目のジャンプでは a 
2
​	
 (=4) 移動することで、座標 X(=10) の位置にいるようにすることができます。

入力例 2
Copy
2 10
10 100
10 100
出力例 2
Copy
No
1 回目のジャンプの後に座標 X(=10) の位置にいるようにすることはできますが、全てのジャンプの後に座標 X(=10) の位置にいるようにすることはできません。

入力例 3
Copy
4 12
1 8
5 7
3 4
2 6
出力例 3
Copy
Yes
"""
N,X = map(int,input().split())
ab = [tuple(map(int,input().split())) for _ in range(N)]

dp = [[False]*(X+1) for _ in range(N+1)]
dp[0][0] = True 

for i in range(N):
    a,b = ab[i]
    for s in range(X+1):
        if dp[i][s]:
            if s + a <= X:
                dp[i+1][s+a] = True 
            if s + b <= X:
                dp[i+1][s+b] = True 

print("Yes" if dp[N][X] else "No")