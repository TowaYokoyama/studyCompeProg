"""
英小文字からなる長さ N の文字列 S が与えられます。

整数の組 (i,j) であって、以下の条件をすべて満たすものの個数を求めてください。

1≤i≤j≤N
S 
i
​	
 =S 
j
​	
 
L≤j−i≤R
制約
2≤N≤5×10 
5
 
1≤L≤R≤N−1
N,L,R は整数
S は長さ N の英小文字からなる文字列
入力
入力は以下の形式で標準入力から与えられる。

N L R
S
出力
答えを出力せよ。

入力例 1
Copy
6 2 4
aabcba
出力例 1
Copy
2
問題文中の条件をすべて満たす整数の組は (i,j)=(2,6),(3,5) の 2 つです。

入力例 2
Copy
9 3 6
aaaaaaaaa
出力例 2
Copy
18
入力例 3
Copy
10 2 6
aabbccaabb
出力例 3
Copy
6
"""
from collections import defaultdict
N,L,R = map(int,input().split())
S = input()
#window = L -R 
ans = 0
count = defaultdict(int)

for j in range(N):
    #jから距離L~R前のiを管理
    #新たにウィンドウに入るiを追加
    add_i = j - L    
    if add_i >= 0:
        count[S[add_i]] += 1
    
    #ウィンドウから外れるiを削除
    remove_i = j - R -1 
    if remove_i >= 0:
        count[S[remove_i]] -= 1
        
    #S[j]と同じ文字がウィンドウ内にいくつあるか
    ans += count[S[j]]

print(ans)
