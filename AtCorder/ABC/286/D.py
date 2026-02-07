"""
AtCorder.ABC.286.C の Docstring
問題文
高橋君は N 種類の硬貨をそれぞれ何枚か持っており、 具体的には、1≤i≤N について A 
i
​	
  円硬貨を B 
i
​	
  枚持っています。

高橋君が現在持っている硬貨を用いて、（お釣りが出ないように）ちょうど X 円を支払うことができるか判定してください。

制約
1≤N≤50
1≤X≤10 
4
 
1≤A 
i
​	
 ≤100
1≤B 
i
​	
 ≤50
A 
i
​	
  はすべて異なる。
入力はすべて整数
入力
入力は以下の形式で標準入力から与えられる。

N X
A 
1
​	
  B 
1
​	
 
A 
2
​	
  B 
2
​	
 
⋮
A 
N
​	
  B 
N
​	
 
出力
高橋君が現在持っている硬貨を用いてちょうど X 円を支払うことができる場合は Yes を、 できない場合は No を出力せよ。

入力例 1
Copy
2 19
2 3
5 6
出力例 1
Copy
Yes
高橋君は 2 円硬貨を 3 枚、5 円硬貨を 6 枚持っています。 このうち、2 円硬貨を 2 枚、5 円硬貨を 3 枚用いることでちょうど 2×2+5×3=19 円を支払うことができます。 よって、Yes を出力します。

入力例 2
Copy
2 18
2 3
5 6
出力例 2
Copy
No
持っている硬貨をどのように組み合わせてもちょうど 18 円を支払うことはできません。 よって、No を出力します。

入力例 3
Copy
3 1001
1 1
2 1
100 10
出力例 3
Copy
Yes
1 枚も使用しない硬貨が存在しても構いません。
"""
N,X = map(int,input().split())
dp = [False] * (X+1) #dp[s]=s円が作れるのかどうか
dp[0] = True

coins = []
for _ in range(N):
  a,b = map(int,input().split())
  coins.append((a,b))
  
for a,b in coins:
  new_dp = dp[:] #今の状態を保存
  
  for s in range(X+1):
    if not dp[s]:
      continue
    
    for k in range(1,b+1):#この硬貨を1~b枚数触ってみる
      if s + a * k > X:
        break 
      new_dp[s+a*k] = True 
  
  dp = new_dp #この硬貨を使った結果を、次のターンの基準にする
print("Yes" if dp[X] else "No")