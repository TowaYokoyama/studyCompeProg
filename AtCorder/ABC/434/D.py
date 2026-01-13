"""
AtCorder.ABC.434.D の Docstring
は 2000×2000 のマス目で表されます。
空を見上げた時、上から r 行目、左から c 列目にあるマスを (r,c) と呼びます。

いま、この空には雲 1,2,…,N が浮かんでいます。
整数の組 (r,c) が U 
i
​	
 ≤r≤D 
i
​	
 ,L 
i
​	
 ≤c≤R 
i
​	
  を満たすとき、またその時に限り、 (r,c) は雲 i で覆われています。

k=1,2,…,N について、以下の問いに答えてください。

N 個の雲のうち、雲 k のみを取り除く。この時点で空には N−1 個の雲が浮かんでいる。このとき、どの雲にも覆われていないマスがいくつあるか答えよ。
制約
1≤N≤2×10 
5
 
1≤U 
i
​	
 ≤D 
i
​	
 ≤2000
1≤L 
i
​	
 ≤R 
i
​	
 ≤2000
入力される値は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N
U 
1
​	
  D 
1
​	
  L 
1
​	
  R 
1
​	
 
U 
2
​	
  D 
2
​	
  L 
2
​	
  R 
2
​	
 
⋮
U 
N
​	
  D 
N
​	
  L 
N
​	
  R 
N
​	
 
出力
N 行出力せよ。
i 行目には、 k=i とした場合の問いの答えを出力せよ。

入力例 1
Copy
5
2 4 1 4
3 3 3 5
1 3 4 6
4 5 3 5
5 5 4 6
出力例 1
Copy
3999983
3999976
3999982
3999978
3999977
図は、空のうち左上 5×6 の領域を抜き出したものです。



雲 1 を取り除いた際、何らかの雲に覆われているマスは 17 マスなので、どの雲にも覆われていないマスは 3999983 マスです。
雲 2 を取り除いた際、何らかの雲に覆われているマスは 24 マスなので、どの雲にも覆われていないマスは 3999976 マスです。
雲 3 を取り除いた際、何らかの雲に覆われているマスは 18 マスなので、どの雲にも覆われていないマスは 3999982 マスです。
雲 4 を取り除いた際、何らかの雲に覆われているマスは 22 マスなので、どの雲にも覆われていないマスは 3999978 マスです。
雲 5 を取り除いた際、何らかの雲に覆われているマスは 23 マスなので、どの雲にも覆われていないマスは 3999977 マスです。
"""
import sys
from array import array

# 入力をまとめて読む
data = list(map(int, sys.stdin.buffer.read().split()))
idx = 0

N = data[idx]
idx += 1

H = W = 2000

# 2次元いもす用の差分配列
diff = [array('i', [0]) * (W + 2) for _ in range(H + 2)]

rects = []

# 雲の入力
for _ in range(N):
    u = data[idx]; d = data[idx+1]
    l = data[idx+2]; r = data[idx+3]
    idx += 4

    rects.append((u, d, l, r))

    # 2次元いもす更新
    diff[u][l] += 1
    diff[d + 1][l] -= 1
    diff[u][r + 1] -= 1
    diff[d + 1][r + 1] += 1

# cnt == 1 のマス用の2次元累積和
S = [array('i', [0]) * (W + 1) for _ in range(H + 1)]

covered_all = 0  # 1枚以上の雲に覆われているマス数

# diff → cnt にしながら S を作る
for i in range(1, H + 1):
    for j in range(1, W + 1):
        diff[i][j] += diff[i-1][j] + diff[i][j-1] - diff[i-1][j-1]
        v = diff[i][j]

        if v > 0:
            covered_all += 1

        one = 1 if v == 1 else 0
        S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + one

total_cells = H * W
uncovered_all = total_cells - covered_all

# 各雲を除いたときの答え
out = []
for (u, d, l, r) in rects:
    # 雲kだけに覆われていたマス数
    unique = (
        S[d][r]
        - S[u-1][r]
        - S[d][l-1]
        + S[u-1][l-1]
    )
    out.append(str(uncovered_all + unique))

print("\n".join(out))
