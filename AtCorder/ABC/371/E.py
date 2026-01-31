"""
AtCorder.ABC.371.E の Docstring
問題文
長さ N の整数列 A=(A 
1
​	
 ,A 
2
​	
 ,…,A 
N
​	
 ) が与えられます。また、f(l,r) を以下で定義します。

(A 
l
​	
 ,A 
l+1
​	
 ,…,A 
r−1
​	
 ,A 
r
​	
 ) に含まれる値の種類数
次の式の値を求めてください。

i=1
∑
N
​	
  
j=i
∑
N
​	
 f(i,j)


制約
1≤N≤2×10 
5
 
1≤A 
i
​	
 ≤N
入力される数値は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N
A 
1
​	
  … A 
N
​	
 
出力
答えを出力せよ。

入力例 1
Copy
3
1 2 2
出力例 1
Copy
8
f(1,2) について考えます。(A 
1
​	
 ,A 
2
​	
 )=(1,2) に含まれる値の種類数は 2 なので f(1,2)=2 です。

f(2,3) について考えます。(A 
2
​	
 ,A 
3
​	
 )=(2,2) に含まれる値の種類数は 1 なので f(2,3)=1 です。

f の総和は 8 となります。

入力例 2
Copy
9
5 4 2 2 3 2 4 4 1
出力例 2
Copy
111
"""
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

# 各値の出現位置を記録（1-indexed）
pos = defaultdict(list)
for i, a in enumerate(A, start=1):
    pos[a].append(i)

# 全区間数
total = N * (N + 1) // 2

ans = 0

for x in pos:
    prev = 0
    sub = 0

    # x を含まない区間の数を数える
    for p in pos[x]:
        length = p - prev - 1
        sub += length * (length + 1) // 2
        prev = p

    # 最後の区間
    length = N - prev
    sub += length * (length + 1) // 2

    # x が貢献する区間数を足す
    ans += total - sub

print(ans)
