"""
AtCorder.ADT.217.All1800~.G の Docstring
あなたの運営する Web サービスには N 人のユーザがいます。

i 番目のユーザの現在のユーザ名は S 
i
​	
  ですが、T 
i
​	
  への変更を希望しています。
ここで、S 
1
​	
 ,…,S 
N
​	
  は相異なり、T 
1
​	
 ,…,T 
N
​	
  も相異なります。

ユーザ名を変更する順序を適切に定めることで、以下の条件を全て満たすように、全てのユーザのユーザ名を希望通り変更することができるか判定してください。

ユーザ名の変更は 1 人ずつ行う
どのユーザもユーザ名の変更は一度だけ行う
ユーザ名の変更を試みる時点で他のユーザが使っているユーザ名に変更することはできない
制約
1≤N≤10 
5
 
S 
i
​	
 ,T 
i
​	
  は英小文字からなる 1 文字以上 8 文字以下の文字列
S 
i
​	
 

=T 
i
​	
 
S 
i
​	
  は相異なる
T 
i
​	
  は相異なる
入力
入力は以下の形式で標準入力から与えられる。

N
S 
1
​	
  T 
1
​	
 
S 
2
​	
  T 
2
​	
 
⋮
S 
N
​	
  T 
N
​	
 
出力
条件を全て満たすように全てのユーザのユーザ名を希望通り変更することができるとき Yes、できないとき No と出力せよ。

入力例 1
Copy
2
b m
m d
出力例 1
Copy
Yes
1 番目のユーザの現在のユーザ名は b であり、m への変更を希望しています。
2 番目のユーザの現在のユーザ名は m であり、d への変更を希望しています。

まず、2 番目のユーザのユーザ名を m から d に変更し、 その後 1 番目のユーザのユーザ名を b から m に変更することで、条件を満たしながら変更することができます。

最初の時点では 2 番目のユーザのユーザ名が m なので、1 番目のユーザのユーザ名を同じ m に変更することはできません。

入力例 2
Copy
3
a b
b c
c a
出力例 2
Copy
No
1 番目のユーザの現在のユーザ名は a であり、b への変更を希望しています。
2 番目のユーザの現在のユーザ名は b であり、c への変更を希望しています。
3 番目のユーザの現在のユーザ名は c であり、a への変更を希望しています。

条件を満たしながらユーザ名の変更を行うことはできません。

入力例 3
Copy
5
aaa bbb
yyy zzz
ccc ddd
xxx yyy
bbb ccc
出力例 3
Copy
Yes
"""
import sys
sys.setrecursionlimit(10**7)

N = int(input())

graph = {}
for _ in range(N):
    s, t = input().split()
    graph[s] = t

visited = set()
in_stack = set()

def dfs(v):
    if v in in_stack:
        return True  # サイクル発見
    if v in visited:
        return False

    visited.add(v)
    in_stack.add(v)

    if v in graph:
        if dfs(graph[v]):
            return True

    in_stack.remove(v)
    return False

for v in graph:
    if dfs(v):
        print("No")
        exit()

print("Yes")
