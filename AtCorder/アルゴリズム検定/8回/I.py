"""
AtCorder.アルゴリズム検定.8回.I の Docstring
問題文
長さ N の正整数のみからなる数列 A=(A 
1
​	
 ,A 
2
​	
 ,…,A 
N
​	
 ) が与えられます。
この数列に以下の操作を 0 回以上何度でも行ってよいとき、数列の項の最小値として達成可能な最大値を求めてください。

まず、数列の中から偶数である項を 1 つ選び、その項を 2 で割る。次に、数列の中から任意の項を 1 つ選び、その項を 3 倍する。
制約
入力は全て整数
1≤N≤10 
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
答えを整数として出力せよ。

入力例 1
Copy
3
18 21 46
出力例 1
Copy
23
例えば、以下の操作を行うことで、項の最小値を 23 にすることができます。

はじめ、A=(18,21,46) である。
A 
1
​	
  を 2 で割り、 A 
1
​	
  を 3 倍する。この操作の後、数列は A=(27,21,46) となる。
A 
3
​	
  を 2 で割り、 A 
2
​	
  を 3 倍する。この操作の後、数列は A=(27,63,23) となる。
入力例 2
Copy
5
3 5 7 11 13
出力例 2
Copy
3
一度も操作が行えない場合もあります。

入力例 3
Copy
1
536870912
出力例 3
Copy
68630377364883
"""
import sys
import math
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# 各数の2の個数を数える
total_two = 0
for i in range(N):
    while A[i] % 2 == 0:
        A[i] //= 2
        total_two += 1

# 判定関数
def ok(x):
    need = 0
    for a in A:
        if a >= x:
            continue
        # 何回3倍すればx以上？
        k = 0
        val = a
        while val < x:
            val *= 3
            k += 1
            if k > total_two:
                return False
        need += k
        if need > total_two:
            return False
    return True

# 二分探索
low = 0
high = 10**18

while high - low > 1:
    mid = (low + high) // 2
    if ok(mid):
        low = mid
    else:
        high = mid

print(low)

import heapq

N = int(input())
A = list(map(int, input().split()))

heap = []
k = 0

# 2で割れるだけ割る
for a in A:
    while a % 2 == 0:
        a //= 2
        k += 1
    heapq.heappush(heap, a)

# k回、最小に3をかける
for _ in range(k):
    x = heapq.heappop(heap)
    x *= 3
    heapq.heappush(heap, x)

print(heap[0])
