"""
長さ N の数列 A=(A 
1
​	
 ,A 
2
​	
 ,…,A 
N
​	
 ),B=(B 
1
​	
 ,B 
2
​	
 ,…,B 
N
​	
 ) が与えられます。
{1,2,…,N} の部分集合であって大きさが K のものを 1 つ選び S とします。この時、以下の式の値としてあり得る最小値を求めてください。

( 
i∈S
max
​	
 A 
i
​	
 )×( 
i∈S
∑
​	
 B 
i
​	
 )
T 個のテストケースが与えられるので、それぞれに対して答えを求めてください。

制約
1≤T≤2×10 
5
 
1≤K≤N≤2×10 
5
 
1≤A 
i
​	
 ,B 
i
​	
 ≤10 
6
 
全てのテストケースに対する N の総和は 2×10 
5
  以下
入力される値は全て整数
入力
入力は以下の形式で標準入力から与えられる。ここで case 
i
​	
  は i 番目のテストケースを意味する。

T
case 
1
​	
 
case 
2
​	
 
⋮
case 
T
​	
 
各テストケースは以下の形式で与えられる。

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
 
B 
1
​	
  B 
2
​	
  … B 
N
​	
 
出力
T 行出力せよ。i 行目には i 番目のテストケースの答えを出力せよ。

入力例 1
Copy
3
3 2
3 7 6
9 2 4
5 3
6 4 1 5 9
8 6 5 1 7
10 6
61 95 61 57 69 49 46 47 14 43
39 79 48 92 90 76 30 16 30 94
出力例 1
Copy
42
60
14579
1 番目のテストケースでは、S={2,3} を選ぶと式の値が 7×(2+4)=42 になり、これが最小です。
"""
import heapq 
T = int(input())
for _ in range(T):
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    
    #Aで昇順ソート
    AB = sorted(zip(A,B))
    
    heap = []
    subB = 0 
    ans = float('INF')
    
    for a,b in AB:
        #Bを追加
        heapq.heappush(heap, -b)
        subB+= b 
        
        #K個を超えたら最大Bを削除
        if len(heap) >K:
            removed = -heapq.heappop(heap)
            subB-= removed 
        #K個揃ったら計算
        if len(heap) == K:
            ans = min(ans, a* subB)
    
    print(ans)