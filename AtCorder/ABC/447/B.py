"""
問題文
英小文字からなる文字列 S が与えられます。 S の中で出現回数が最も多い文字をすべて取り除き、残った文字を元の順序を保ったまま連結して出力してください。

なお、出現回数が最大の文字が複数種類ある場合は、そのすべてを取り除いてください。

制約
1≤∣S∣≤100
S は英小文字からなる文字列である
入力
入力は以下の形式で標準入力から与えられる。

S
出力
答えを出力せよ。

入力例 1
Copy
mississippi
出力例 1
Copy
mpp
mississippi に最も多く出現する文字は s と i でともに 4 回出現します。s と i をすべて取り除いた文字列は mpp となります。

入力例 2
Copy
atcoder
出力例 2
Copy
入力例 3
Copy
beginner
出力例 3
Copy
bgir
"""
from collections import defaultdict 

S = input()
dict = defaultdict(int)
for ch in S:
    dict[ch] += 1
# print(dict)
# 除外する文字のリスト
max_cnt = max(dict.values())

remove_chars = {ch for ch,cnt in dict.items() if cnt == max_cnt }

result = ""

for s in S:
    if s not in remove_chars:
        result += s 

print(result)