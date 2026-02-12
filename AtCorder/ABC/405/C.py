"""
AtCorder.ABC.405.C の Docstring
問題文
長さ N の整数列 A=(A 
1
​	
 ,A 
2
​	
 ,…,A 
N
​	
 ) が与えられます。

1≤i<j≤N
∑
​	
 A 
i
​	
 A 
j
​	
  の値を求めてください。

制約
2≤N≤3×10 
5
 
1≤A 
i
​	
 ≤10 
4
 
入力は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N
A 
1
​	
  A 
2
​	
  … A 
N
​	
 
出力
答えを出力せよ。

入力例 1
Copy
3
4 2 3
出力例 1
Copy
26
1≤i<j≤N
∑
​	
 A 
i
​	
 A 
j
​	
 =A 
1
​	
 A 
2
​	
 +A 
1
​	
 A 
3
​	
 +A 
2
​	
 A 
3
​	
 =4⋅2+4⋅3+2⋅3=26 です。

入力例 2
Copy
2
9 45
出力例 2
Copy
405
入力例 3
Copy
10
7781 8803 8630 9065 8831 9182 8593 7660 7548 8617
出力例 3
Copy
3227530139
"""
N = int(input())
A = list(map(int,input().split()))
sum_A = sum(A)
used_sum_A = sum_A **2
ans = 0
minas = 0
for x in A:
    minas += x **2
ans = (used_sum_A - minas) //2
print(ans)