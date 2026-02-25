"""
AtCoder社ではカードを使った 1 人ゲームが流行っています。
ゲームで使う各カードには、英小文字 1 文字または @ の文字が書かれており、いずれのカードも十分多く存在します。
ゲームは以下の手順で行います。

カードを同じ枚数ずつ 2 列に並べる。
@ のカードを、それぞれ a, t, c, o, d, e, r のいずれかのカードと置き換える。
2 つの列が一致していれば勝ち。そうでなければ負け。
このゲームに勝ちたいあなたは、次のようなイカサマをすることにしました。

手順 1 以降の好きなタイミングで、列内のカードを自由に並び替えてよい。
手順 1 で並べられた 2 つの列を表す 2 つの文字列 S,T が与えられるので、イカサマをしてもよいときゲームに勝てるか判定してください。

制約
S,T は英小文字と @ からなる
S,T の長さは等しく 1 以上 2×10 
5
  以下
入力
入力は以下の形式で標準入力から与えられる。

S
T
出力
イカサマをしてもよいとき、ゲームに勝てるなら Yes、勝てないなら No と出力せよ。

入力例 1
Copy
ch@ku@ai
choku@@i
出力例 1
Copy
Yes
@ をうまく置き換えることによって、両方とも chokudai と一致させることが可能です。

入力例 2
Copy
ch@kud@i
akidu@ho
出力例 2
Copy
Yes
イカサマをし、@ をうまく置き換えることによって、両方とも chokudai と一致させることが可能です。

入力例 3
Copy
aoki
@ok@
出力例 3
Copy
No
イカサマをしても勝つことはできません。

入力例 4
Copy
aa
bb
出力例 4
Copy
No
"""
from collections import Counter

S = input()
T = input()

cs = Counter(S)
ct = Counter(T)

allowed = set("atcoder")

for ch in set(cs.keys()) | set(ct.keys()):
    if ch == "@":
        continue
    
    diff = cs[ch] - ct[ch]
    
    if diff > 0:
        # Sの方が多い
        if ch in allowed:
            ct["@"] -= diff
        else:
            print("No")
            exit()
    elif diff < 0:
        # Tの方が多い
        if ch in allowed:
            cs["@"] += diff  # diffは負
        else:
            print("No")
            exit()

if cs["@"] >= 0 and ct["@"] >= 0:
    print("Yes")
else:
    print("No")