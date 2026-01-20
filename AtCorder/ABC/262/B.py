"""
AtCorder.ABC.262.B の Docstring
問題文
N 頂点 M 辺の単純無向グラフが与えられます。頂点には 1,…,N の番号が付けられており、i(1≤i≤M) 番目の辺は頂点 U 
i
​	
  と頂点 V 
i
​	
  を結んでいます。

以下の条件を全て満たす整数 a,b,c の組の総数を求めてください。

1≤a<b<c≤N
頂点 a と頂点 b を結ぶ辺が存在する。
頂点 b と頂点 c を結ぶ辺が存在する。
頂点 c と頂点 a を結ぶ辺が存在する。
制約
3≤N≤100
1≤M≤ 
2
N(N−1)
​	
 
1≤U 
i
​	
 <V 
i
​	
 ≤N(1≤i≤M)
(U 
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
 )(i

=j)
入力は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N M
U 
1
​	
  V 
1
​	
 
⋮
U 
M
​	
  V 
M
​	
 
出力
答えを出力せよ。

入力例 1
Copy
5 6
1 5
4 5
2 3
1 4
3 5
2 5
出力例 1
Copy
2
(a,b,c)=(1,4,5),(2,3,5) が条件を満たします。

入力例 2
Copy
3 1
1 2
出力例 2
Copy
0
入力例 3
Copy
7 10
1 7
5 7
2 5
3 6
4 7
1 5
2 4
1 3
1 6
2 7
出力例 3
Copy
4
"""
N,M = map(int,input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u,v =map(int,input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

ans = 0

ans = 0
for a in range(N):
    for b in range(a+1, N):
        if b not in graph[a]:
            continue
        for c in range(b+1, N):
            if c in graph[a] and c in graph[b]:
                ans += 1

print(ans)