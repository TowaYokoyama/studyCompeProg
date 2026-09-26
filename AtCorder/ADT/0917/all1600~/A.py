"""
接官の人数 
N と、各面接官の高橋君への評価を表す長さ 
N の文字列 
S が与えられます。
i=1,2,…,N に対し 
S の 
i 文字目が 
i 番目の面接官の評価に対応し、o は「良」、- は「可」、x は 「不可」を表します。

高橋君は以下の 
2 つの条件を両方満たすならば合格、そうでなければ不合格です。

「良」と評価した面接官が少なくとも 
1 人いる
「不可」と評価した面接官がいない
高橋君が合格かどうかを判定してください。

制約
1≤N≤100
S は o, -, x のみからなる長さが 
N の文字列
入力
入力は以下の形式で標準入力から与えられる。

N
S"Ye
出力
高橋君が合格ならば Yes と、そうでなければ No と出力せよ。

入力例 1
Copy
4
oo--
出力例 1
Copy
Yes
1,2 番目の面接官が「良」と評価していて、さらに「不可」と評価した面接官がいないため合格です。

入力例 2
Copy
3
---
出力例 2
Copy
No
「良」と評価した面接官が 
1 人もいないため不合格です。

入力例 3
Copy
1
o
出力例 3
Copy
Yes
入力例 4
Copy
100
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooox
出力例 4
Copy
No
100 番目の面接官が「不可」と評価しているため不合格です。
"""
N = int(input())
S = input()

first = False
second = True
for a in S:
    if a == "o":
        first = True
    if a == "x":
        second = False

print("Yes" if first & second else "No")