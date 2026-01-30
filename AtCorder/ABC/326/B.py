"""
AtCorder.326.C の Docstring
3 桁の正整数であって、百の位の数と十の位の数の積が一の位の数と等しいものを 326-like number と呼びます。

例えば 326,400,144 は 326-like number であり、623,777,429 は 326-like number ではありません。

整数 N が与えられるので、N 以上の最小の 326-like number を求めてください。なお、制約の条件下で答えは必ず存在します。

制約
100≤N≤919
N は整数である
入力
入力は以下の形式で標準入力から与えられる。

N
出力
答えを出力せよ。

入力例 1
Copy
320
出力例 1
Copy
326
320,321,322,323,324,325 は 326-like number ではなく、326 は 326-like number です。

入力例 2
Copy
144
出力例 2
Copy
144
144 は 326-like number です。

入力例 3
Copy
516
出力例 3
Copy
600

"""
N = int(input())
for x in range(N,1000):
    #３桁
    a = x // 100        # 百の位
    b = (x // 10) % 10 # 十の位
    c = x % 10         # 一の位
    if a * b == c:
        print(x)
        break