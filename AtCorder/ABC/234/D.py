"""
AtCorder.ABC.234.D の Docstring
問題文
(1,2,…,N) の順列 P=(P 
1
​	
 ,P 
2
​	
 ,…,P 
N
​	
 )、および正整数 K が与えられます。

i=K,K+1,…,N について、以下を求めてください。

P の先頭 i 項のうち、K 番目に大きい値
制約
1≤K≤N≤5×10 
5
 
(P 
1
​	
 ,P 
2
​	
 ,…,P 
N
​	
 ) は (1,2,…,N) の並び替えによって得られる
入力はすべて整数
入力
入力は以下の形式で標準入力から与えられる。

N K
P 
1
​	
  P 
2
​	
  … P 
N
​	
 
出力
i=K,K+1,…,N についてこの順に、問題文中で問われている値を改行区切りで出力せよ。

入力例 1
Copy
3 2
1 2 3
出力例 1
Copy
1
2
P の先頭 2 項、すなわち (P 
1
​	
 ,P 
2
​	
 )=(1,2) の中で K=2 番目に大きい値は 1 となります。
P の先頭 3 項、すなわち (P 
1
​	
 ,P 
2
​	
 ,P 
3
​	
 )=(1,2,3) の中で K=2 番目に大きい値は 2 となります。
入力例 2
Copy
11 5
3 7 2 5 11 6 1 9 8 10 4
出力例 2
Copy
2
3
3
5
6
7
7
"""
import heapq

N, K = map(int, input().split())
P = list(map(int, input().split()))

heap = []

# 最初のK個を入れる
for i in range(K):
    heapq.heappush(heap, P[i])

print(heap[0])

# 残り
for i in range(K, N):
    if P[i] > heap[0]:
        heapq.heappop(heap)#最小値を 取り出して削除する
        heapq.heappush(heap, P[i])
    
    print(heap[0])
