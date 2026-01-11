"""
AtCorder.ABC.440.D の Docstring
問題文
相異なる N 個の整数からなるリストがあります。リストの i 個目 (1≤i≤N) の整数は A 
i
​	
  です。

Q 個の質問が与えられるので、それぞれの答えを求めてください。j 個目の質問 (1≤j≤Q) は以下の通りです。

X 
j
​	
  以上の整数であってリストに含まれないもののうち、小さいほうから Y 
j
​	
  番目の値を求めよ。
制約
1≤N≤3×10 
5
 
1≤Q≤3×10 
5
 
1≤A 
i
​	
 ≤10 
9
  (1≤i≤N)
A 
1
​	
 ,…,A 
N
​	
  は相異なる
1≤X 
j
​	
 ≤10 
9
  (1≤j≤Q)
1≤Y 
j
​	
 ≤10 
9
  (1≤j≤Q)
入力される値はすべて整数
入力
入力は以下の形式で標準入力から与えられる。

N Q
A 
1
​	
  ⋯ A 
N
​	
 
X 
1
​	
  Y 
1
​	
 
⋮
X 
Q
​	
  Y 
Q
​	
 
出力
Q 行出力せよ。j 行目 (1≤j≤Q) には j 個目の質問の答えを出力せよ。

入力例 1
Copy
5 4
16 9 2 3 1
6 10
12 4
1 1
1000000000 1000000000
出力例 1
Copy
17
15
4
1999999999
1 個目の質問について、6 以上の整数であってリストに含まれないもののうち、小さいほうから 10 個を挙げると 6, 7, 8, 10, 11, 12, 13, 14, 15, 17 となります。したがって、質問の答えは 17 です。

2 個目の質問について、12 以上の整数であってリストに含まれないもののうち、小さいほうから 4 個を挙げると 12, 13, 14, 15 となります。したがって、質問の答えは 15 です。

3 個目の質問について、1 以上の整数であってリストに含まれないもののうち、小さいほうから 1 番目の値は 4 です。

4 個目の質問について、1000000000 以上の整数であってリストに含まれないもののうち、小さいほうから 1000000000 番目の値は 1999999999 です。

入力例 2
Copy
10 10
284008711 658403910 982178205 50598815 694147827 230009803 763277509 509451676 821970166 284008710
740250292 159734720
255870361 8400028
23659634 718117163
697334729 301140741
698853172 270344164
713418715 285312509
50065000 52368934
46642556 591869945
607623561 273664826
482426028 265015448
出力例 2
Copy
899985013
264270388
741776803
998475472
969197337
998731226
102433934
638512505
881288390
747441478
"""
import bisect 

N,Q = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

for _ in range(Q):
  X,Y = map(int,input().split())
  
  #探索範囲d
  low = X 
  high = X+Y+N #Aが全部が言ってもたりる範囲
  
  while low < high:
    mid = (low + high)//2
    
    #x以上mid以下に含まれるAの個数
    cnt = bisect.bisect_right(A,mid)- bisect.bisect_left(A,X)
    
    #欠番の数
    missing = (mid-X+1) -cnt
    
    if missing >= Y:
      high = mid
      
    else:
      low = mid + 1
      
  print(low)
  
  
  
  import bisect

def solve(a, x, y, idx1, k):
  # X+Y-1+K 以下の最大の A の index
  idx2 = bisect.bisect_right(a, x+y-1+k) - 1
  num_included_A = max(0, idx2 - idx1 + 1) # 一応 idx1がidx2を飛び越えないように
  return k >= num_included_A

N, Q = map(int, input().split())
A = [0] + list(map(int, input().split()))
A.sort()
ans = []
for _ in range(Q):
  X, Y = map(int, input().split())
  # これは最初に求めておく。毎回 idx2 と一緒に計算してたら TLE になった。
  idx1 = bisect.bisect_left(A, X)

  ok = N
  ng = -1
  while (abs(ok - ng) > 1):
    mid = (ok + ng) // 2
    if solve(A, X, Y, idx1, mid):
      ok = mid
    else:
      ng = mid
  ans.append(X+Y-1+ok)

for an in ans:
  print(an)
