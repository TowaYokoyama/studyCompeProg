"""
10 以上の正整数のうち、十進数表記したときに先頭の桁（最も大きい位）の数字がそれ以外のどの桁の数字よりも真に大きくなるようなものを ヘビ数 とよびます。 例えば、31 や 201 はヘビ数ですが、35 や 202 はヘビ数ではありません。

L 以上 R 以下のヘビ数が何個あるか求めてください。

制約
10≤L≤R≤10 
18
 
入力は全て整数
入力
入力は以下の形式で標準入力から与えられる。

L R
出力
答えを出力せよ。

入力例 1
Copy
97 210
出力例 1
Copy
6
97 以上 210 以下のヘビ数は、97,98,100,200,201,210 の 6 個です。

入力例 2
Copy
1000 9999
出力例 2
Copy
2025
入力例 3
Copy
252509054433933519 760713016476190692
出力例 3
Copy
221852052834757
"""

# n 進数を 10 進数に変換する
def base_n_to_10(n, string):
  string = string[::-1]
  n10 = 0
  for digit in range(len(string)):
    n10 += n ** digit * int(string[digit])
  return n10
  
# 桁数ごとに何個あるかをまず求めておく。19桁まで計算しておく。
count_by_digit = [0 for _ in range(20)]
for digit in range(2, 20):
  total = 0
  for num in range(1, 10):
    total += num ** (digit - 1)
  count_by_digit[digit] = total
# 使いやすくするため、累積和にして持っておく。
cum = [0 for _ in range(20)]
for i in range(1, 20):
  cum[i] = cum[i-1] + count_by_digit[i]

# 入力
L, R = input().split()
# L 以上の最小のヘビ数を求める。
LL = int(L[0]) 
for i in range(1, len(L)):
  if int(L[0]) <= int(L[i]):
    LL += 1
    LL *= 10 ** (len(L) - i)
    break
  else:
    LL = LL * 10 + int(L[i])
LL = str(LL)
# R 以上の最小のヘビ数を求める。
RR = int(R[0])
for i in range(1, len(R)):
  if int(R[0]) <= int(R[i]):
    RR += 1
    RR *= 10 ** (len(R) - i)
    break
  else:
    RR = RR * 10 + int(R[i])
RR = str(RR)

# LL が何番目であるのかを調べる。1 桁目を d とすると 2 桁目以降は d 進数の数になる。
d = int(LL[0])
order_L = base_n_to_10(d, LL[1:]) + 1 # 2 桁目以降を 10 進数に変換して何番目かを調べる。
for i in range(1, d): # 1 桁目が 1 から d-1 であるヘビ数の数を数える。
  order_L += i ** (len(LL) - 1)
order_L += cum[len(LL) - 1] # 桁数の少ない分を足す。
## RR についても同様。
d = int(RR[0])
order_R = base_n_to_10(d, RR[1:]) + 1
for i in range(1, d):
  order_R += i ** (len(RR) - 1)
order_R += cum[len(RR) - 1]

ans = order_R - order_L
if R == RR: # R 自身がヘビ数だったら 1 個余分に数える。
  ans += 1
print(ans)
