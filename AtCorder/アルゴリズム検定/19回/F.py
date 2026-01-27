"""
AtCorder.アルゴリズム検定.19回.F の Docstring
問題文
あなたはドミノを並べています。

各 1≤i≤N について「ドミノ S 
i
​	
  が倒れるとドミノ T 
i
​	
  が倒れる」という計 N 個の情報が与えられます。

与えられた情報から「ドミノ X を倒すとドミノ Y が倒れる」といえるか判定してください。

制約
1≤N≤2×10 
5
 
N は整数
S 
i
​	
 ,T 
i
​	
 ,X,Y は英小文字のみからなる長さ 1 以上 100 以下の文字列
X

=Y
全ての i で S 
i
​	
 

=T 
i
​	
 
(S 
i
​	
 ,T 
i
​	
 ) は相異なる
入力
入力は以下の形式で標準入力から与えられる。

N
X Y
S 
1
​	
  T 
1
​	
 
⋮
S 
N
​	
  T 
N
​	
 
出力
与えられた情報から「ドミノ X を倒すとドミノ Y が倒れる」といえるとき Yes、いえないとき No と出力せよ。

入力例 1
Copy
5
second fourth
first second
second third
third fourth
fourth fifth
fifth sixth
出力例 1
Copy
Yes
2 番目の情報からドミノ second が倒れるとドミノ third が倒れること、3 番目の情報からドミノ third が倒れるとドミノ fourth が倒れることがことがわかります。
よってドミノ second を倒すとドミノ fourth が倒れるといえます。

入力例 2
Copy
5
fourth second
first second
second third
third fourth
fourth fifth
fifth sixth
出力例 2
Copy
No
与えられた情報からはドミノ fourth を倒すとドミノ second が倒れるとはいえません。

入力例 3
Copy
6
e d
a b
b a
a c
c d
d e
e a
出力例 3
Copy
Yes
入力例 4
Copy
1
a b
x y
出力例 4
Copy
No
"""
from collections import defaultdict,deque

N = int(input())
X,Y = input().split()
#graph = [[]]
graph = defaultdict(list)
for _ in range(N):
    s,t = input().split()
    graph[s].append(t)
    """
    具体例で見る（入力例1）
入力：
first second
second third
third fourth
graph はこうなる👇
{
  "first": ["second"],
  "second": ["third"],
  "third": ["fourth"]
}
    """
#bfs
queue = deque([X])
visited = set([X])

while queue:
    v = queue.popleft()
    if v == Y:
        print("Yes")
        exit()
    
    for nv in graph[v]:
        if nv not in visited:
            visited.add(nv)
            queue.append(nv)

print("No")