"""
H 行 W 列で区切られた区域があります。この区域には、通行可能な区画と、通行不能な区画が存在します。

便宜上、この問題では縦 i 行目で横 j 列目の区画のことを (i, j) と表記します。

いま、通行可能な区画のみをたどることで、(1, 1) の区画から (H, W) の区画へ移動できないことがわかっています。しかし、あなたは通行不能な区画のうち、1 区画のみを通行可能にすることができます。

通行不能な区画 1 箇所を通行可能にすることで、(1, 1) から (H, W) へ移動できるようになる箇所が何箇所存在するかを求めてください。

入力例 1 の場合、通行可能な区画と通行不能な区画は次の通りです。


図1

この通行不能な区画のうち、(3, 3) を通行可能に変更することで (1, 1) から (H, W) へ移動できるようになります。

図2

他には、(3, 4) を通行可能に変更することで (1, 1) から (H, W) へ移動できるようになります。

図3

1 箇所のみを通行可能にすることで (1, 1) から (H, W) へ移動できるようになる箇所は以上の 2 箇所のみなので、2 と出力します。
評価ポイント
10個のテストケースを入力し、正答数と解答の提出までに要した時間を測定し得点が決まります。
※提出いただいたコードは複数回実行され、一度の実行では1つのテストケースのみ入力
※制限時間を超えるとテストケースが通っても失格(0点)となります。
得点の計算方法：正解数得点(50点) ＋ 正解率×解答時間得点(2時間以内で50点、4時間以内で25点、6時間で0点と線形に点数が落ちます)
10個のテストケースで正しい出力がされるか評価 (50点)
解答の提出までに要した時間による評価 (50点)
入力される値
入力は次のフォーマットで与えられます。
H W
s_1
s_2
...
s_H

・1 行目に縦の区画数 H と横の区画数 W が順に半角スペース区切りで与えられます。
・続く H 行のうちの i 行目 (1 ≦ i ≦ H) には半角記号 "." および "#" からなる長さ W の文字列 s_i が与えられます。s_i の j 番目 (1 ≦ j ≦ W) の文字は i 行 j 列目の区画が通行可能か ("." は通行可能、"#" は通行不能) を表します。
・入力は合計で H+1 行からなり、入力値最終行の末尾に改行が 1 つ入ります。

文字列は標準入力から渡されます。標準入力からの値取得方法はこちらをご確認ください
期待する出力
通行不能な区画 1 箇所を通行可能にすることで、(1, 1) から (H, W) へ移動できるようになる箇所の数を整数で出力してください。
末尾に改行を入れ、余計な文字、空行を含んではいけません。
条件
すべてのテストケースにおいて、以下の条件をみたします。
・1 ≦ H, W ≦ 1,000
・s_i (1 ≦ i ≦ H) は半角記号 ".", "#" のいずれかで構成される長さ W の文字列
・s_1 の 1 文字目と s_H の W 文字目は "."

言語別実行時間制限の詳細は こちら をご確認ください。
入力例1
5 7
...#.#.
....#..
#######
.#....#
#.#....
出力例1
2
入力例2
5 5
.....
####.
..#..
.####
.....
出力例2
5
入力例3
3 3
.#.
#.#
.#.
出力例3
0
"""
from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

# 壊した壁を保存する
# visited[x][y] に
# (壊した壁x, 壊した壁y)
# を入れる

visited = [[set() for _ in range(W)] for _ in range(H)]

queue = deque()

# まだ壁を壊してない状態
# (-1,-1) を特殊値にする
queue.append((0, 0, -1, -1))

visited[0][0].add((-1, -1))

while queue:
    x, y, bx, by = queue.popleft()

    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy

        if not (0 <= nx < H and 0 <= ny < W):
            continue

        # 道
        if S[nx][ny] == ".":

            if (bx, by) not in visited[nx][ny]:
                visited[nx][ny].add((bx, by))
                queue.append((nx, ny, bx, by))

        # 壁
        else:

            # まだ壁を壊してない時だけ
            if bx == -1:

                # この壁を壊したことにする
                if (nx, ny) not in visited[nx][ny]:
                    visited[nx][ny].add((nx, ny))
                    queue.append((nx, ny, nx, ny))

ans = set()

# ゴール地点へ来れた「壊した壁」を集める
for bx, by in visited[H-1][W-1]:

    # 壁を1回使ったものだけ
    if bx != -1:
        ans.add((bx, by))

print(len(ans))



# or 



from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(sx, sy):
    visited = [[False] * W for _ in range(H)]

    queue = deque()
    queue.append((sx, sy))

    visited[sx][sy] = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy

            if not (0 <= nx < H and 0 <= ny < W):
                continue

            # 道だけ進める
            if S[nx][ny] == "." and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return visited

# start側から到達可能
start = bfs(0, 0)

# goal側から到達可能
goal = bfs(H - 1, W - 1)

ans = 0

for i in range(H):
    for j in range(W):

        # 壁だけ見る
        if S[i][j] == "#":

            start_ok = False
            goal_ok = False

            # 周囲4方向を見る
            for dx, dy in dirs:
                ni = i + dx
                nj = j + dy

                if not (0 <= ni < H and 0 <= nj < W):
                    continue

                # start側に接してる
                if start[ni][nj]:
                    start_ok = True

                # goal側に接してる
                if goal[ni][nj]:
                    goal_ok = True

            # 両方に接してたら橋になる
            if start_ok and goal_ok:
                ans += 1

print(ans)