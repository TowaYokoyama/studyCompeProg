"""
AtCorder.ABS10.dream の Docstring
配点 : 300 点

問題文
英小文字からなる文字列 S が与えられます。 Tが空文字列である状態から始め、以下の操作を好きな回数繰り返すことで S=T とすることができるか判定してください。

T の末尾に dream dreamer erase eraser のいずれかを追加する。
制約
1≦∣S∣≦10 
5
 
S は英小文字からなる。
入力
入力は以下の形式で標準入力から与えられる。

S
出力
S=T とすることができる場合 YES を、そうでない場合 NO を出力せよ。

入力例 1
Copy
erasedream
出力例 1
Copy
YES
erase dream の順で T の末尾に追加することで S=T とすることができます。

入力例 2
Copy
dreameraser
出力例 2
Copy
YES
dream eraser の順で T の末尾に追加することで S=T とすることができます。

入力例 3
Copy
dreamerer
出力例 3
Copy
NO


"""
S = input()[::-1]

words = ["maerd", "remaerd", "esare", "resare"]

i = 0
while i < len(S):
    matched = False
    for w in words:
        if S[i:i+len(w)] == w:
            i += len(w)
            matched = True
            break
    if not matched:
        print("NO")
        exit()

print("YES")


S = input()
N = len(S)

words = ["dream", "dreamer", "erase", "eraser"]

dp = [False] * (N + 1)
dp[0] = True  # 空文字は作れる

for i in range(N):
    if not dp[i]:
        continue
    for w in words:
        if S[i:i+len(w)] == w:
            dp[i+len(w)] = True

print("YES" if dp[N] else "NO")
