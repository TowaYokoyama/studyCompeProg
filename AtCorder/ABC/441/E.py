"""
AtCorder.ABC.441.E の Docstring
問題文
A, B, C の 3 種類の文字からなる長さ N の文字列 S が与えられます。

S の空でない連続する部分文字列は  
2
N(N+1)
​	
  個ありますが、そのうち A が B よりも多く含まれるものはいくつあるか求めてください。

2 つの部分文字列は、S から取り出す場所が異なれば文字列として等しくても区別して数えることに注意してください。

部分文字列とは
制約
1≤N≤5×10 
5
 
S は A, B, C からなる長さ N の文字列
N は整数
入力
入力は以下の形式で標準入力から与えられる。

N
S
出力
S の連続する部分文字列のうち A が B よりも多く含まれるものの個数を出力せよ。

入力例 1
Copy
10
ACBBCABCAB
出力例 1
Copy
8
以下の 8 つの部分文字列が条件を満たします。

A：S の 1 文字目から 1 文字目
AC：S の 1 文字目から 2 文字目
CA：S の 5 文字目から 6 文字目
CABCA：S の 5 文字目から 9 文字目
A：S の 6 文字目から 6 文字目
ABCA：S の 6 文字目から 9 文字目
CA：S の 8 文字目から 9 文字目
A：S の 9 文字目から 9 文字目
これら以外の部分文字列は条件を満たさないため、8 を出力してください。

A や CA は複数箇所から取り出すことができますが、取り出す場所が異なれば区別して数えることに注意してください。

入力例 2
Copy
4
CCBC
出力例 2
Copy
0
条件を満たす部分文字列が存在しないこともあります。

入力例 3
Copy
36
CABACBBBBBAABABACCBCABCCABAABABBCBAC
出力例 3
Copy
136
"""
N, S = input().split()
N = int(N)

# counter[d + N] = これまでの D_j のうち D_j = d の個数
counter = [0] * (2 * N + 1)

D = N          # C++の unsigned D{N};
counter[D] += 1

sum_ = 0       # C++の unsigned long sum
ans = 0        # C++の unsigned long ans

for c in S:
    if c == 'A':
        sum_ += counter[D]
        D += 1
    elif c == 'B':
        D -= 1
        sum_ -= counter[D]

    counter[D] += 1
    ans += sum_

print(ans)
