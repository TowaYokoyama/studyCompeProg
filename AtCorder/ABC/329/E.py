"""
AtCorder.ABC.329.E の Docstring
英大文字からなる長さ N の文字列 S と、英大文字からなる長さ M (≤N) の文字列 T が与えられます。

# のみからなる長さ N の文字列 X があります。 以下の操作を好きな回数行うことで、X を S に一致させることができるか判定してください。

X の中から連続する M 文字を選び、T で置き換える。
制約
1≤N≤2×10 
5
 
1≤M≤min(N, 5)
S は英大文字からなる長さ N の文字列
T は英大文字からなる長さ M の文字列
入力
入力は以下の形式で標準入力から与えられる。

N M
S
T
出力
X を S に一致させることができるならば Yes を、できないならば No を出力せよ。

入力例 1
Copy
7 3
ABCBABC
ABC
出力例 1
Copy
Yes
以下、X の l 文字目から r 文字目までの部分を X[l:r] と表記します。

次のように操作を行うことで、X を S に一致させることができます。

X[3:5] を T で置き換える。X= ##ABC## になる。　
X[1:3] を T で置き換える。X= ABCBC## になる。　
X[5:7] を T で置き換える。X= ABCBABC になる。　
入力例 2
Copy
7 3
ABBCABC
ABC
出力例 2
Copy
No
どのように操作を行っても、X を S に一致させることはできません。

入力例 3
Copy
12 2
XYXXYXXYYYXY
XY
出力例 3
Copy
Yes
"""
"""
方針
1消せる区間を全部探す
2キューに入れる
3消す
4その影響で新しく消せる場所を再チェック
5全部 # になれば成功
"""
from collections import deque

N, M = map(int, input().split())
S = list(input())   # 文字を書き換えるので list にする
T = input()

used = [False] * (N - M + 1)
q = deque()

def check(i):
    if used[i]:
        return
    ok = True
    for j in range(M):
        if not (S[i + j] == '#' or S[i + j] == T[j]):
            ok = False
            break
    if ok:
        used[i] = True
        q.append(i)

# 最初に消せる場所を全部探す
for i in range(N - M + 1):
    check(i)

# BFS
while q:
    i = q.popleft()

    # 区間を '#' にする
    for j in range(M):
        S[i + j] = '#'

    # 影響を受ける範囲を再チェック
    left = max(i - M + 1, 0)
    right = min(i + M - 1, N - M)
    for j in range(left, right + 1):
        check(j)

# 最後に全部 '#' になっているか
if all(c == '#' for c in S):
    print("Yes")
else:
    print("No")
