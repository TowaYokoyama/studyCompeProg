X = int(input())

found = False
for a in range(1, 7):
    for b in range(1, 7):
        for c in range(1, 7):
            if a + b + c == X:
                found = True

print("Yes" if found else "No")
"""
問題文
6 つの面を持つサイコロが 3 個あります。
どのサイコロも、面には 1,2,3,4,5,6 が書かれています。

これらのサイコロを同時に振ったとき、出た目の合計が X になることはありますか？

制約
X は 1 以上 20 以下の整数
入力
入力は以下の形式で標準入力から与えられる。

X
出力
出た目の合計が X になることがあれば Yes 、なければ No を出力せよ。

入力例 1
Copy
15
出力例 1
Copy
Yes
例えば、出目が 4,5,6 のとき、合計は 15 となります。

入力例 2
Copy
2
出力例 2
Copy
No
"""