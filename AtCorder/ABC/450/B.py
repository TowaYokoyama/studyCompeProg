"""
問題文
N 個の駅 1,2,…,N があり、これらはこの順に西から東に一直線上に並んでいます。
AtCoder 鉄道の電車はこれら N 個の駅を通り、西から東に走っています。
1≤i<j≤N を満たす任意の 2 整数 i,j について、駅 i から電車に乗って駅 j で降りるのにコストが C 
i,j
​	
  かかります。

以下のような 3 つの整数 a,b,c が存在するかを判定してください。

1≤a<b<c≤N
駅 a から電車に乗って駅 c で降りるときにかかるコストよりも、駅 a から電車に乗って駅 b で降り、再度、駅 b から電車に乗って駅 c で降りるときにかかるコストの総和の方が小さい。
制約
3≤N≤100
1≤C 
i,j
​	
 ≤10 
9
 
入力される値は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N
C 
1,2
​	
  C 
1,3
​	
  … C 
1,N
​	
 
C 
2,3
​	
  … C 
2,N
​	
 
⋮
C 
N−1,N
​	
 
出力
条件を満たす 3 整数 a,b,c が存在するならば Yes を、存在しないならば No を 1 行で出力せよ。

入力例 1
Copy
3
45 450
45
出力例 1
Copy
Yes
(a,b,c) として (1,2,3) を選ぶと、
C 
a,b
​	
 +C 
b,c
​	
 =C 
1,2
​	
 +C 
2,3
​	
 =45+45
C 
a,c
​	
 =C 
1,3
​	
 =450
なので、条件を満たします。

入力例 2
Copy
4
25 40 65
30 55
25
出力例 2
Copy
No
どのように (a,b,c) を選んでも、条件を満たしません。
"""
N = int(input())
C = {}
# graph = []


for i in range(1,N):
    move_c = list(map(int,input().split()))#駅iから行けるその駅までのコスト
    for k ,j in enumerate(range(i+1, N+1)):#k=何番目か,j=駅番号
        C[(i,j)] = move_c[k]  

found = False 
for a in range(1,N+1):
    for b in range(a+1,N+1):
        for c in range(b+1, N+1):
            if C[(a,b)] + C[(b,c)] < C[(a,c)]:
                found = True

print("Yes" if found else "No" )