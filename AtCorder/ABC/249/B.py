"""
AtCorder.ABC.249.B の Docstring


問題文
英大文字と英小文字からなる文字列のうち、以下の条件を全て満たすものを素晴らしい文字列ということとします。

英大文字が文字列の中に現れる。
英小文字が文字列の中に現れる。
全ての文字が相異なる。
例えば、AtCoder や Aa は素晴らしい文字列ですが、atcoder や Perfect は素晴らしい文字列ではありません。

文字列 S が与えられるので、S が素晴らしい文字列か判定してください。

制約
1≤∣S∣≤100
S は英大文字と英小文字からなる文字列である。
入力
入力は以下の形式で標準入力から与えられる。

S
出力
S が素晴らしい文字列ならば Yes を、そうでないならば No を出力せよ。

入力例 1
Copy
AtCoder
出力例 1
Copy
Yes
AtCoder は、英大文字が含まれ、英小文字も含まれ、かつ全ての文字が相異なるため素晴らしい文字列です。

入力例 2
Copy
Aa
出力例 2
Copy
Yes
A と a は違う文字であることに注意してください。この文字列は素晴らしい文字列です。

入力例 3
Copy
atcoder
出力例 3
Copy
No
英大文字が含まれていないため、素晴らしい文字列ではありません。

入力例 4
Copy
Perfect
出力例 4
Copy
No

"""
S = input()
has_upper = False 
has_lower = False 
for c in S:
    if c.isupper():
        has_upper = True 
        
    if c.islower():
        has_lower =True 

all_unique = len(S) == len(set(S))

if has_upper and has_lower and all_unique:
    print("Yes")
else:
    print("No")