A,B,C,D,E,F,X = map(int,input().split())

# 高橋
cycle_t = A + C
full_t = X // cycle_t
rest_t = X % cycle_t
walk_t = full_t * A + min(rest_t, A)
dist_t = walk_t * B

# 青木
cycle_a = D + F
full_a = X // cycle_a
rest_a = X % cycle_a
walk_a = full_a * D + min(rest_a, D)
dist_a = walk_a * E

if dist_t > dist_a:
    print("Takahashi")
elif dist_t < dist_a:
    print("Aoki")
else:
    print("Draw")

"""
問題文
高橋君と青木君はジョギングをすることにしました。
高橋君は「A 秒間秒速 B メートルで歩き、C 秒間休む」ことを繰り返します。
青木君は「D 秒間秒速 E メートルで歩き、F 秒間休む」ことを繰り返します。
二人が同時にジョギングを始めてから X 秒後、高橋君と青木君のうちどちらが長い距離を進んでいますか？

制約
1≤A,B,C,D,E,F,X≤100
入力は全て整数
入力
入力は以下の形式で標準入力から与えられる。

A B C D E F X
出力
二人が同時にジョギングを始めてから X 秒後時点で、高橋君の方が青木君よりも長い距離を進んでいるならば Takahashi、青木君の方が高橋君よりも長い距離を進んでいるならば Aoki、二人が同じ距離を進んでいるならば Draw と出力せよ。

入力例 1
Copy
4 3 3 6 2 5 10
出力例 1
Copy
Takahashi
二人はジョギングを始めてから 10 秒間の間、以下のように行動します。

高橋君は 4 秒間歩き、3 秒間休んだ後、再び 3 秒間歩く。合計 (4+3)×3=21 メートル歩く。
青木君は 6 秒間歩き、4 秒間休む。合計 6×2=12 メートル歩く。
高橋君の方が長い距離を進んでいるので、Takahashi と出力します。

入力例 2
Copy
3 1 4 1 5 9 2
出力例 2
Copy
Aoki
入力例 3
Copy
1 1 1 1 1 1 1
出力例 3
Copy
Draw

"""
