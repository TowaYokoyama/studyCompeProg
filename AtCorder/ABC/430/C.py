"""
AtCorder.ABC.430.C の Docstring
実行時間制限: 2 sec / メモリ制限: 1024 MiB

配点 : 300 点

問題文
AtCoder 国には「トラック運転手は A 分以上運転する際には B 分以上の休憩を取らなければならない」というルールがあります。
a, b からなる長さ N の文字列 S と正整数 A,B が与えられます。以下の条件を全て満たす整数組 (l,r) の個数を求めてください。

1≤l≤r≤N
S の l 文字目から r 文字目までに含まれる a の個数が A 以上
S の l 文字目から r 文字目までに含まれる b の個数が B 未満
制約
1≤N≤3×10 
5
 
1≤A,B≤N
S は a, b のみからなる長さ N の文字列
与えられる数値は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N A B
S
出力
答えを出力せよ。

入力例 1
Copy
11 4 2
abbaaabaaba
出力例 1
Copy
3
条件を満たす (l,r) の組は (4,8),(4,9),(5,9) の 3 個です。

入力例 2
Copy
13 1 2
bbbbbbbbbbbbb
出力例 2
Copy
0
条件を満たす (l,r) の組は存在しません。
"""
N, A, B = map(int, input().split())
S = input()

rA = 0  # aがA個以上になる最小rを探す右端（exclusive）
rB = 0  # bがB個に達する最小rを探す右端（exclusive）
a_cnt = 0
b_cnt = 0
ans = 0
INF = 10**18

for l in range(N):
    # a_l（aがA個以上になる最小r）を作る：足りないならrAを伸ばす
    while rA < N and a_cnt < A:
        if S[rA] == 'a':
            a_cnt += 1
        rA += 1
    a_l = (rA - 1) if a_cnt >= A else INF  # 存在しないならINF

    # b_l（bがB未満でいられる最大r）を作る：
    # bがB個に達する最小rを探す（達した位置の1つ手前が最大）
    while rB < N and b_cnt < B:
        if S[rB] == 'b':
            b_cnt += 1
        rB += 1
    if b_cnt >= B:
        b_l = rB - 2   # bがB個に達した最小rは(rB-1)なので、その1つ手前
    else:
        b_l = N - 1    # 最後までB個に達しないなら、どこまで伸ばしてもOK

    # このlで条件を満たすrの個数
    if a_l != INF and a_l <= b_l:
        ans += (b_l - a_l + 1)

    # 次のlへ：左端lを窓から外す（入っている場合だけ減らす）
    if l < rA and S[l] == 'a':
        a_cnt -= 1
    if l < rB and S[l] == 'b':
        b_cnt -= 1

print(ans)




            