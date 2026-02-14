"""
AtCorder.ABC.445.B の Docstring
小文字からなる N 個の奇数長の文字列 S 
1
​	
 ,S 
2
​	
 ,…,S 
N
​	
  が与えられます。

S 
1
​	
 ,S 
2
​	
 ,…,S 
N
​	
  のうち最も長いものの長さを m とします。 以下の条件を満たす文字列 T 
1
​	
 ,T 
2
​	
 ,…,T 
N
​	
  を求めてください。

条件：T 
i
​	
  はある非負整数 k について k 個の .、S 
i
​	
 、k 個の . をこの順に結合してできる、長さ m の文字列である。
制約
N は 1 以上 100 以下の整数
S 
i
​	
  は英小文字からなる長さ 1 以上 99 以下の奇数長の文字列
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
N 行出力せよ。i (1≤i≤N) 行目には T 
i
​	
  を出力せよ。

入力例 1
Copy
4
apple
blueberry
coconut
dragonfruit
出力例 1
Copy
...apple...
.blueberry.
..coconut..
dragonfruit
m=11 であり、T 
1
​	
 ,T 
2
​	
 ,T 
3
​	
 ,T 
4
​	
  はそれぞれ k=3,1,2,0 について問題文中の条件を満たしています。

入力例 2
Copy
6
abc
d
efghi
jkl
mnopq
r
出力例 2
Copy
.abc.
..d..
efghi
.jkl.
mnopq
..r..
"""
N = int(input())
z = []
for _ in range(N):
    S = input()
    z.append(S)
max_l = 0
for x in z:
    if len(x) > max_l:
        max_l = len(x)
# print(max_l)
k = ['.'] * (max_l)
# print(k)#['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
for a in z:
    #mid = len(a)//2+1
    need_block = max_l - len(a)
    need_block_union = need_block//2
    print("".join((".")*need_block_union)+a+"".join((".")*need_block_union))
