"""
a, b, c からなる文字列 S が与えられます。

S の空でない部分列であって、同じ文字が隣り合わないものの個数を 998244353 で割った余りを求めてください。

ただし、 2 つの部分列が文字列として一致しても、取り出す位置が異なるならば区別するものとします。

部分列とは
制約
S は a, b, c からなる長さ 1 以上 3×10 
5
  以下の文字列
入力
入力は以下の形式で標準入力から与えられる。

S
出力
答えを出力せよ。

入力例 1
Copy
abbc
出力例 1
Copy
11
同じ文字が隣合わない部分列は以下の 11 個です。

a ( S の 1 文字目)
b ( S の 2 文字目)
b ( S の 3 文字目)
c ( S の 4 文字目)
ab ( S の 1,2 文字目)
ab ( S の 1,3 文字目)
ac ( S の 1,4 文字目)
bc ( S の 2,4 文字目)
bc ( S の 3,4 文字目)
abc ( S の 1,2,4 文字目)
abc ( S の 1,3,4 文字目)
2 番目と 3 番目のもののように、文字列として一致しても、取り出す位置が異なるならば区別することに注意してください。

入力例 2
Copy
cabcabcbcaccacbcbcaabacbacaabccacbccbcacbacbacabcacabcaccaaaaabababcbabacaccabbcacbcbcbcababcbcbabca
出力例 2
Copy
378217423
998244353 で割った余りを出力してください。
"""
S = input()
mod = 998244353

dp = {'a':0,"b":0,"c":0}
ans = 0

for ch in S:
    "ch以外で終わる部分列合計 +1(chだけの場合)"
    new=0
    for c in dp:
        if c != ch:
            new += dp[c]
    
    new +=1
    new %=mod
    
    ans += new 
    ans %=mod
    dp[ch] = (dp[ch] + new) % mod
    
print(ans)