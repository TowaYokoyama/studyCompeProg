"""
英小文字からなる文字列 S,T が与えられます。

S の空でない部分文字列 s のうち、T を（連続するとは限らない）部分列として含まないものの個数を求めてください。

ここで、S の 2 つの部分文字列は、取り出した箇所が異なれば文字列として等しくても区別するものとします。

部分文字列とは
部分列とは
制約
S は英小文字からなる文字列
∣S∣ を S の長さとして、1≤∣S∣≤2×10 
5
 
T は英小文字からなる文字列
∣T∣ を T の長さとして、1≤∣T∣≤50
入力
入力は以下の形式で標準入力から与えられる。

S
T
出力
答えを出力せよ。

入力例 1
Copy
abrakadabra
aba
出力例 1
Copy
51
例えば、S の 1 文字目から 3 文字目までからなる部分文字列 abr は T を部分列として含みません。 他にも、k（S の 5 文字目のみ）や akada（S の 4 文字目から 8 文字目）などの 51 個の部分文字列が条件を満たします。

文字列 abr は S の 1 文字目から 3 文字目までからなる部分文字列としても S の 8 文字目から 10 文字目までからなる部分文字列としても得ることができますが、文字列から取り出す箇所が異なるため区別して数えることに注意してください。

入力例 2
Copy
aaaaa
a
出力例 2
Copy
0
S の空でない部分文字列は、すべて T を部分列として含みます。

よって、条件を満たす部分文字列は存在しないため、0 を出力してください。

入力例 3
Copy
rdddrdtdcdrrdcredctdordoeecrotet
dcre
出力例 3
Copy
263
"""

S = input()
T = input()
N = len(S)
M = len(T)

# nxt[i][c]: 位置i以降でcが最初に現れるindex（なければN）
INF = N
nxt = [[INF] * 26 for _ in range(N + 1)]

for i in range(N - 1, -1, -1):
    for c in range(26):
        nxt[i][c] = nxt[i + 1][c]
    nxt[i][ord(S[i]) - ord('a')] = i

ans = 0
for l in range(N):
    # 左端lからTを部分列として含む最短右端を求める
    pos = l
    for ch in T:
        pos = nxt[pos][ord(ch) - ord('a')]
        if pos == INF:
            break
        pos += 1
    
    if pos == INF:
        # Tを含めない → 全部カウント
        ans += N - l
    else:
        # S[l:pos-1]までは含まない、pos以降は含む
        ans += pos - 1 - l

print(ans)