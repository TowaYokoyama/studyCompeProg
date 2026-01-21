"""
AtCorder.ABC.182.C の Docstring
問題文
各桁に 0 が出現しないような正の整数 N が与えられます。
N の桁数を k とします。N の桁を 0 個以上 k 個未満消して、残った桁をそのままの順序で結合することで 3 の倍数を作りたいです。
3 の倍数を作ることができるか判定し、作ることができるなら作るのに必要な最少の消す桁数を求めてください。

制約
1≤N<10 
18
 
N は各桁に 0 が出現しない整数
入力
入力は以下の形式で標準入力から与えられる。

N
出力
3 の倍数を作ることができないなら -1 を、作ることができるなら作るのに必要な最少の消す桁数を出力せよ。

入力例 1
Copy
35
出力例 1
Copy
1
5 を消した 3 という数は 3 の倍数です。このとき消した桁数は 1 で最少です。

入力例 2
Copy
369
出力例 2
Copy
0
1 つも桁を消さなくてもいいことに注意してください。

入力例 3
Copy
6227384
出力例 3
Copy
1
例えば、 8 を消した 622734 は 3 の倍数です。

入力例 4
Copy
11
出力例 4
Copy
-1
消す桁数は N の桁数を k として 0 個以上 k 個未満でなければならないため、全部の桁を消すことはできないことに注意してください。
この場合問題文に従って 3 の倍数を作ることは不可能なため -1 を出力します。
"""
N = input()
digits = list(map(int, N))
k = len(digits)
S = sum(digits)

if S % 3 == 0:
    print(0)
    exit()

cnt1 = sum(1 for d in digits if d % 3 == 1)
cnt2 = sum(1 for d in digits if d % 3 == 2)

ans = 10**18

if S % 3 == 1:
    if cnt1 >= 1:
        ans = 1
    if cnt2 >= 2:
        ans = min(ans, 2)

elif S % 3 == 2:
    if cnt2 >= 1:
        ans = 1
    if cnt1 >= 2:
        ans = min(ans, 2)

# 全消しチェック
if ans >= k:
    print(-1)
else:
    print(ans if ans != 10**18 else -1)

N = input()
digits = list(map(int, N))
k = len(digits)

INF = 10**18
ans = INF

# mask: どの桁を「残す」か
for mask in range(1, 1 << k):  # 全消しは禁止なので 0 は除く
    s = 0        # 残した桁の和
    keep = 0     # 残した桁数

    for i in range(k):
        if (mask >> i) & 1:
            s += digits[i]
            keep += 1

    # 3の倍数判定
    if s % 3 == 0:
        removed = k - keep
        ans = min(ans, removed)

if ans == INF:
    print(-1)
else:
    print(ans)
