"""
問題文
英小文字からなる長さ M の文字列 N 個 S 
1
​	
 ,S 
2
​	
 ,…,S 
N
​	
  が与えられます。ここで、S 
i
​	
  は互いに異なります。

これらを並び替えた文字列の列 T 
1
​	
 ,T 
2
​	
 ,…,T 
N
​	
  であって、以下の条件を満たすものが存在するか判定してください。

1≤i≤N−1 を満たす全ての整数 i に対して、T 
i
​	
  を 1 文字だけ別の英小文字に変えて T 
i+1
​	
  にすることが出来る。
制約
2≤N≤8
1≤M≤5
S 
i
​	
  は英小文字からなる長さ M の文字列である。(1≤i≤N)
S 
i
​	
  は互いに異なる。
入力
入力は以下の形式で標準入力から与えられる。

N M
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
問題文の条件を満たす列が存在するならば Yes を、そうでないならば No を出力せよ。

入力例 1
Copy
4 4
bbed
abcd
abed
fbed
出力例 1
Copy
Yes
abcd , abed , bbed , fbed の順に並び替えると条件を満たします。

入力例 2
Copy
2 5
abcde
abced
出力例 2
Copy
No
どのように並び替えても条件を満たすことは出来ません。

入力例 3
Copy
8 4
fast
face
cast
race
fact
rice
nice
case
出力例 3
Copy
Yes
"""
from itertools import permutations 

def diff_ones(s,t):
    """sとtがちょうど１文字だけ違うか判定"""
    cnt = 0
    for a,b in zip(s,t):
        if a!= b:
            cnt+=1
    return cnt == 1

N,M = map(int,input().split())
S = [input().strip() for _ in range(N)]

#全ての並び替えを試す
for perm in permutations(S):
    ok = True 
    for i in range(N-1):
        if not diff_ones(perm[i], perm[i+1]):
            ok = False 
            break 
    if ok:
        print("Yes")
        exit()

print("No")