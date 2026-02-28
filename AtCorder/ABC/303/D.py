"""
D - Shift vs. CapsLock   / 
実行時間制限: 2 sec / メモリ制限: 1024 MiB

配点 : 400 点

問題文
あなたのパソコンのキーボードには、a キー・Shift キー・CapsLock キーの 3 種類のキーがあります。また、CapsLock キーにはランプが付いています。 初め、CapsLock キーのランプは OFF であり、パソコンの画面には空文字列が表示されています。

あなたは、以下の 3 種類の操作のうち 1 つを選んで実行するということを 0 回以上何度でも行うことができます。

X ミリ秒かけて a キーのみを押す。CapsLock キーのランプが OFF ならば画面の文字列の末尾に a が付け足され、ON ならば A が付け足される。
Y ミリ秒かけて Shift キーと a キーを同時に押す。CapsLock キーのランプが OFF ならば画面の文字列の末尾に A が付け足され、 ON ならば a が付け足される。
Z ミリ秒かけて CapsLock キーを押す。CapsLock キーのランプが OFF ならば ON に、ON ならば OFF に切り替わる。
A と a からなる文字列 S が与えられます。画面の文字列を S に一致させるのに必要な最短の時間は何ミリ秒かを求めてください。

制約
1≤X,Y,Z≤10 
9
 
X,Y,Z は整数
1≤∣S∣≤3×10 
5
 
S は A と a からなる文字列
入力
入力は以下の形式で標準入力から与えられる。

X Y Z
S
出力
答えを出力せよ。

入力例 1
Copy
1 3 3
AAaA
出力例 1
Copy
9
以下のように操作を行うと 9 ミリ秒で画面の文字列を AAaA に一致させられます。これが最短の時間です。

Z(=3) ミリ秒かけて CapsLock キーを押す。CapsLock キーのランプが ON になる。
X(=1) ミリ秒かけて a キーを押す。A が画面の文字列の末尾に付け足される。
X(=1) ミリ秒かけて a キーを押す。A が画面の文字列の末尾に付け足される。
Y(=3) ミリ秒かけて Shift キーと a キーを同時に押す。a が画面の文字列の末尾に付け足される。
X(=1) ミリ秒かけて a キーを押す。A が画面の文字列の末尾に付け足される。
入力例 2
Copy
1 1 100
aAaAaA
出力例 2
Copy
6
入力例 3
Copy
1 2 4
aaAaAaaAAAAaAaaAaAAaaaAAAAA
出力例 3
Copy
40
"""
X, Y, Z = map(int, input().split())
S = input().strip()

INF = float('inf')
dp = [0, INF]  # dp[0] = CapsLockキー：off dp[1]=on

for ch in S:
    ndp = [INF, INF]
    for c in range(2):
        if dp[c] == INF:
            continue
        # 状態 c でのタイプコスト
        def cost(state):
            if state == 0:
                return X if ch == 'a' else Y
            else:
                return X if ch == 'A' else Y

        # そのまま打つ
        ndp[c] = min(ndp[c], dp[c] + cost(c))
        # CapsLock切り替えてから打つ
        nc = 1 - c
        ndp[nc] = min(ndp[nc], dp[c] + Z + cost(nc))
    dp = ndp

print(min(dp))