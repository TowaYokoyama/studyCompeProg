"""
AtCorder.ABC.249.D の Docstring

D - Index Trio   / 
実行時間制限: 2 sec / メモリ制限: 1024 MiB

配点 : 400 点

問題文
長さ N の整数列 A=(A 
1
​	
 ,…,A 
N
​	
 ) が与えられます。

以下の条件を全て満たす整数の組 (i,j,k) の総数を求めてください。

1≤i,j,k≤N
A 
j
​	
 
A 
i
​	
 
​	
 =A 
k
​	
 
制約
1≤N≤2×10 
5
 
1≤A 
i
​	
 ≤2×10 
5
 (1≤i≤N)
入力は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N
A 
1
​	
  … A 
N
​	
 
出力
答えを出力せよ。

入力例 1
Copy
3
6 2 3
出力例 1
Copy
2
(i,j,k)=(1,2,3),(1,3,2) が条件を満たします。

入力例 2
Copy
1
2
出力例 2
Copy
0
入力例 3
Copy
10
1 3 2 4 6 8 2 2 3 7
出力例 3
Copy
62
""" 
from collections import Counter
N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)
"""
cnt = {
  1: 1,
  2: 2,
  3: 1
}

"""
maxA = max(A)

ans = 0

#A_i = x とする
for x in cnt:
    for z in range(x, maxA + 1, x):   # z = x * y
        #z は x の倍数だけを見る
        if z in cnt:
            y = z // x
            if y in cnt:
                ans += cnt[x] * cnt[y] * cnt[z]

print(ans)
