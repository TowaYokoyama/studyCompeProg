"""
AtCorder.鉄則本.B06 の Docstring
問題文
太郎君はくじを N 回引き，i 回目の結果は A 
i
​	
  でした．A 
i
​	
 =1 のときアタリ，A 
i
​	
 =0 のときハズレを意味します． 「L 回目から R 回目までの中では，アタリとハズレどちらが多いか？」という形式の質問が Q 個与えられるので， それぞれの質問に答えるプログラムを作成してください．

制約
1≤N,Q≤10 
5
 
0≤A 
i
​	
 ≤1
1≤L 
i
​	
 ≤R 
i
​	
 ≤N
入力はすべて整数
入力
入力は以下の形式で標準入力から与えられます．

N
A 
1
​	
  A 
2
​	
  ⋯ A 
N
​	
 
Q
L 
1
​	
  R 
1
​	
 
⋮
L 
Q
​	
  R 
Q
​	
 
出力
i=1,2,3,…,Q それぞれについて，アタリの方が多い場合 win を，ハズレの方が多い場合 lose を，アタリとハズレが同じ場合 draw を，一行ずつ，総計 Q 行に出力してください．

入力例 1
Copy
7
0 1 1 0 1 0 0
3
2 5
2 7
5 7
出力例 1
Copy
win
draw
lose
"""
N = int(input())
A = list(map(int,input().split()))
Q = int(input())
S = [0]*(N+1)
for i in range(N): 
    S[i+1] = S[i] + A[i]
# print(S)
for _ in range(Q):
    L,R = map(int,input().split())
    length = R -L +1
    hits = S[R] - S[L-1]
    if hits>length - hits:
        print("win")
    elif hits < length - hits:
        print("lose")
    else:
        print("draw")