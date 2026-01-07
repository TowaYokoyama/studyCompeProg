"""
AtCorder.ABC.249.E の Docstring
E - RLE   / 
実行時間制限: 3 sec / メモリ制限: 1024 MiB

配点 : 500 点

問題文
英小文字のみからなる文字列 X に対し、以下の手続きによって文字列を得ることを考えます。

X を異なる文字が隣り合っている部分で分割する。
分割した各文字列 Y に対して、Y を Y を構成する文字と Y の長さを繋げた文字列に置き換える。
元の順番を保ったまま、置き換えた文字列をすべて繋げる。
例えば、aaabbcccc の場合、aaa,bb,cccc に分けられ、それぞれを a3,b2,c4 に置き換え、その順番のまま繋げることにより a3b2c4 を得ます。また、aaaaaaaaaa の場合、a10 になります。

長さ N の英小文字のみからなる文字列 S のうち、上記の手続きによって得られた文字列 T との長さを比べたとき、T の方が短いものの個数を P で割ったあまりを求めてください。

制約
1≤N≤3000
10 
8
 ≤P≤10 
9
 
N,P は整数
P は素数
入力
入力は以下の形式で標準入力から与えられる。

N P
出力
答えを出力せよ。

入力例 1
Copy
3 998244353
出力例 1
Copy
26
1,2,3 文字目が全て等しい文字列のみが条件を満たします。

例えば、aaa は a3 となり条件を満たしますが、abc は a1b1c1 となり条件を満たしません。

入力例 2
Copy
2 998244353
出力例 2
Copy
0
aa → a2 のように、長さが等しいものは条件を満たさないことに注意してください。

入力例 3
Copy
5 998244353
出力例 3
Copy
2626
aaabb や aaaaa などが条件を満たします。

入力例 4
Copy
3000 924844033
出力例 4
Copy
607425699
条件を満たす文字列の個数を 

"""
N, P = map(int, input().split())

# dp[i][j]:
# 長さ i の文字列を作って、RLE後の長さが j になる通り数
dp = [[0] * (N + 5) for _ in range(N + 1)]

# 初期状態：1文字置く
# RLEは「文字1 + 桁1」= 2
dp[1][2] = 26

# 桁数が増える境界
def inc_digit(x):
    return x == 1 or x == 9 or x == 99 or x == 999

# run[i]: i文字連続しているときの桁数
run_digit = [0] * (N + 1)
for i in range(1, N + 1):
    run_digit[i] = len(str(i))

# dp2[i][j][k]:
# 長さ i、RLE長 j、現在の連続長 k
dp2 = [[dict() for _ in range(N + 5)] for _ in range(N + 1)]

# 初期
for _ in range(26):
    dp2[1][2][1] = 26

for i in range(1, N):
    for j in range(1, N):
        for k, v in dp2[i][j].items():
            if v == 0:
                continue

            # 1. 同じ文字を続ける
            nk = k + 1
            nj = j
            if inc_digit(k):
                nj += 1
            if nj <= N:
                dp2[i + 1][nj][nk] = (dp2[i + 1][nj].get(nk, 0) + v) % P

            # 2. 別の文字に切り替える（25通り）
            nj = j + 2
            if nj <= N:
                dp2[i + 1][nj][1] = (dp2[i + 1][nj].get(1, 0) + v * 25) % P

# 集計
ans = 0
for j in range(N):
    for v in dp2[N][j].values():
        ans = (ans + v) % P

print(ans)
