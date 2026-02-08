"""
AtCorder.ABC.444.B の Docstring
問題文
正整数 n の桁和を、 n を十進法で表したときの各桁の和と定めます。例えば 2026 の桁和は 2+0+2+6=10 です。

N 以下の正整数のうち、桁和が K であるものの個数を求めてください。

制約
1≤N,K≤10 
5
 
入力は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N K
出力
答えを出力せよ。

入力例 1
Copy
30 4
出力例 1
Copy
3
30 以下の正整数のうち、桁和が 4 であるものは、4,13,22 の 3 個です。

入力例 2
Copy
2026 10
出力例 2
Copy
121
入力例 3
Copy
99999 45
出力例 3
Copy
1

"""
N, K = map(int, input().split())

ans = 0

for s in range(1, N + 1):

    if s < 10:
        digit_sum = s

    elif s < 100:
        digit_sum = s // 10 + s % 10

    elif s < 1000:
        digit_sum = s // 100 + (s // 10) % 10 + s % 10

    elif s < 10000:
        digit_sum = (
            s // 1000 +
            (s // 100) % 10 +
            (s // 10) % 10 +
            s % 10
        )

    else:  # 10000〜100000
        digit_sum = (
            s // 10000 +
            (s // 1000) % 10 +
            (s // 100) % 10 +
            (s // 10) % 10 +
            s % 10
        )

    if digit_sum == K:
        ans += 1

print(ans)

N,K = map(int,input().split())
ans = 0
for i in range(1,N+1):
    a = str(i)
    tmp = 0
    for j in range(len(a)):
        tmp += int(a[j])
    if tmp == K:
        ans += 1

print(ans)