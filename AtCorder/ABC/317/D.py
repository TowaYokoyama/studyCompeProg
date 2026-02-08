"""
AtCorder.ABC.317.D の Docstring
問題文
高橋君と青木君が選挙で戦っています。
選挙区は N 個あります。i 番目の選挙区には X 
i
​	
 +Y 
i
​	
  人の有権者がいて、そのうち X 
i
​	
  人が高橋派、Y 
i
​	
  人が青木派です。(X 
i
​	
 +Y 
i
​	
  はすべて奇数です)
それぞれの区では、多数派がその区の Z 
i
​	
  議席を全て獲得します。そして、N 個の選挙区全体として過半数の議席を獲得した方が選挙に勝利します。( 
i=1
∑
N
​	
 Z 
i
​	
  は奇数です)
高橋君が選挙で勝利するには最低で何人を青木派から高橋派に鞍替えさせる必要がありますか？

制約
1≤N≤100
0≤X 
i
​	
 ,Y 
i
​	
 ≤10 
9
 
X 
i
​	
 +Y 
i
​	
  は奇数
1≤Z 
i
​	
 
i=1
∑
N
​	
 Z 
i
​	
 ≤10 
5
 
i=1
∑
N
​	
 Z 
i
​	
  は奇数
入力
入力は以下の形式で標準入力から与えられる。

N
X 
1
​	
  Y 
1
​	
  Z 
1
​	
 
X 
2
​	
  Y 
2
​	
  Z 
2
​	
 
⋮
X 
N
​	
  Y 
N
​	
  Z 
N
​	
 
出力
答えを出力せよ。

入力例 1
Copy
1
3 8 1
出力例 1
Copy
3
選挙区が 1 個しかないので、1 番目の選挙区で議席を獲得した人が選挙に勝利します。
1 番目の選挙区の青木派 3 人を高橋派に鞍替えさせると、1 番目の選挙区にいる有権者のうち高橋派は 6 人、青木派は 5 人になり、高橋君は議席を獲得できます。

入力例 2
Copy
2
3 6 2
1 8 5
出力例 2
Copy
4
1 番目の選挙区の議席数よりも 2 番目の選挙区の議席数の方が多いため、高橋君が選挙に勝つには 2 番目の選挙区で高橋派を多数派にする必要があります。
2 番目の選挙区の青木派の 4 人を鞍替えさせると高橋君は 5 議席を獲得できます。このとき青木君の獲得する議席は 2 議席なので、高橋君は選挙に勝利できます。

入力例 3
Copy
3
3 4 2
1 2 3
7 2 6
出力例 3
Copy
0
青木派から高橋派に鞍替えする人が 0 人でも高橋君が選挙で勝つ場合は 0 人が答えになります。

入力例 4
Copy
10
1878 2089 16
1982 1769 13
2148 1601 14
2189 2362 15
2268 2279 16
2394 2841 18
2926 2971 20
3091 2146 20
3878 4685 38
4504 4617 29
出力例 4
Copy
86
"""
N = int (input())

items = [] #(コスト,議席)
current_seat = 0 #すでに取れている議席
total_seat = 0 #全議席

for _ in range(N):
    X,Y,Z = map(int,input().split())
    total_seat += Z 
    
    if X > Y:
        #すでに勝っている
        current_seat += Z 
    else:
        #ひっくり返すのに必要な人数
        cost = (Y - X)//2 +1
        items.append((cost,Z))

#過半数
need = total_seat // 2 +1

#もう勝っているなら0
if current_seat >= need:
    print(0)
    exit()

#追加で必要な議席
target = need - current_seat 

INF = 10 ** 18

#dp[s] = 議席sを取るために必要な最小人数
dp = [INF] * (total_seat + 1)
dp[0] = 0

#ナップサック
for cost,seat in items:
    for s in range(total_seat, seat -1, -1):
        dp[s] = min(dp[s], dp[s-seat]+cost)

#target以上の中で最小を探す

answer = INF 
for s in range(target, total_seat + 1):
    answer = min(answer,dp[s])
print(answer)