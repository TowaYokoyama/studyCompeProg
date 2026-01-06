"""
AtCorder.ABC.439.C の Docstring

問題文
正整数 n が次の条件を満たす時、n を 良い整数 と呼びます。

0<x<y かつ x 
2
 +y 
2
 =n を満たす整数の組 (x,y) がただ 1 つ存在する。
例えば n=2026 とすると、0<x<y かつ x 
2
 +y 
2
 =n を満たす整数の組は (x,y)=(1,45) しか存在しないことが確認できます。よって 2026 は良い整数です。

正整数 N が与えられます。N 以下の良い整数を全て列挙してください。

制約
1≤N≤10 
7
 
N は整数
入力
入力は以下の形式で標準入力から与えられる。

N
出力
N 以下の良い整数が k 個あり、それらを昇順に並べた列が (a 
1
​	
 ,a 
2
​	
 ,…,a 
k
​	
 ) であるとする。この時、以下の形式で答えを出力せよ。(k=0 である場合は 2 行目は空行として出力せよ。)

k
a 
1
​	
  a 
2
​	
  … a 
k
​	
 
入力例 1
Copy
10
出力例 1
Copy
2
5 10
0<x<y かつ x 
2
 +y 
2
 =5 を満たす整数の組は (x,y)=(1,2) しか存在しないので 5 は良い整数です。
0<x<y かつ x 
2
 +y 
2
 =10 を満たす整数の組は (x,y)=(1,3) しか存在しないので 10 は良い整数です。
N 以下の良い整数はこの 2 個のみです。

入力例 2
Copy
1
出力例 2
Copy
0

入力例 3
Copy
50
出力例 3
Copy
14
5 10 13 17 20 25 26 29 34 37 40 41 45 50

"""
N = int(input())
"""
制約
1≤N≤10**7
N は整数
"""
#俺の回答
num_com = 0 #組数
ans = [] #その時のx**2+y**2 = n**2のnを入れるためのリスト
#x,y = 0
#良い整数候補のループ
for n in range(1,N+1):
  for x in range(1,N):
    for y in range(2,N):
      if x < y and x**2 +y **2 == n:
        num_com += 1
        ans.append(n)
  
print(num_com)
print(*ans)

#模範回答
"""ここが最大の発想転換
❌ n を決めて x,y を探す
⭕ x,y を決めて n を作る
"""
from collections import defaultdict
N = int(input())
cnt = defaultdict(int)

limit = int(N**0.5) + 1
for x in range(1, limit):
    for y in range(x + 1, limit):
        n = x * x + y * y 
        if n > N:
            break 
        cnt[n] += 1
        
ans = [n for n in cnt if cnt[n] == 1]
ans.sort()

print(len(ans))
print(*ans)#空白区切りで出力

"""
import numpy as np

N = int(input())

# 配列サイズ（次の2冪にするのが普通やけど、ここでは簡略）
size = N + 1

A = np.zeros(size, dtype=np.int64)

# 平方数の位置を 1 にする
i = 1
while i * i <= N:
    A[i * i] = 1
    i += 1

# FFT 畳み込み
FA = np.fft.fft(A)
C = np.fft.ifft(FA * FA)

# C[n] ≒ n = x^2 + y^2 の通り数（x,y 順序あり）
# 今回は 0 < x < y なので調整が必要やけど、雰囲気重視
ans = []
for n in range(1, N + 1):
    if int(round(C[n].real)) == 2:  # (x,y),(y,x) の2通り
        ans.append(n)

print(len(ans))
print(*ans)

"""