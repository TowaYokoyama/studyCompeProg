"""
AtCorder.ABC.426.B の Docstring
問題文
英小文字からなる長さ 3 以上の文字列 S が与えられます。
S はちょうど 2 種類の文字を含み、 1 文字だけ他の文字と異なります。その 1 文字を答えてください。

例えば、 S が odd なら o と答えてください。

制約
S は英小文字からなる長さ 3 以上 10 以下の文字列
S はちょうど 2 種類の文字を含み、 1 文字だけ他の文字と異なる
入力
入力は以下の形式で標準入力から与えられる。

S
出力
答えを出力せよ。

入力例 1
Copy
odd
出力例 1
Copy
o
odd のうち他の文字と異なるものは o です。

入力例 2
Copy
dad
出力例 2
Copy
a
dad のうち他の文字と異なるものは a です。

入力例 3
Copy
wwwwwwwwwv
出力例 3
Copy
v
wwwwwwwwwv のうち他の文字と異なるものは v です。
"""
from collections import Counter
S = input()

K = []

for i in range(len(S)):
   K.append(S[i]) 
z = Counter(K)
for c in z:
    if z[c] == 1:
        print(c)
        break
    
