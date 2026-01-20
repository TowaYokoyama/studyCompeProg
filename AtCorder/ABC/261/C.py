"""
AtCorder.ABC.261.C の Docstring
問題文
2 つの文字列 A,B に対して、A の末尾に B を連結した文字列を A+B と表します。

N 個の文字列 S 
1
​	
 ,…,S 
N
​	
  が与えられます。i=1,…,N の順に、次の指示に従って加工して出力してください。

S 
1
​	
 ,…,S 
i−1
​	
  の中に S 
i
​	
  と同じ文字列が存在しないならば、S 
i
​	
  を出力する。
S 
1
​	
 ,…,S 
i−1
​	
  の中に S 
i
​	
  と同じ文字列が X 個 (X>0) 存在するならば、X を文字列として扱って S 
i
​	
 + ( +X+ ) を出力する。
制約
1≤N≤2×10 
5
 
S 
i
​	
  は英小文字のみからなる長さ 1 以上 10 以下の文字列
入力
入力は以下の形式で標準入力から与えられる。

N
S 
1
​	
 
S 
2
​	
 
⋮
S 
N
​	
 
出力
問題文中の指示にしたがって、N 行出力せよ。

入力例 1
Copy
5
newfile
newfile
newfolder
newfile
newfolder
出力例 1
Copy
newfile
newfile(1)
newfolder
newfile(2)
newfolder(1)
入力例 2
Copy
11
a
a
a
a
a
a
a
a
a
a
a
出力例 2
Copy
a
a(1)
a(2)
a(3)
a(4)
a(5)
a(6)
a(7)
a(8)
a(9)
a(10)
"""
N = int(input())
S = []
for _ in range(N):
    S.append(input())
k = {}

for i in range (N):
    s = S[i]
    if s not in k:
        print(s)
        k[s] = 1
    else:
        print(f"{s}({k[s]})")
        k[s] += 1
        
from collections import defaultdict 
N = int(input())
k = defaultdict(int)

for _ in range(N):
  s = input()
  if k[s] == 0:
    print(s)
  else:
    print(f"{s}({k[s]})")
    k[s] += 1