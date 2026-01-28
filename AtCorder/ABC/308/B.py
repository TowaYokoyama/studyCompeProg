"""
問題文
高橋くんは回転寿司で N 皿の料理を食べました。 i 皿目の色は文字列 C 
i
​	
  で表されます。

また、料理の価格は皿の色と対応し、 i=1,…,M のそれぞれについて、色が文字列 D 
i
​	
  の皿の料理は一皿 P 
i
​	
  円です。また、D 
1
​	
 ,…,D 
M
​	
  のいずれとも異なる色の皿の料理は一皿 P 
0
​	
  円です。

高橋くんが食べた料理の価格の合計を求めてください。

制約
1≤N,M≤100
C 
i
​	
 ,D 
i
​	
  は英小文字からなる長さ 1 以上 20 以下の文字列
D 
1
​	
 ,…,D 
M
​	
  はすべて異なる
1≤P 
i
​	
 ≤10000
N,M,P 
i
​	
  は整数
入力
入力は以下の形式で標準入力から与えられる。

N M
C 
1
​	
  … C 
N
​	
 
D 
1
​	
  … D 
M
​	
 
P 
0
​	
  P 
1
​	
  … P 
M
​	
 
出力
答えを整数として出力せよ。

入力例 1
Copy
3 2
red green blue
blue red
800 1600 2800
出力例 1
Copy
5200
blue の皿は P 
1
​	
 =1600 円、red の皿は P 
2
​	
 =2800 円、green の皿は P 
0
​	
 =800 円です。

高橋くんが食べた料理の価格の合計は、2800+800+1600=5200 円です。

入力例 2
Copy
3 2
code queen atcoder
king queen
10 1 1
出力例 2
Copy
21
"""
N, M = map(int, input().split())
C = input().split()
D = input().split()
P = list(map(int, input().split()))

price = {}
for i in range(M):
    price[D[i]] = P[i+1]   # D_i の値段は P_{i+1}

ans = 0
for c in C:
    if c in price:
        ans += price[c]
    else:
        ans += P[0]

print(ans)
