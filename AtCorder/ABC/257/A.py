"""
AtCorder.ABC.257.D の Docstring
問題文
A を N 個、B を N 個、…、Z を N 個この順に繋げて得られる文字列の先頭から X 番目の文字を求めてください。

制約
1≤N≤100
1≤X≤N×26
入力は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N X
出力
答えを出力せよ。

入力例 1
Copy
1 3
出力例 1
Copy
C
得られる文字列は ABCDEFGHIJKLMNOPQRSTUVWXYZ です。先頭から 3 番目の文字は C です。

入力例 2
Copy
2 12
出力例 2
Copy
F
得られる文字列は AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ です。先頭から 12 番目の文字は F です。
"""
N,X  = map(int,input().split())
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c =[]
for i in range(26):
    c.append(a[i] * N)


c = "".join(c)    
print(c[X-1])
    