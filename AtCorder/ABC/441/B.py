"""
AtCorder.ABC.441.B の Docstring
AtCoder 国の公用語は、高橋語と青木語の 2 つの言語です。

高橋語と青木語は、どちらもその言語に含まれる単語を表記するのに英小文字の一部を使います。 高橋語では長さ N の文字列 S に含まれる文字のみを使い、青木語では長さ M の文字列 T に含まれる文字のみを使います。

AtCoder 国の公用語に含まれる Q 個の単語 w 
1
​	
 ,w 
2
​	
 ,…,w 
Q
​	
  が与えられます。 それぞれの単語について、その単語に含まれる文字からその単語が次のうちどれに該当するか判定してください。

高橋語の単語であることが確定する
青木語の単語であることが確定する
どちらともいえない
制約
1≤N≤26
1≤M≤26
S は英小文字からなる長さ N の文字列
S に含まれる文字は先頭からアルファベット順で昇順に並んでいる
S に含まれる文字はすべて異なる
T は英小文字からなる長さ M の文字列
T に含まれる文字は先頭からアルファベット順で昇順に並んでいる
T に含まれる文字はすべて異なる
1≤Q≤100
w 
i
​	
  は英小文字からなる長さ 1 以上 100 以下の文字列 (1≤i≤Q)
w 
i
​	
  は高橋語か青木語のどちらかの単語 (1≤i≤Q)
N,M,Q は整数
入力
入力は以下の形式で標準入力から与えられる。

N M
S
T
Q
w 
1
​	
 
w 
2
​	
 
⋮
w 
Q
​	
 
出力
Q 行にわたって出力せよ。 i 行目には、w 
i
​	
  が高橋語の単語であることが確定するなら Takahashi 、青木語の単語であることが確定するなら Aoki 、どちらとも確定しないなら Unknown と出力せよ。

入力例 1
Copy
6 5
ahikst
aikot
5
asahi
okita
kiai
hash
it
出力例 1
Copy
Takahashi
Aoki
Unknown
Takahashi
Unknown
例えば、a, s, h, i はすべて高橋語で使われる文字で、h は青木語で使われる文字ではないので asahi は高橋語の単語であることが確定します。 よって、1 行目には Takahashi と出力してください。

i および t はどちらも高橋語でも青木語でも使われる文字なので it は高橋語の単語であるとも青木語の単語であるとも確定しません。 よって、5 行目には Unknown と出力してください。

入力例 2
Copy
7 6
ahiknst
ahikos
5
kioki
ohiki
tashi
nishi
kashi
出力例 2
Copy
Aoki
Aoki
Takahashi
Takahashi
Unknown
o は高橋語で使われる文字ではないので、はじめ 2 つの単語は青木語の単語であることが確定します。 よって、1 行目と 2 行目には Aoki と出力してください。

t や n は青木語で使われる文字ではないので、続く 2 つの単語は高橋語の単語であることが確定します。 よって、3 行目と 4 行目には Takahashi と出力してください。

はじめ 4 つの単語については、末尾が shi なら高橋語、末尾が ki なら青木語という法則がありますが、k, a, s, h, i はいずれも高橋語と青木語の両方で使われる文字なので kashi がどちらの言語の単語であるかを使われている文字から確定させることはできません。 よって、5 行目には Unknown と出力してください。

入力例 3
Copy
13 11
defghiqsvwxyz
acejmoqrtwx
15
qhsqzhd
jcareec
wwqxqew
wxqxwex
jxxrtwa
trtqjxe
sqyggse
xxqwxew
xewwxxw
wwqxwex
xqqxqwq
qxxexxe
teqeroc
eeeqqee
vxdevyy
出力例 3
Copy
Takahashi
Aoki
Unknown
Unknown
Aoki
Aoki
Takahashi
Unknown
Unknown
Unknown
Unknown
Unknown
Aoki
Unknown
Takahashi
"""
N,M = map(int,input().split())
S = set(input())
T = set(input())
Q = int(input())
w = []
for _ in range(Q):
    z = input()
    w.append(set(z))

for x in w:
    if x.issubset(S) and not x.issubset(T) :
        print("Takahashi")
    elif x.issubset(T) and not x.issubset(S):
        print("Aoki")
    
    else:
        print("Unknown")