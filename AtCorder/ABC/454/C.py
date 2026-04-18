"""
アイテム 1 からアイテム N までの N 種類のアイテムがあります。はじめ、高橋君はアイテム 1 のみ持っています。

高橋君には M 人の友達がいます。i 人目 (1≤i≤M) の友達にアイテム A 
i
​	
  を渡すと、アイテム B 
i
​	
  をもらうことができます。

高橋君が手に入れることのできるアイテムはアイテム 1 を含めて何種類あるか求めてください。

制約
2≤N≤3×10 
5
 
1≤M≤3×10 
5
 
1≤A 
i
​	
 ,B 
i
​	
 ≤N
A 
i
​	
 

=B 
i
​	
 
入力される値は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N M
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
M
​	
  B 
M
​	
 
出力
答えを出力せよ。

入力例 1
Copy
5 5
1 2
2 3
3 4
2 4
5 2
出力例 1
Copy
4
例えば、以下のように行動することでアイテム 4 を手に入れることができます。

アイテム 1 を 1 人目の友達に渡す。アイテム 2 をもらう。
アイテム 2 を 4 人目の友達に渡す。アイテム 4 をもらう。
高橋君が手に入れられるアイテムはアイテム 1,2,3,4 の 4 種類です。したがって、4 を出力してください。

入力例 2
Copy
3 2
2 1
3 2
出力例 2
Copy
1
高橋君が手に入れられるアイテムはアイテム 1 の 1 種類です。

入力例 3
Copy
7 8
2 6
2 5
3 6
1 6
1 2
5 6
2 3
3 7
出力例 3
Copy
6
"""
from collections import deque
N,M = map(int,input().split())
graph = [[] for _ in range(N + 1)]  # ノード1~N分の空リストを用意  
for _ in range(M):
    A,B = map(int,input().split())
    graph[A].append(B)

    # graph[B].append(A)
def bfs():        
    queue = deque([1])
    visited = set([1])
    while queue:
            current = queue.popleft()
            for next_item in graph[current]:
                if next_item not in visited:
                    visited.add(next_item)
                    queue.append(next_item)
    return visited 

res = bfs()
print(len(res))
    