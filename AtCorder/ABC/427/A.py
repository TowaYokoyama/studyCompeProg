"""
AtCorder.ABC.427.A の Docstring
入力
入力は以下の形式で標準入力から与えられる。

S
出力
問題文中の指示に従い、文字列を出力せよ。

入力例 1
Copy
ABCDE
出力例 1
Copy
ABDE
ABCDE の中央の文字は 3 文字目の C であるため、ABDE を出力します。

入力例 2
Copy
OOO
出力例 2
Copy
OO
入力例 3
Copy
ATCODER
出力例 3
Copy
ATCDER

"""
S = input()
mid = len(S)//2
ANS = []
for i in range(len(S)):
    if i != mid:
        ANS.append(S[i])
print("".join(ANS))