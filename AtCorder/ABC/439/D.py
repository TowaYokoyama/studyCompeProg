"""
D - Kadomatsu Subsequence   / 
実行時間制限: 2 sec / メモリ制限: 1024 MiB

配点 : 425 点

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
以下を全て満たす整数の 3 つ組 (i,j,k) がいくつあるか求めてください。

1≤i,j,k≤N
A 
i
​	
 :A 
j
​	
 :A 
k
​	
 =7:5:3
min(i,j,k)=j または max(i,j,k)=j
制約
入力は全て整数
1≤N≤3×10 
5
 
1≤A 
i
​	
 ≤10 
9
 
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
10
3 10 7 10 7 6 7 6 5 14
出力例 1
Copy
7
条件を満たす整数の 3 つ組 (i,j,k) は以下の 7 個です。

(3,9,1)
A 
i
​	
 :A 
j
​	
 :A 
k
​	
 =7:5:3 であり、 max(i,j,k)=j です。
(5,9,1)
A 
i
​	
 :A 
j
​	
 :A 
k
​	
 =7:5:3 であり、 max(i,j,k)=j です。
(7,9,1)
A 
i
​	
 :A 
j
​	
 :A 
k
​	
 =7:5:3 であり、 max(i,j,k)=j です。
(10,2,6)
A 
i
​	
 :A 
j
​	
 :A 
k
​	
 =14:10:6=7:5:3 であり、 min(i,j,k)=j です。
(10,2,8)
A 
i
​	
 :A 
j
​	
 :A 
k
​	
 =14:10:6=7:5:3 であり、 min(i,j,k)=j です。
(10,4,6)
A 
i
​	
 :A 
j
​	
 :A 
k
​	
 =14:10:6=7:5:3 であり、 min(i,j,k)=j です。
(10,4,8)
A 
i
​	
 :A 
j
​	
 :A 
k
​	
 =14:10:6=7:5:3 であり、 min(i,j,k)=j です。
入力例 2
Copy
6
210 210 210 210 210 210
出力例 2
Copy
0
入力例 3
Copy
21
49 30 50 21 35 15 21 70 35 9 50 70 21 49 30 50 70 15 9 21 30
出力例 3
Copy
34

"""
from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))

left = defaultdict(int)
right = defaultdict(int)

for a in A:
    right[a] += 1 #ここで頻度を覚えておく

ans = 0

for j in range(N):
    aj = A[j]
    right[aj] -= 1

    if aj % 5 == 0:
        t = aj // 5
        ans += left[7*t] * left[3*t]
        ans += right[7*t] * right[3*t]

    left[aj] += 1

print(ans)