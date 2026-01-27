"""
AtCorder.ABC.277.C の Docstring
問題文
10 
9
  階建てのビルがあり、N 本のはしごがかかっています。
ビルの 1 階にいる高橋君ははしごを繰り返し使って（0 回でもよい）できるだけ高い階へ上りたいと考えています。
はしごには 1 から N までの番号がついており、はしご i は A 
i
​	
  階と B 
i
​	
  階を結んでいます。はしご i を利用すると A 
i
​	
  階から B 
i
​	
  階へ、または B 
i
​	
  階から A 
i
​	
  階へ双方向に移動することができますが、それ以外の階の間の移動は行うことはできません。
また、高橋君は同じ階での移動は自由に行うことができますが、はしご以外の方法で他の階へ移動することはできません。
高橋君は最高で何階へ上ることができますか？

制約
1≤N≤2×10 
5
 
1≤A 
i
​	
 ,B 
i
​	
 ≤10 
9
 
A 
i
​	
 

=B 
i
​	
 
入力はすべて整数
入力
入力は以下の形式で標準入力から与えられる。

N
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
 
…
A 
N
​	
  B 
N
​	
 
出力
答えを出力せよ。

入力例 1
Copy
4
1 4
4 3
4 10
8 3
出力例 1
Copy
10
はしご 1 で 4 階に進み、はしご 3 で 10 階に進むことにより、10 階にたどり着くことができます。

入力例 2
Copy
6
1 3
1 5
1 12
3 5
3 12
5 12
出力例 2
Copy
12
入力例 3
Copy
3
500000000 600000000
600000000 700000000
700000000 800000000
出力例 3
Copy
1
他の階への移動ができない場合もあります。
"""
from collections import defaultdict,deque 
N = int(input())
graph = defaultdict(list)
for _ in range(N):
    a,b= map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
#無向グラフゆえにこれをここに書いておく！
"""
{
  1: [4],
  4: [1, 3, 10],
  3: [4, 8],
  10: [4],
  8: [3]
}

"""
def bfs():
    queue = deque([1])
    visited = set([1])
    
    while queue:
        v = queue.popleft()
       
        for nv in graph[v]:
            if nv not in visited:
                visited.add(nv)
                queue.append(nv)
    
    return max(visited)

print(bfs())