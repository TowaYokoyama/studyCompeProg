"""
AtCorder.326.D の Docstring
整数 N と A, B, C からなる長さ N の文字列 R,C が与えられるので、以下の問題を解いてください。

N×N のマス目があり、最初全てのマスは空きマスです。
各マスに A, B, C のうち高々 1 文字を書き込みます。( 空きマスのままにすることも許されます )

以下の条件を全て満たすことが可能であるか判定し、可能であれば書き込み方を 1 つ出力して下さい。

各行 / 各列 に A, B, C がちょうど 1 個ずつ含まれる
i 行目に書かれた文字の中で最も左にある文字は R の i 文字目と一致する
i 列目に書かれた文字の中で最も上にある文字は C の i 文字目と一致する
制約
N は 3 以上 5 以下の整数
R,C は A, B, C からなる長さ N の文字列
入力
入力は以下の形式で標準入力から与えられる。

N
R
C
出力
問題文中の条件を満たす書き込み方が存在しない場合、 No と 1 行に出力してください。
そうでない場合、以下の形式に従い書き込み方を出力してください。

Yes
A 
1
​	
 
A 
2
​	
 
⋮
A 
N
​	
 
まず、 1 行目に Yes と出力してください。 続く N 行のうちの i 行目に、長さ N の文字列である A 
i
​	
  を出力してください。

A 
i
​	
  の j 文字目が . であるとき、上から i 行目、左から j 列目のマスは空きマスであることを示します。
A 
i
​	
  の j 文字目が A であるとき、上から i 行目、左から j 列目のマスに A が書き込まれたことを示します。
A 
i
​	
  の j 文字目が B であるとき、上から i 行目、左から j 列目のマスに B が書き込まれたことを示します。
A 
i
​	
  の j 文字目が C であるとき、上から i 行目、左から j 列目のマスに C が書き込まれたことを示します。
正しい書き込み方が複数存在する場合、どれを出力しても構いません。

入力例 1
Copy
5
ABCBC
ACAAB
出力例 1
Copy
Yes
AC..B
.BA.C
C.BA.
BA.C.
..CBA
出力例のマス目は以下の条件を全て満たすため、正解として扱われます。

全ての行に A, B, C がちょうど 1 個ずつ含まれる
全ての列に A, B, C がちょうど 1 個ずつ含まれる
各行に書かれた最も左の文字は上から順に A, B, C, B, C である
各列に書かれた最も上の文字は左から順に A, C, A, A, B である
入力例 2
Copy
3
AAA
BBB
出力例 2
Copy
No
この入力では、条件を満たす書き込み方は存在しません。
"""
import sys
sys.setrecursionlimit(10**7)

N = int(input())
R = input()
C = input()

letters = ['A', 'B', 'C']

# -------------------------------------------------
# 1. 行パターンを事前列挙
#    条件：
#    - A,B,C が1個ずつ
#    - 残りは '.'
#    - 最左の文字が R[i] に対応できる
# -------------------------------------------------

from itertools import permutations

row_patterns = {ch: [] for ch in letters}

base = ['A', 'B', 'C'] + ['.'] * (N - 3)

for p in set(permutations(base)):
    # 最左の文字を取得
    first = None
    for x in p:
        if x != '.':
            first = x
            break
    if first is not None:
        row_patterns[first].append(p)

# -------------------------------------------------
# 2. DFS で上の行から決める
# -------------------------------------------------

# 列ごとの状態
# cnt[j][k] : 列 j に 文字 k (A,B,C) が何個あるか
cnt = [[0]*3 for _ in range(N)]
# top[j] : 列 j の最上の文字（まだなら None）
top = [None]*N

grid = []
found = False

def dfs(i):
    global found
    if found:
        return

    if i == N:
        # 最後に列に A,B,C がちょうど1個ずつあるか確認
        for j in range(N):
            if cnt[j][0] != 1 or cnt[j][1] != 1 or cnt[j][2] != 1:
                return
        print("Yes")
        for row in grid:
            print("".join(row))
        found = True
        return

    # 行 i の最左文字は R[i]
    for row in row_patterns[R[i]]:
        ok = True
        changed = []

        for j in range(N):
            ch = row[j]
            if ch == '.':
                continue

            k = ord(ch) - ord('A')

            # 列 j に同じ文字が2個以上はダメ
            if cnt[j][k] >= 1:
                ok = False
                break

            # 列の最上が未確定なら C[j] と一致する必要あり
            if top[j] is None:
                if ch != C[j]:
                    ok = False
                    break
                top[j] = ch
                changed.append(('top', j))

            cnt[j][k] += 1
            changed.append(('cnt', j, k))

        if ok:
            grid.append(row)
            dfs(i + 1)
            grid.pop()

        # 状態を戻す
        for item in reversed(changed):
            if item[0] == 'top':
                _, j = item
                top[j] = None
            else:
                _, j, k = item
                cnt[j][k] -= 1

        if found:
            return


dfs(0)

if not found:
    print("No")
