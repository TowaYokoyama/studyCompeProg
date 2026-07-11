""" 
 個のボールがあります。

i 番目のボールの色は C 
i
​	
 、大きさは S 
i
​	
  です。ここで、色は 1,2,…,M の整数で表されます。

k=1,2,…,M について、色 k のボールの大きさの最大値を出力してください。ただし、色 k のボールが存在しない場合は -1 と出力してください。

制約
1≤N,M≤100
1≤C 
i
​	
 ≤M
1≤S 
i
​	
 ≤100
入力される値はすべて整数
入力
入力は以下の形式で標準入力から与えられる。

N M
C 
1
​	
  S 
1
​	
 
C 
2
​	
  S 
2
​	
 
⋮
C 
N
​	
  S 
N
​	
 
出力
k=1,2,…,M の順に、色 k のボールが存在するならば色 k のボールの大きさの最大値を、存在しないならば -1 を空白区切りで出力せよ。

入力例 1
Copy
4 5
1 3
2 10
1 7
4 9
出力例 1
Copy
7 10 -1 9 -1
色 1 のボールの大きさの最大値は 7、色 2 のボールの大きさの最大値は 10、色 4 のボールの大きさの最大値は 9 です。

色 3 のボール、色 5 のボールは存在しません。

入力例 2
Copy
5 5
2 6
5 12
5 2
5 9
2 7
出力例 2
Copy
-1 7 -1 -1 12
"""
from collections import defaultdict
N,M = map(int,input().split())
ball_sizes = defaultdict(int)
for i in range(N):
    C,S = map(int,input().split())
    ball_sizes[C] = max(ball_sizes[C], S)
for k in range(1, M+1):
    print(ball_sizes[k] if ball_sizes[k] > 0 else -1)