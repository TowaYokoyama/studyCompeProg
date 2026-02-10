"""
AtCorder.ABC.122.C の Docstring
問題文
A, C, G, T からなる長さ N の文字列 S が与えられます。以下の Q 個の問いに答えてください。

問 i (1≤i≤Q): 整数 l 
i
​	
 ,r 
i
​	
  (1≤l 
i
​	
 <r 
i
​	
 ≤N) が与えられる。S の先頭から l 
i
​	
  文字目から r 
i
​	
  文字目までの (両端含む) 部分文字列を考える。この文字列に AC は部分文字列として何回現れるか。
注記
文字列 T の部分文字列とは、T の先頭と末尾から 0 文字以上を取り去って得られる文字列です。

例えば、ATCODER の部分文字列には TCO, AT, CODER, ATCODER, (空文字列) が含まれ、AC は含まれません。

制約
2≤N≤10 
5
 
1≤Q≤10 
5
 
S は長さ N の文字列である。
S の各文字は A, C, G, T のいずれかである。
1≤l 
i
​	
 <r 
i
​	
 ≤N
入力
入力は以下の形式で標準入力から与えられる。

N Q
S
l 
1
​	
  r 
1
​	
 
:
l 
Q
​	
  r 
Q
​	
 
出力
Q 行出力せよ。i 行目に問 i への答えを出力すること。

入力例 1
Copy
8 3
ACACTACG
3 7
2 3
1 8
出力例 1
Copy
2
0
3
問 1: S の先頭から 3 文字目から 7 文字目までの部分文字列は ACTAC です。この文字列に AC は部分文字列として 2 回現れます。
問 2: S の先頭から 2 文字目から 3 文字目までの部分文字列は CA です。この文字列に AC は部分文字列として 0 回現れます。
問 3: S の先頭から 1 文字目から 8 文字目までの部分文字列は ACACTACG です。この文字列に AC は部分文字列として 3 回現れます。
"""
N,Q = map(int,input().split())
S = input()
# AC は部分文字列として何回現れるか。
"""
方針
prefix[i] =
「1〜iまでに AC が何回出たか」
"""
prefix = [0] * (N+1)

for i in range(1,N):
    prefix[i+1] = prefix[i]
    if S[i-1] == 'A' and S[i] == 'C':
        prefix[i+1] += 1
        
for _ in range(Q):
    l,r = map(int,input().split())
    print(prefix[r] - prefix[l])
