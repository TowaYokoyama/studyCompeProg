"""
AtCorder.ABC.435.A の Docstring
問題文
正整数 N が与えられます。
1 以上 N 以下の整数をすべて足し合わせた値 1+2+⋯+N を出力してください。

制約
1≤N≤100
N は整数
入力
入力は以下の形式で標準入力から与えられる。

N
出力
1 以上 N 以下の整数をすべて足し合わせた値を出力せよ。

入力例 1
Copy
5
出力例 1
Copy
15
1+2+3+4+5=15 のため、15 を出力します。

入力例 2
Copy
1
出力例 2
Copy
1
入力例 3
Copy
29
出力例 3
Copy
435
"""
N = int(input())
ans = 0
for i in range(N+1):
    ans += i
    
print(ans)