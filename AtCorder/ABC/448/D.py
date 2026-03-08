"""
問題文
頂点 1,2,…,N の N 頂点からなる木が与えられます。この木の辺のうち i 本目は頂点 U 
i
​	
  と頂点 V 
i
​	
  を結びます。
頂点 i には整数 A 
i
​	
  が書かれています。

全ての k=1,2,…,N について以下の問題に答えてください。

問題: 頂点 1 から頂点 k への単純なパス (同じ頂点を複数回通らないパス) に含まれる頂点について、同じ整数の書かれた異なる 2 頂点の組が存在すれば Yes 、そうでないなら No と答えよ。
なお、木上の 2 つの頂点を結ぶ単純なパスが一意に定まることは証明できる。
制約
入力は全て整数
2≤N≤2×10 
5
 
1≤A 
i
​	
 ≤10 
9
 
1≤U 
i
​	
 ,V 
i
​	
 ≤N
与えられるグラフは木
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
N−1
​	
  V 
N−1
​	
 
出力
N 行出力せよ。
そのうち i 行目には、 k=i である場合の問題の答えを出力せよ。

入力例 1
Copy
5
1 3 2 1 2
1 2
1 3
3 4
3 5
出力例 1
Copy
No
No
No
Yes
Yes
k=1 について、頂点 1 から頂点 1 へのパスに含まれるのは頂点 1 です。パスが 1 頂点のみで構成されるので、答えは No となります。
k=2 について、頂点 1 から頂点 2 へのパスに含まれるのは頂点 1,2 で、それぞれに書かれた整数は 1,3 です。よって、答えは No です。
k=3 について、頂点 1 から頂点 3 へのパスに含まれるのは頂点 1,3 で、それぞれに書かれた整数は 1,2 です。よって、答えは No です。
k=4 について、頂点 1 から頂点 4 へのパスに含まれるのは頂点 1,3,4 で、それぞれに書かれた整数は 1,2,1 です。パス内の頂点 1,4 に同じ整数 1 が書かれているので、答えは Yes です。
k=5 について、頂点 1 から頂点 5 へのパスに含まれるのは頂点 1,3,5 で、それぞれに書かれた整数は 1,2,2 です。パス内の頂点 3,5 に同じ整数 2 が書かれているので、答えは Yes です。
入力例 2
Copy
2
1000000000 1000000000
2 1
出力例 2
Copy
No
Yes
入力例 3
Copy
10
10 7 3 9 1 3 8 5 7 10
3 6
8 6
6 1
9 7
7 10
5 4
4 2
10 2
1 9
出力例 3
Copy
No
Yes
Yes
Yes
Yes
No
No
No
No
Yes
"""
# from collections import deque
import sys
sys.setrecursionlimit(10**7)

n = int(input())
a = list(map(int, input().split()))

g = [[] for _ in range(n)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

cnt = 0
s = set()
ans = [0] * n


def dfs(v, pv):
    global cnt

    del_flag = 0

    if a[v] in s:
        del_flag = 1
    else:
        s.add(a[v])

    cnt += del_flag

    if cnt > 0:
        ans[v] = 1
    else:
        ans[v] = 0

    for nx in g[v]:
        if nx == pv:
            continue
        dfs(nx, v)

    cnt -= del_flag

    if del_flag == 0:
        s.remove(a[v])


dfs(0, -1)

for x in ans:
    if x:
        print("Yes")
    else:
        print("No")
"""
er/ABC/448/D.py
dfsコードの結果testcase3
10
10 7 3 9 1 3 8 5 7 10
3 6
8 6
6 1
9 7
7 10
5 4
4 2
10 2
1 9
No
Yes
Yes
No
No
No
No
No
No
Yes
"""
# print(graph)
# [[], [2, 3], [1], [1, 4, 5], [3], [3]]

#頂点1から探索しながら拡張てんkへのパス上に重複している整数が存在しているかどうか
# def dfs():
    
#     ans = [""] * (N+1)
#     queue = deque()
#     #(現在の頂点, これまでパスで見た値の集合)
#     queue.append((1,{A[0]}))#頂点1,A[1]はA[0]
#     visited = [False] * (N+1)
#     visited[1] =True
#     ans[1] = "No"#頂点１自身は１頂点なのの重複なし
    
#     while queue:
#         v,seen = queue.popleft()
#         for nv in graph[v]:
#             if not visited[nv]:
#                 visited[nv] = True
#                 val = A[nv-1]
#                 if val in seen:
#                     ans[nv] = "Yes"
#                 else:
#                     ans[nv] = "No"

#                 queue.append((nv,seen | {val}))#seenに追加した新しい集合
#     return ans

# ans = bfs()
# for i in range(1, N + 1):
#     print(ans[i])
"""
Atcoder公式解

頂点 1 から頂点 k までのパスを毎回求めなおしているようでは時間計算量が O(N 
2
 ) となり実行時間制限に間に合いません。
全てのパスに対する答えを何らかの方法でまとめて高速に挙げる必要があります。どのようにすればよいでしょうか？

以下のような 深さ優先探索(DFS) を考えます。

頂点 1 への侵入から始める。
頂点 v へ侵入するタイミングで、頂点 v に関する情報を追加する。
頂点 v から退出するタイミングで、頂点 v に関する情報を削除する。
このようにすることで、頂点 v に侵入し頂点 v に関する情報を追加した時点で、頂点 1 から頂点 v へのパスを構成する頂点集合に関する情報が得られています。

これを用いて、この問題の答えが求められるようにします。

最初は空である集合 S 、最初 0 である変数 cnt を持っておく。
頂点 v への侵入
S 内に既に A 
v
​	
  があれば、 cnt に 1 加算する。
(頂点 1 を根と解釈した場合に) v の祖先に既に A 
v
​	
  が含まれるので、そのことを記憶します。
そうでないなら S に A 
v
​	
  を追加する。
v の祖先に A 
v
​	
  が含まれないので、子孫を考える時に A 
v
​	
  の存在を検知できるようにします。
その後、 cnt>0 なら Yes 、 cnt=0 なら No と判断する。
頂点 v からの退出
もし進入時 S に A 
v
​	
  を追加していた場合、 A 
v
​	
  を削除する。
このケースでは v の祖先に A 
v
​	
  は存在しません。
そうでないなら、 cnt から 1 減算する。
このケースではまだ v の祖先に A 
v
​	
  は存在しますが、頂点 v での重複の検知を解除する必要があります。
例えば C++ の set を利用して実装すると、時間計算量が O(NlogN) となります。

この問題に関する発展的話題として、 Euler Tour があります。

実装例 (C++):

#include<bits/stdc++.h>
using namespace std;
int n;
vector<int> a;
vector<vector<int>> g;
int cnt=0;
set<int> s;
vector<int> ans;
void dfs(int v,int pv){
  int del=0;
  if(s.find(a[v])!=s.end()){del=1;}
  else{s.insert(a[v]);}
  cnt+=del;
  if(cnt>0){ans[v]=1;}
  else{ans[v]=0;}
  for(auto &nx : g[v]){
    if(nx==pv){continue;}
    dfs(nx,v);
  }
  cnt-=del;
  if(del==0){
    s.erase(a[v]);
  }
}
int main(){
  cin >> n;
  a.resize(n);
  for(auto &nx : a){cin >> nx;}
  g.resize(n);
  for(int i=1;i<n;i++){
    int u,v;
    cin >> u >> v;
    u--; v--;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  ans.resize(n);
  dfs(0,-1);
  for(auto &nx : ans){
    if(nx){cout << "Yes\n";}
    else{cout << "No\n";}
  }
  return 0;
}
"""