"""
AtCorder.ABC.416.A の Docstring
問題文
o, x からなる長さ N の文字列 S と整数 L,R が与えられます。

S の L 文字目から R 文字目までが全て o であるかどうか判定してください。

制約
1≤N≤100
1≤L≤R≤N
S は o, x のみからなる長さ N の文字列
N,L,R は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N L R
S
出力
S の L 文字目から R 文字目までが全て o なら Yes、そうでないなら No と出力せよ。

入力例 1
Copy
10 6 8
xoxxooooxo
出力例 1
Copy
Yes
S の 6 文字目から 8 文字目は全て o なので答えは Yes です。

入力例 2
Copy
9 6 8
xoxxoxoox
出力例 2
Copy
No

"""
N,L,R = map(int,input().split())
S = input()
# print(S[L-1:R])
k = S[L-1:R]
if 'x' in S[L-1:R]:
    print("No")
else:
    print("Yes")
      