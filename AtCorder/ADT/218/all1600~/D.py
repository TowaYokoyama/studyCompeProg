"""
AtCorder.ADT.218.all1600~.D の Docstring
文字列 S, T が与えられます。以下の操作を高々 1 回行うことで、S を T と一致させることができるかを判定してください。

S の隣り合う 2 文字を選び、入れ替える。
なお、上記の操作を一度も行わないことも可能です。

制約
S, T はそれぞれ英小文字のみからなる、長さ 2 以上 100 以下の文字列
S の長さと T の長さは等しい
入力
入力は以下の形式で標準入力から与えられる。

S
T
出力
問題文中の操作を高々 1 回行うことで S を T と一致させることができるなら Yes を、できないなら No を出力せよ。

入力例 1
Copy
abc
acb
出力例 1
Copy
Yes
S の 2 文字目と 3 文字目を入れ替えることで、S を T と一致させることができます。

入力例 2
Copy
aabb
bbaa
出力例 2
Copy
No
どのように操作を行っても、S を T と一致させることはできません。

入力例 3
Copy
abcde
abcde
出力例 3
Copy
Yes
S と T は既に一致しています。
"""
S = input().strip()
T = input().strip()

if S == T:
    print("Yes")
    exit()

diff = []

for i in range(len(S)):
    if S[i] != T[i]:
        diff.append(i)

if len(diff) != 2:
    print("No")
else:
    i, j = diff
    if j == i + 1 and S[i] == T[j] and S[j] == T[i]:
        print("Yes")
    else:
        print("No")
