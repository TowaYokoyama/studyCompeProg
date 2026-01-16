"""
AtCorder.ABC.428.B の Docstring
英小文字からなる長さ N の文字列 S が与えられます。

長さ K の文字列 t の出現回数を、以下を満たす整数 i の個数として定義します。

1≤i≤N−K+1
S の i 文字目から i+K−1 文字目までからなる部分文字列が t に一致する。
長さ K の文字列に対する出現回数の最大値 x を求めてください。 また、出現回数が x となるような長さ K の文字列をすべて辞書順昇順に出力してください。

制約
N,K は整数
S は英小文字からなる長さ N の文字列
1≤K≤N≤100
入力
入力は以下の形式で標準入力から与えられる。

N K
S
出力
2 行出力せよ。

1 行目には、長さ K の文字列に対する出現回数の最大値 x を出力せよ。

2 行目には、出現回数が x となるような長さ K の文字列を辞書順昇順に、空白区切りで出力せよ。

入力例 1
Copy
9 3
ovowowovo
出力例 1
Copy
2
ovo owo
出現回数 2 の文字列として、以下が挙げられます。

文字列 ovo について、i=1,7 が条件を満たすことから、ovo の出現回数は 2 です。
文字列 owo について、i=3,5 が条件を満たすことから、owo の出現回数は 2 です。
出現回数が 2 よりも大きいような長さ 3 の文字列は存在しないので、求める最大値は 2 です。

一方で、出現回数が 2 よりも小さい文字列として、以下が挙げられます。

文字列 vow について、i=2 が条件を満たすことから、vow の出現回数は 1 です。
文字列 ooo について、条件を満たす i が存在しないことから、ooo の出現回数は 0 です。
入力例 2
Copy
9 1
ovowowovo
出力例 2
Copy
5
o
入力例 3
Copy
35 3
thequickbrownfoxjumpsoverthelazydog
出力例 3
Copy
2
the
"""
N, K = map(int, input().split())
S = input()

cnt = {}

# ① 区間を全部見る
for i in range(N - K + 1):
    sub = S[i:i+K]
    cnt[sub] = cnt.get(sub, 0) + 1
"""
cnt.get(キー, デフォルト値)
キーが あれば → その値
キーが なければ → デフォルト値
"""
# ② 最大出現回数
max_cnt = max(cnt.values())

# ③ 最大のものを辞書順で出す
ans = []
for k, v in cnt.items():
    """
    ("ovo", 2)
("owo", 2)
("vow", 1)
...

    """
    if v == max_cnt:
        ans.append(k)

ans.sort()

# 出力
print(max_cnt)
print(" ".join(ans))

    