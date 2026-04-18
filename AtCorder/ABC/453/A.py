N = int(input())
S = input()
i = 0
del_ch = []
while i < N and S[i] == 'o':
    i+=1
print(S[i:])
    
"""

長さ N の文字列 S が与えられます。
S のうち先頭に連続する o をすべて取り除いた文字列を出力してください。
なお、 S 中のすべての文字が o である場合は空文字列を出力してください。

制約
N は 1≤N≤50 を満たす整数
S は英小文字からなる長さ N の文字列
入力
入力は以下の形式で標準入力から与えられる。

N
S
出力
答えを出力せよ。

入力例 1
Copy
7
ooparts
出力例 1
Copy
parts
ooparts のうち先頭に連続する o をすべて取り除くと parts となります。

入力例 2
Copy
6
abcooo
出力例 2
Copy
abcooo
先頭の文字が o でない場合もあります。
"""
