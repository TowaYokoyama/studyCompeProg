"""
AtCorder.ABC.273.A の Docstring
問題文
非負整数 x に対し定義される関数 f(x) は以下の条件を満たします。

f(0)=1
任意の正整数 k に対し f(k)=k×f(k−1)
このとき、 f(N) を求めてください。

制約
N は 0≤N≤10 を満たす整数
入力
入力は以下の形式で標準入力から与えられる。

N
出力
答えを整数として出力せよ。

入力例 1
Copy
2
出力例 1
Copy
2
f(2)=2×f(1)=2×1×f(0)=2×1×1=2 です。

入力例 2
Copy
3
出力例 2
Copy
6
f(3)=3×f(2)=3×2=6 です。

入力例 3
Copy
0
出力例 3
Copy
1
入力例 4
Copy
10
出力例 4
Copy
3628800
"""
N = int(input())

def f(N):
    if N == 0:
        return 1
    return N * f(N-1)
print(f(N))