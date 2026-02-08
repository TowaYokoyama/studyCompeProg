"""
AtCorder.ABC.317.B の Docstring
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
2 3 5
出力例 1
Copy
4
ナオヒロ君は初め 2,3,4,5 の 4 個の整数を持っており、4 をなくし、2,3,5 が残っていました。

なくした整数である 4 を出力します。

入力例 2
Copy

出力例 2
Copy
7
入力例 3
Copy
16
152 153 154 147 148 149 158 159 160 155 156 157 144 145 146 150
出力例 3
Copy
151
"""
N = int(input())
A = list(map(int,input().split()))
A.sort()
default_l = N + 1
for i in range(default_l):
    if A[i+1] != A[i] + 1: 
        print(A[i]+1)
        exit()
