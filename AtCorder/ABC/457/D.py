"""
問題文
長さ N の数列 A=(A 
1
​	
 ,A 
2
​	
 ,…,A 
N
​	
 ) と整数 K が与えられます。

あなたは次の操作を 0 回以上 K 回以下行うことができます。

1≤i≤N を満たす整数 i を 1 つ選び、A 
i
​	
  に i を加える。
操作後の数列に対する  
1≤i≤N
min
​	
 A 
i
​	
  としてありうる最大値を求めてください。

制約
1≤N≤2×10 
5
 
1≤A 
i
​	
 ≤10 
18
 
1≤K≤10 
18
 
入力される値はすべて整数
入力
入力は以下の形式で標準入力から与えられる。

N K
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
3 3
1 2 3
出力例 1
Copy
3
例えば i=1 を 2 回、 i=2 を 1 回選ぶと、数列は (3,4,3) になります。このとき最小値は 3 です。

最小値を 4 以上にすることはできないため、 3 と出力して下さい。

入力例 2
Copy
4 5
10 1 10 1
出力例 2
Copy
7
入力例 3
Copy
20 457
8 9 10 9 8 8 4 6 8 1 5 10 2 8 2 6 8 1 6 6
出力例 3
Copy
132
"""

"""
i を選び、Ai に i を加える
最小値min(A)が操作ができない状態まで行い、操作後に最大値としての下限の値
最終的に min を X にできる？」
"""
N, K = map(int, input().split())
A = list(map(int, input().split()))

def ok(x):
    total = 0
    for i in range(N):
        if A[i] >= x:
            continue
        need = (x - A[i] + (i + 1) - 1) // (i + 1)
        total += need
        if total > K:  # 早期終了
            return False
    return True

okv = 0
ng = max(A) + N * K + 1  # 安全な上限

while ng - okv > 1:
    mid = (okv + ng) // 2
    if ok(mid):
        okv = mid
    else:
        ng = mid

print(okv)