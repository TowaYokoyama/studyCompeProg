"""
paiza.B.B145 の Docstring
B145:ビンゴゲームの判定
08秒経過
6時間経過で時間切れ
N × N のビンゴカードが 1 枚あります。
どのビンゴカードにも中央のマスには 0 が書かれており、最初から開けることができます。また、他のマスには数字がランダムに書かれています。
ただし、同じ数字が書かれたマスはありません。

これから K 回の抽選が行われます。
抽選では数字がランダムに排出されます。同じ数字が2回以上排出されることはありません。
ビンゴカードに抽選された数字と同じ数字が書かれたマスがあれば、そのマスを開けることができます。

ビンゴカードの縦横もしくは対角の斜め N 個のマスがすべて開けられたとき、ビンゴとします。
K 回の抽選の後、ビンゴの数を出力してください。

図1

たとえば、入力例 1 では 0, 9, 3, 13, 16, 8 が書かれた 6 つのマスを開けることができます。
縦、横、斜め、それぞれひとつずつビンゴになっており、ビンゴの数は合計で 3 となります。
評価ポイント
10回のテストケースで、正答率、実行速度、メモリ消費量をはかり得点が決まります。
より早い解答時間で提出したほうが得点が高くなります。
複数のテストケースで正しい出力がされるか評価（+50点）
解答までの速さ評価（+50点）
入力される値
入力は以下のフォーマットで与えられます。

N K
b_{1,1} b_{1,2} ... b_{1,N}
b_{2,1} b_{2,2} ... b_{2,N}
...
b_{N,1} b_{1,2} ... b_{N,N}
c_1 c_2 ... c_K
・1 行目にビンゴカードの縦横の大きさを表す整数 N と抽選回数を表す整数 K が半角スペース区切りで与えられます。
・続く 2 行目から N+1 行目までビンゴカードに書かれた数字が半角スペース区切りで与えられます。
・続く N+2 行目に抽選された数字が半角スペース区切りで与えられます。
・入力は合計で N+2 行となり、末尾に改行が 1 つ入ります。

それぞれの値は文字列で標準入力から渡されます。標準入力からの値取得方法はこちらをご確認ください
期待する出力
K 回の抽選の後のビンゴの数を出力してください。
末尾に改行を入れ、余計な文字、空行を含んではいけません。

条件
すべてのテストケースにおいて、以下の条件をみたします。

・3 ≦ N ≦ 21
・0 ≦ b_{i,j} ≦ 3*N^2 (1 ≦ i,j ≦ N)
・0 ≦ c_i ≦ 3*N^2 (1 ≦ i ≦ K)
・1 ≦ K ≦ 2*N^2-1
・N は奇数
・ビンゴカードの中央に書かれている数字は 0
・b_{i,j} および c_i に重複はない
入力例1
3 8
13 3 9
8 0 2
16 17 15
7 14 9 10 3 13 16 8
出力例1
3
入力例2
5 8
7 6 15 32 41
29 5 48 3 43
26 13 0 1 18
2 17 49 8 40
11 50 36 22 27
3 21 16 41 11 40 34 17
出力例2
1
入力例3
3 8
1 2 3
4 0 5
6 7 8
1 2 3 4 5 6 7 8
出力例3
8

"""
N, K = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(N)]
c = list(map(int, input().split()))

open = [[False]*N for _ in range(N)]

mid = N // 2
open[mid][mid] = True

# 抽選処理
for x in c:
    for i in range(N):
        for j in range(N):
            if b[i][j] == x:
                open[i][j] = True

bingo = 0

# 横
for i in range(N):
    if all(open[i][j] for j in range(N)):
        bingo += 1

# 縦
for j in range(N):
    if all(open[i][j] for i in range(N)):
        bingo += 1

# 斜め
if all(open[i][i] for i in range(N)):
    bingo += 1

if all(open[i][N-1-i] for i in range(N)):
    bingo += 1

print(bingo) 

# 辞書での解き方

N, K = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(N)]
c = list(map(int, input().split()))

# 数字 → 座標 の辞書
pos = {}
for i in range(N):
    for j in range(N):
        pos[b[i][j]] = (i, j)

# 中央は最初から開いている
row = [0] * N
col = [0] * N
diag1 = 0
diag2 = 0

mid = N // 2
row[mid] += 1
col[mid] += 1
diag1 += 1
diag2 += 1

# 抽選処理
for x in c:
    if x in pos:
        i, j = pos[x]

        row[i] += 1
        col[j] += 1

        if i == j:
            diag1 += 1
        if i + j == N - 1:
            diag2 += 1

# ビンゴ数を数える
bingo = 0

for i in range(N):
    if row[i] == N:
        bingo += 1
    if col[i] == N:
        bingo += 1

if diag1 == N:
    bingo += 1
if diag2 == N:
    bingo += 1

print(bingo)
