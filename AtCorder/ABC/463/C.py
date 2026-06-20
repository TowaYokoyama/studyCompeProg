"""
現在、会議室に N 人の高橋くんがいます。 i 番目 (1≤i≤N) の高橋くんの身長は H 
i
​	
  であり、今から L 
i
​	
  分後に会議室を去ります。 一度会議室を去った高橋くんはそれ以降会議室に戻ることはありません。

Q 個のクエリが与えられるので、順に答えてください。 i 番目 (1≤i≤Q) のクエリでは整数 T 
i
​	
  が与えられるので、今から T 
i
​	
 + 
2
1
​	
  分後に会議室にいる高橋くんの身長の最大値を答えてください。 この問題の制約のもとで、今から T 
i
​	
 + 
2
1
​	
  分後には会議室に 1 人以上の高橋くんがいることが保証されます。

制約
1≤N≤3×10 
5
 
1≤H 
i
​	
 ≤10 
9
  (1≤i≤N)
1≤L 
1
​	
 ≤L 
2
​	
 ≤⋯≤L 
N
​	
 ≤10 
9
 
1≤Q≤3×10 
5
 
0≤T 
i
​	
 <L 
N
​	
  (1≤i≤Q)
入力はすべて整数
入力
入力は以下の形式で標準入力から与えられる。

N
H 
1
​	
  L 
1
​	
 
H 
2
​	
  L 
2
​	
 
⋮
H 
N
​	
  L 
N
​	
 
Q
T 
1
​	
  T 
2
​	
  … T 
Q
​	
 
出力
Q 行にわたって出力せよ。 i 行目 (1≤i≤Q) には、i 番目のクエリに対する答えを出力せよ。

入力例 1
Copy
4
31 4
26 5
3 5
15 9
4
3 4 5 6
出力例 1
Copy
31
26
15
15
今から 3+ 
2
1
​	
  分後には、現在会議室にいる高橋くんは全員会議室にとどまっています。 よって、1 番目のクエリの答えは {31,26,3,15} の最大値である 31 です。

今から 5+ 
2
1
​	
  分後には、会議室には 4 番目の高橋くんだけがいます。 よって、3 番目のクエリの答えは {15} の最大値である 15 です。

入力例 2
Copy
10
587 138
772 155
755 404
519 408
529 432
169 586
114 632
249 656
329 972
299 984
14
443 801 824 276 399 314 300 510 311 580 498 930 359 5
出力例 2
Copy
329
329
329
755
755
755
755
329
755
329
329
329
755
772
"""
from sortedcontainers import SortedList

N = int(input())

people = []
heights = SortedList()

for _ in range(N):
    h, l = map(int, input().split())

    people.append((l, h))
    heights.add(h)

Q = int(input())
T = list(map(int, input().split()))

queries = []

for i, t in enumerate(T):
    queries.append((t, i))

queries.sort()

ans = [0] * Q

ptr = 0

for t, idx in queries:

    while ptr < N and people[ptr][0] <= t:
        l, h = people[ptr]

        heights.remove(h)

        ptr += 1

    ans[idx] = heights[-1]

for x in ans:
    print(x)
