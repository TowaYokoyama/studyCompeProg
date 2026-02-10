"""
問題文
英小文字のみからなる長さ N の文字列 S=S 
1
​	
 S 
2
​	
 …S 
N
​	
  が与えられます。

また、S に関する Q 個の質問が与えられます。 i=1,2,…,Q について、i 番目の質問は 2 つの整数 l 
i
​	
 ,r 
i
​	
  で表される下記の質問です。

S の l 
i
​	
  文字目から r 
i
​	
  文字目までからなる部分文字列 S 
l 
i
​	
 
​	
 S 
l 
i
​	
 +1
​	
 …S 
r 
i
​	
 
​	
  において、 同じ英小文字が 2 つ隣りあう箇所は何個ありますか？ すなわち、l 
i
​	
 ≤p≤r 
i
​	
 −1 かつ S 
p
​	
 =S 
p+1
​	
 を満たす整数 p は何個ありますか？
Q 個の質問それぞれの答えを出力してください。

制約
N,Q は整数
1≤N,Q≤3×10 
5
 
S は英小文字のみからなる長さ N の文字列
l 
i
​	
 ,r 
i
​	
  は整数
1≤l 
i
​	
 ≤r 
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
 
l 
2
​	
  r 
2
​	
 
⋮
l 
Q
​	
  r 
Q
​	
 
出力
Q 行出力せよ。 i=1,2,…,Q について、i 行目には i 番目の質問に対する答えを出力せよ。

入力例 1
Copy
11 4
mississippi
3 9
4 10
4 6
7 7
出力例 1
Copy
2
2
0
0
4 個の質問それぞれに対する答えは下記の通りです。

1 個目の質問に関して、S 
3
​	
 S 
4
​	
 …S 
9
​	
 = ssissip で同じ英小文字が隣り合う箇所は、S 
3
​	
 S 
4
​	
 = ss と S 
6
​	
 S 
7
​	
 = ss の 2 個です。
2 個目の質問に関して、S 
4
​	
 S 
5
​	
 …S 
10
​	
 = sissipp で同じ英小文字が隣り合う箇所は、S 
6
​	
 S 
7
​	
 = ss と S 
9
​	
 S 
10
​	
 = pp の 2 個です。
3 個目の質問に関して、S 
4
​	
 S 
5
​	
 S 
6
​	
 = sis で同じ英小文字が隣り合う箇所は 0 個です。
4 個目の質問に関して、S 
7
​	
 = s で同じ英小文字が隣り合う箇所は 0 個です。
入力例 2
Copy
5 1
aaaaa
1 5
出力例 2
Copy
4
S 
1
​	
 S 
2
​	
 …S 
5
​	
 = aaaaa で同じ英小文字が隣り合う箇所は、 S 
1
​	
 S 
2
​	
 = aa 、S 
2
​	
 S 
3
​	
 = aa 、S 
3
​	
 S 
4
​	
 = aa 、S 
4
​	
 S 
5
​	
 = aa の 4 個です。
"""
N,Q = map(int,input().split())
S = input()
prefix = [0]*(N+1)
for i in range(1,N):
    prefix[i+1] = prefix[i]
    if S[i] == S[i-1]:
        prefix[i+1] += 1
# print(prefix)

for _ in range(Q):
    l,r = map(int,input().split())
    print(prefix[r] - prefix[l])