"""
AtCorder.ABC.428.D の Docstring
正整数 x,y に対して f(x,y) を以下で定義します。

十進表記の x,y をそれぞれ文字列として解釈しこの順に連結して得られる文字列を z とする。z を十進表記の整数として解釈したときの値を f(x,y) とする。
たとえば f(3,14)=314, f(100,3)=1003 です。

正の整数 C,D が与えられます。以下を満たす整数 x の個数を求めてください。

1≤x≤D
f(C,C+x) は平方数である
T 個のテストケースが与えられるので、それぞれについて答えを求めてください。

制約
1≤T≤3×10 
5
 
1≤C≤2×10 
8
 
1≤D≤5×10 
9
 
入力される値はすべて整数
入力
入力は以下の形式で標準入力から与えられる。

T
case 
1
​	
 
case 
2
​	
 
⋮
case 
T
​	
 
case 
i
​	
  は i 番目のテストケースを表す。各テストケースは以下の形式で与えられる。

C D
出力
T 行出力せよ。i 行目 (1≤i≤T) には i 番目のテストケースに対する答えを出力せよ。

入力例 1
Copy
4
4 80
183 5000
18 10
824 5000000000
出力例 1
Copy
3
2
0
1421
1 番目のテストケースにおいて、条件を満たす x は x=5,37,80 の 3 通りです。

x=5 のとき f(C,C+5)=f(4,9)=49=7 
2
 
x=37 のとき f(C,C+37)=f(4,41)=441=21 
2
 
x=80 のとき f(C,C+80)=f(4,84)=484=22 
2
 
2 番目のテストケースにおいて、条件を満たす x は x=1,3133 の 2 通りです。

x=1 のとき f(C,C+1)=f(183,184)=183184=428 
2
 
x=3133 のとき f(C,C+3133)=f(183,3316)=1833316=1354 
2
 
3 番目のテストケースにおいて、条件を満たす x は 0 通りです。

4 番目のテストケースにおいて、条件を満たす x は 1421 通りです。
"""
import sys
import math

input = sys.stdin.readline

def ceil_sqrt(n):
    r = math.isqrt(n)
    if r * r == n:
        return r
    else:
        return r + 1


T = int(input())

# 10^L をあらかじめ用意
pow10 = [1]
for _ in range(20):
    pow10.append(pow10[-1] * 10)

ans_list = []

for _ in range(T):
    C, D = map(int, input().split())

    y_min_all = C + 1
    y_max_all = C + D

    # y の桁数の範囲
    L_start = len(str(y_min_all))
    L_end = len(str(y_max_all))

    ans = 0

    for L in range(L_start, L_end + 1):
        # L桁の範囲
        if L == 1:
            lo_d = 1
        else:
            lo_d = pow10[L - 1]
        hi_d = pow10[L] - 1

        y_min = max(y_min_all, lo_d)
        y_max = min(y_max_all, hi_d)

        if y_min > y_max:
            continue

        base = C * pow10[L]
        low = base + y_min
        high = base + y_max

        left = ceil_sqrt(low)
        right = math.isqrt(high)

        if left <= right:
            ans += right - left + 1

    ans_list.append(str(ans))

print("\n".join(ans_list))
