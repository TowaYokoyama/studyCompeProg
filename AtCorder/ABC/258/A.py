"""
AtCorder.ABC.258.A の Docstring
AtCoder Beginner Contest は通常、日本標準時で 21 時ちょうどに始まり 100 分間にわたって行われます。

0 以上 100 以下の整数 K が与えられます。21 時ちょうどから K 分後の時刻を HH:MM の形式で出力してください。ただし、HH は 24 時間制での時間を、MM は分を表します。時間または分が 1 桁のときは、先頭に 0 を追加して 2 桁の整数として表してください。

制約
K は 0 以上 100 以下の整数
入力
入力は以下の形式で標準入力から与えられる。

K
出力
21 時ちょうどから K 分後の時刻を問題文中の形式に従って出力せよ。

入力例 1
Copy
63
出力例 1
Copy
22:03
21 時ちょうどから 63 分後の時刻は 22 時 3 分なので、22:03 と出力します。

以下のような出力は不正解となります。

10:03
22:3
入力例 2
Copy
45
出力例 2
Copy
21:45
入力例 3
Copy
100
出力例 3
Copy
22:40

"""
K = int(input())
#HH:MM
HH = 21

h = K//60
m = K%60 
MM = 00 + m
if MM <10:
    MM = "".join(str(0)+str(MM))
while h>0:
    if HH+h <24:
        HH =HH +h
    else:
        HH = HH +h-24
    h-=1

print("".join(str(HH)+":"+str(MM)))    
K = int(input())

total = 21 * 60 + K
HH = total // 60
MM = total % 60

print(f"{HH:02d}:{MM:02d}")
