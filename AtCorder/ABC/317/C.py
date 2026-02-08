"""
AtCorder.ABC.317.C の Docstring
問題文
ある地方に、1 から N の番号がついた N 個の街と、1 から M の番号がついた M 本の道路があります。

i 番目の道路は街 A 
i
​	
  と街 B 
i
​	
  を双方向に結び、長さは C 
i
​	
  です。

好きな街からスタートして同じ街を二度以上通らずに別の街へ移動するときの、通る道路の長さの和としてありえる最大値を求めてください。

制約
2≤N≤10
1≤M≤ 
2
N(N−1)
​	
 
1≤A 
i
​	
 <B 
i
​	
 ≤N
(A 
i
​	
 ,B 
i
​	
 ) は相異なる
1≤C 
i
​	
 ≤10 
8
 
入力は全て整数である
入力
入力は以下の形式で標準入力から与えられる。

N M
A 
1
​	
  B 
1
​	
  C 
1
​	
 
⋮
A 
M
​	
  B 
M
​	
  C 
M
​	
 
出力
答えを出力せよ。

入力例 1
Copy
4 4
1 2 1
2 3 10
1 3 100
1 4 1000
出力例 1
Copy
1110
4→1→3→2 と移動すると、通る道路の長さの和は 1110 となります。

入力例 2
Copy
10 1
5 9 1
出力例 2
Copy
1
道路と繋がっていない街が存在するかもしれません。

入力例 3
Copy
10 13
1 2 1
1 10 1
2 3 1
3 4 4
4 7 2
4 8 1
5 8 1
5 9 3
6 8 1
6 9 5
7 8 1
7 9 4
9 10 3
出力例 3
Copy
20

"""
N,M = map(int,input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    A,B,C = map(int,input().split())
    graph[A-1].append((B-1,C))
    graph[B-1].append((A-1,C))

ans = 0

def dfs(v,visited,total):
    """
    v       : 今いる街
    visited : すでに訪れた街の情報（True/False）
    total   : 今までの距離の合計
    """
    global ans 
    ans = max(total,ans)
    
    for nv, cost in graph[v]:
        if not visited[nv]:
            visited[nv] = True 
            dfs(nv, visited, total + cost)
            visited[nv] = False 

for start in range(N):
    visited = [False]*N 
    visited[start] = True 
    dfs(start,visited,0)
    
print(ans)