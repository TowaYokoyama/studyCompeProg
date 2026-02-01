"""
AtCorder.ABC.211.C の Docstring
問題文
文字列 S が与えられます。
このうち 8 文字を選び下線を引き、下線を引いた文字が左から順に c , h , o , k , u , d , a , i となるようにする方法は何通りありますか？
ただし答えは非常に大きくなる可能性があるので、(10 
9
 +7) で割った余りを出力してください。

制約
8≤∣S∣≤10 
5
 
S は英小文字からなる
入力
入力は以下の形式で標準入力から与えられる。

S
出力
答えを (10 
9
 +7) で割った余りを出力せよ。

入力例 1
Copy
chchokudai
出力例 1
Copy
3
chchokudai
chchokudai
chchokudai
上の 3 つが条件を満たします。

chchokudai
は、条件を満たさないことに注意してください。

入力例 2
Copy
atcoderrr
出力例 2
Copy
0
答えが 0 通りになることもあります。

入力例 3
Copy
chokudaichokudaichokudai
出力例 3
Copy
45
"""
S = input()
mod = (10 ** 9 + 7)

target = "chokudai"
dp = [0] * 9 #今、target の何文字目まで完成しているか

dp[0] = 1 #から文字

for ch in S:
    for i in range(8):
        if ch == target[i]:
            dp[i +1] = (dp[i+1] + dp[i]) % mod 

print(dp[8])