"""
問題文
AtCoder 食堂では主菜と副菜からなる定食が販売されています。
主菜は N 種類あり、順に主菜 1, 主菜 2, …, 主菜 N と呼びます。主菜 i の価格は a 
i
​	
  円です。
副菜は M 種類あり、順に副菜 1, 副菜 2, …, 副菜 M と呼びます。副菜 i の価格は b 
i
​	
  円です。

定食は主菜と副菜を 1 種類ずつ選んで構成されます。定食の価格は選んだ主菜の価格と副菜の価格の和です。
ただし、L 個の相異なる組 (c 
1
​	
 ,d 
1
​	
 ),…,(c 
L
​	
 ,d 
L
​	
 ) について、主菜 c 
i
​	
  と副菜 d 
i
​	
  からなる定食は食べ合わせが悪いため提供されていません。
つまり、提供されている定食は NM−L 種類あることになります。(提供されている定食が少なくとも 1 種類存在することが制約によって保証されています。)

提供されている定食のうち、最も価格の高い定食の価格を求めてください。

制約
1≤N,M≤10 
5
 
0≤L≤min(10 
5
 ,NM−1)
1≤a 
i
​	
 ,b 
i
​	
 ≤10 
9
 
1≤c 
i
​	
 ≤N
1≤d 
j
​	
 ≤M
i

=j ならば (c 
i
​	
 ,d 
i
​	
 )

=(c 
j
​	
 ,d 
j
​	
 )
入力される値は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N M L
a 
1
​	
  a 
2
​	
  … a 
N
​	
 
b 
1
​	
  b 
2
​	
  … b 
M
​	
 
c 
1
​	
  d 
1
​	
 
c 
2
​	
  d 
2
​	
 
⋮
c 
L
​	
  d 
L
​	
 
出力
提供されている定食のうち、最も価格の高い定食が何円であるかを出力せよ。

入力例 1
Copy
2 3 3
2 1
10 30 20
1 2
2 1
2 3
出力例 1
Copy
31
提供されている定食、及びその価格は次の 3 種類です。

主菜 1 と副菜 1 からなる定食。価格は 2+10=12 円である。
主菜 1 と副菜 3 からなる定食。価格は 2+20=22 円である。
主菜 2 と副菜 2 からなる定食。価格は 1+30=31 円である。
この中で最も高い定食は 3 番目の定食です。よって 31 を出力してください。

入力例 2
Copy
2 1 0
1000000000 1
1000000000
出力例 2
Copy
2000000000
入力例 3
Copy
10 10 10
47718 21994 74148 76721 98917 73766 29598 59035 69293 29127
7017 46004 16086 62644 74928 57404 32168 45794 19493 71590
1 3
2 6
4 5
5 4
5 5
5 6
5 7
5 8
5 10
7 3
出力例 3
Copy
149076
"""
import heapq 

N,M,L = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

"""
方針 A, B を降順ソート
heap に (0,0)
取り出す
禁止でなければそれが答え
禁止なら次候補を追加
繰り返し
"""
ban = set()
for _ in range(L):
    c,d = map(int,input().split())
    ban.add((c-1,d-1))
    
#値と元インデックスを保持
A = sorted([(a, i) for i, a in enumerate(A)], reverse=True)
B = sorted([(b, i) for i, b in enumerate(B)], reverse=True)

heap = []
visited = set()

#(和のマイナス,Aの位置,Bの位置)
heapq.heappush(heap, (-(A[0][0] + B[0][0]), 0,0 ))
visited.add((0,0))

while heap:
    neg_sum, i ,j = heapq.heappop(heap)
    
    org_i = A[i][1]
    org_j = B[j][1]
    
    if (org_i,org_j) not in ban:
        print(-neg_sum)
        break 
    
    #次候補
    if i+1 < N and (i+1, j) not in visited:
        heapq.heappush(heap, (-(A[i+1][0] + B[j][0]), i+1,j))
        visited.add((i+1,j))
    if j+1 < M and (i,j+1) not in visited:
        heapq.heappush(heap, (-(A[i][0] + B[j+1][0]), i, j+1))
        visited.add((i,j+1))
    
