"""
AtCorder.ABC.254.B の Docstring
問題文
以下のような N 個の整数列 A 
0
​	
 ,…,A 
N−1
​	
  を求めてください。

各 i (0≤i≤N−1) について、A 
i
​	
  の長さは i+1 である。
各 i,j (0≤i≤N−1,0≤j≤i) について、A 
i
​	
  の j+1 番目の値 a 
i,j
​	
  は次のように定められる。

j=0 または j=i の時、a 
i,j
​	
 =1
それ以外の時、a 
i,j
​	
 =a 
i−1,j−1
​	
 +a 
i−1,j
​	
 
制約
1≤N≤30
N は整数
入力
入力は以下の形式で標準入力から与えられる。

N
出力
N 行出力せよ。 i 行目には A 
i−1
​	
  の値を順に空白区切りで出力せよ。

入力例 1
Copy
3
出力例 1
Copy
1
1 1
1 2 1
入力例 2
Copy
10
出力例 2
Copy
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
1 8 28 56 70 56 28 8 1
1 9 36 84 126 126 84 36 9 1
"""
N = int(input())
"""
j=0 または j=i の時、a 
i,j
​	
 =1
それ以外の時、a 
i,j
​	
 =a 
i−1,j−1
​	
 +a 
i−1,j
​	
 
"""
#N_length = len(N)
ans = []
for i in range(N):
  row = [1] * (i+1)
  ans.append(row)
#全部１作ったパスカル三角形
for i in range(2,N):
  for j in range(1,i):
    if j == 0 or j == i:
      ans[i][j] = 1
    else:
      ans[i][j] = ans[i-1][j-1] + ans[i-1][j] 

for row in ans:
    print(" ".join(map(str, row)))