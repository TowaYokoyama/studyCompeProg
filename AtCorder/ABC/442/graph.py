"""
AtCorder.ABC.427.D の Docstring
問題文
N 頂点 M 辺の有向グラフがあります。頂点には 1 から N までの番号が付けられており、i 番目の辺は頂点 U 
i
​	
  から頂点 V 
i
​	
 へ向かう有向辺です。ここで、各頂点の出次数は 1 以上です。

また、各頂点には文字が書かれており、頂点 i に書かれている文字は S 
i
​	
  です。ただし、S 
i
​	
  とは S の i 文字目を指します。

Alice と Bob はこのグラフ上で 1 つの駒を用いて以下のゲームを行います。

はじめ、駒は頂点 1 に置かれており、Alice が先手、Bob が後手となって以下の操作を交互に K 回ずつ行う。

現在駒が置かれている頂点を u とする。頂点 u から頂点 v に向かう辺が存在するような頂点 v を選び、駒を頂点 v に移動させる。
最終的に駒が置かれている頂点を v として、S 
v
​	
 = A のとき Alice の勝ち、S 
v
​	
 = B のとき Bob の勝ちである。

両者が最適に行動したときのゲームの勝者を求めてください。

1 つの入力において T 個のテストケースが与えられます。それぞれについて答えてください。

制約
1≤T
2≤N,M≤2×10 
5
 
1≤K≤10
S は A, B からなる長さ N の文字列
1≤U 
i
​	
 ,V 
i
​	
 ≤N
i

=j のとき (U 
i
​	
 ,V 
i
​	
 )

=(U 
j
​	
 ,V 
j
​	
 )
各頂点の出次数は 1 以上
1 つの入力に含まれるテストケースについて、N の総和は 2×10 
5
  以下
1 つの入力に含まれるテストケースについて、M の総和は 2×10 
5
  以下
入力
入力は以下の形式で標準入力から与えられる。

T
case 
1
​	
 
case 
2
​	
 
…
case 
T
​	
 
ここで、case 
i
​	
  は i 番目のテストケースを表し、各テストケースは以下の形式で与えられる。

N M K
S
U 
1
​	
  V 
1
​	
 
U 
2
​	
  V 
2
​	
 
⋮
U 
M
​	
  V 
M
​	
 
出力
T 行出力せよ。i 行目には、i 番目のテストケースにおいて両者が最適に行動したときに Alice が勝つ場合 Alice を、Bob が勝つ場合 Bob を出力せよ。

入力例 1
Copy
3
4 6 2
AABB
1 2
2 3
3 1
3 3
3 4
4 2
4 6 2
ABAB
1 2
2 3
3 1
3 3
3 4
4 2
5 8 3
ABABB
1 2
2 2
2 3
3 1
3 4
4 4
4 5
5 3
出力例 1
Copy
Alice
Bob
Bob
1 番目のテストケースについてゲームの進行の一例を説明します。ただし、この進行において両者は最適に行動しているとは限りません。

はじめ、駒は頂点 1 に置かれている。
Alice が頂点 2 に駒を動かす。
Bob が頂点 3 に駒を動かす。
Alice が頂点 3 に駒を動かす。
Bob が頂点 1 に駒を動かす。
このとき、S 
1
​	
 = A であるため Alice の勝ちとなります。
"""
import sys
sys.setrecursionlimit(10**7)

T = int(input())

for _ in range(T):
    N, M, K = map(int, input().split())
    S = input().strip()

    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)

    # dp[u][t][p]: 
    # u = 今いる頂点
    # t = 残り手数
    # p = 0(Aliceの番), 1(Bobの番)
    # True = Alice勝ち, False = Bob勝ち
    dp = [[[-1]*2 for _ in range(2*K+1)] for __ in range(N)]

    def dfs(u, t, p):
        if dp[u][t][p] != -1:
            return dp[u][t][p]

        # 手数が尽きたら勝敗確定
        if t == 0:
            if S[u] == 'A':
                dp[u][t][p] = True
            else:
                dp[u][t][p] = False
            return dp[u][t][p]

        # Aliceの番
        if p == 0:
            for v in graph[u]:
                if dfs(v, t-1, 1):
                    dp[u][t][p] = True
                    return True
            dp[u][t][p] = False
            return False

        # Bobの番
        else:
            for v in graph[u]:
                if not dfs(v, t-1, 0):
                    dp[u][t][p] = False
                    return False
            dp[u][t][p] = True
            return True

    # 初期状態：頂点0、残り2K手、Aliceの番
    result = dfs(0, 2*K, 0)

    if result:
        print("Alice")
    else:
        print("Bob")
