"""
AtCorder.ABC.255.A の Docstring
問題文
整数 
R,C と 
2 行 
2 列からなる行列 
A が与えられるので、 
A 
R,C
​
  を出力してください。

制約
入力は全て整数
1≤R,C≤2
0≤A 
i,j
​
 ≤100
入力
入力は以下の形式で標準入力から与えられる。

R 
C
A 
1,1
​
  
A 
1,2
​
 
A 
2,1
​
  
A 
2,2
​
 
出力
答えを整数として出力せよ。

入力例 1
Copy
1 2
1 0
0 1
出力例 1
Copy
0
A 
1,2
​
 =0 です。

入力例 2
Copy
2 2
1 2
3 4
出力例 2
Copy
4
A 
2,2
​
 =4 です。

入力例 3
Copy
2 1
90 80
70 60
出力例 3
Copy
70
"""
R,C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(2)]
print(A[R-1][C-1])