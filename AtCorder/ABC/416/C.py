"""
AtCorder.ABC.416.C の Docstring
問題文
N 個の文字列 S 
1
​	
 ,…,S 
N
​	
  が与えられます。

全ての要素が 1 以上 N 以下であるような長さ K の数列 (A 
1
​	
 ,…,A 
K
​	
 ) に対し、 文字列 f(A 
1
​	
 ,…,A 
K
​	
 ) を S 
A 
1
​	
 
​	
 +S 
A 
2
​	
 
​	
 +⋯+S 
A 
K
​	
 
​	
  と定めます。ここで + は文字列の連結を表します。

N 
K
  個の数列全てについての f(A 
1
​	
 ,…,A 
K
​	
 ) を辞書順に並べたとき、小さい方から X 番目の文字列を求めてください。

制約
1≤N≤10
1≤K≤5
1≤X≤N 
K
 
S 
i
​	
  は英小文字からなる長さ 10 以下の文字列
N,K,X は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N K X
S 
1
​	
 
⋮
S 
N
​	
 
出力
答えを出力せよ。

入力例 1
Copy
3 2 6
abc
xxx
abc
出力例 1
Copy
abcxxx
f(1,1)= abcabc
f(1,2)= abcxxx
f(1,3)= abcabc
f(2,1)= xxxabc
f(2,2)= xxxxxx
f(2,3)= xxxabc
f(3,1)= abcabc
f(3,2)= abcxxx
f(3,3)= abcabc
であり、これらを辞書順に並べた abcabc, abcabc, abcabc, abcabc, abcxxx, abcxxx, xxxabc, xxxabc, xxxxxx の 6 番目は abcxxx です。

入力例 2
Copy
5 5 416
a
aa
aaa
aa
a
出力例 2
Copy
aaaaaaa

"""
N,K,X = map(int,input().split())
S = [input().strip() for _ in range(N)]
S.sort()#["abc", "abc", "xxx"]

X -=1#0-indexedに変更するため
ans = ""

for i in range(K):
    block = N ** (K-i-1)
    idx = X // block 
    ans += S[idx]
    X %= block 

print(ans)

"""
（root）
 ├─ abc
 │   ├─ abc   → abcabc
 │   ├─ abc   → abcabc
 │   └─ xxx   → abcxxx
 ├─ abc
 │   ├─ abc   → abcabc
 │   ├─ abc   → abcabc
 │   └─ xxx   → abcxxx
 └─ xxx
     ├─ abc   → xxxabc
     ├─ abc   → xxxabc
     └─ xxx   → xxxxxx
"""