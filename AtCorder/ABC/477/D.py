"""
問題文
N 個のマスが横一列に並んでおり、左から順にマス 1 からマス N までの番号がついています。色は英小文字で表されます。

はじめ、すべてのマスの色は a で、各マスには何も置かれていません。

Q 個のクエリが与えられるので、与えられた順に処理してください。各クエリは以下の 2 種類のいずれかです。

1 X : マス X にタイルが置かれていなければタイルを置き、置かれていれば取り除く。

2 C : タイルが置かれていないすべてのマスの色を C に変更する。

すべてのクエリを処理した後の各マスの色を（タイルが置かれているかどうかにかかわらず）求めてください。

LLM向けの情報はこちら: https://atcoder.jp/r/FMsc0k5o7q6trK_1NyMAmrR3SSg-XEyrbfx69aKWQqxqsoIZ-PtAIYczGooZU4ZMThLsIGr5IDMwIL3q5oFF5pMj3x9Bc4M
翻訳に関する情報はこちら: https://atcoder.jp/r/FMsc0k5o7q6trK_1NyMAmrR3SSg-XEyrbfx69aKWQqxqsoIZ-PtAIYczGooZU4ZMThLsIGr5IDMwIL3q5oFF5pMj3x9Bc4M?reason=t
制約
1≤N,Q≤3×10 
5
 
各クエリはタイプ 1 またはタイプ 2 のいずれか
タイプ 1 のクエリにおいて、X は 1≤X≤N を満たす整数
タイプ 2 のクエリにおいて、C は英小文字 1 文字
入力
入力は以下の形式で標準入力から与えられる。

N Q
query 
1
​	
 
⋮
query 
Q
​	
 
各クエリ query 
i
​	
  (1≤i≤Q) は

1 X
または、

2 C
の形で与えられる。

出力
最終的な各マスの色を、左から順につなげた長さ N の文字列として出力せよ。

入力例 1
Copy
3 5
1 2
2 b
1 1
1 2
2 c
出力例 1
Copy
bcc
タイルの状態について、置かれているならば #、 そうでないならば . として左から順につなげた文字列で表現をすることにします。

クエリによって、以下のようにマスの色・タイルの状態が変化します。はじめの状態は aaa と ... です。

1 つ目のクエリを処理すると、マス 2 にタイルが置かれる。状態は aaa と .#. となる。
2 つ目のクエリを処理すると、タイルの置かれていないマスの色が b に変更される。状態は bab と .#. となる。
3 つ目のクエリを処理すると、マス 1 にタイルが置かれる。状態は bab と ##. となる。
4 つ目のクエリを処理すると、マス 2 のタイルが取り除かれる。状態は bab と #.. となる。
5 つ目のクエリを処理すると、タイルの置かれていないマスの色が c に変更される。状態は bcc と #.. となる。
よって bcc と出力してください。マス 1 にはタイルが置かれたままですが、その場合であってもマスの色を出力します。

入力例 2
Copy
10 15
1 8
2 m
1 3
1 10
2 q
1 6
1 10
2 d
1 1
2 z
1 9
2 f
1 4
1 7
2 k
出力例 2
Copy
dkmfkqfazk
"""

N, Q = map(int, input().split())

# 各マスにタイルがあるか
tile = [False] * N

# 各マスが最後にタイルを置かれた時点
last = [0] * N

# その時点での「全体の色」
color = 'a'

# 各時点での色を保存
colors = ['a'] * (Q + 1)

for t in range(1, Q + 1):
    query = input().split()

    if query[0] == '1':
        x = int(query[1]) - 1

        if tile[x]:
            # タイルを取り除く
            tile[x] = False
        else:
            # タイルを置く
            tile[x] = True
            last[x] = t

    else:
        # 全体の色を変更
        color = query[1]
        colors[t] = color

    # タイプ2でない場合も、その時点の色を引き継ぐ
    if colors[t] == 'a':
        colors[t] = colors[t - 1]

answer = []

for i in range(N):
    # 最後にタイルを置いた時点より後に
    # 色変更があったかを見る
    answer.append(colors[Q] if last[i] <= 0 else colors[last[i]])

print(''.join(answer))