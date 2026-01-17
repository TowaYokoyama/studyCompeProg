"""
AtCorder.ABC.424.C の Docstring
高橋君はゲームをしています。このゲームには 1 から N の番号がついた N 個のスキルがあります。

N 個の整数の組 (A 
1
​	
 ,B 
1
​	
 ),…,(A 
N
​	
 ,B 
N
​	
 ) が与えられます。
(A 
i
​	
 ,B 
i
​	
 )=(0,0) のとき高橋君はスキル i を習得済みです。
そうでないとき、スキル A 
i
​	
 ,B 
i
​	
  の少なくとも一方を習得済みのときかつそのときに限りスキル i を習得することができます。

既に取得済みのスキルも含め、高橋君が最終的に習得することができるスキルの個数を求めてください。

制約
1≤N≤2×10 
5
 
(A 
i
​	
 ,B 
i
​	
 )=(0,0) または 1≤A 
i
​	
 ,B 
i
​	
 ≤N
入力は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N
A 
1
​	
  B 
1
​	
 
A 
2
​	
  B 
2
​	
 
⋮
A 
N
​	
  B 
N
​	
 
出力
答えを出力せよ。

入力例 1
Copy
6
0 0
1 3
3 2
5 5
4 6
6 4
出力例 1
Copy
3
最初、高橋君はスキル 1 を習得済みです。スキル 1 を習得済みのためスキル 2 を習得することができ、スキル 2 を習得したことでスキル 3 を習得できます。
スキル 4,5,6 を習得することはできないため、答えは 3 となります。

入力例 2
Copy
4
0 0
0 0
0 0
0 0
出力例 2
Copy
4

"""
from collections import deque 

N = int(input())

A = [0]*(N+1)
B = [0] * (N+1)

#このスキルを条件にして取れるスキル一覧
need = [[] for _ in range(N+1)]

#すでにとっているかどうか
have = [False] * (N+1) 

q = deque()


#入力を読む
for i in range(1,N+1):
    a,b = map(int,input().split())
    A[i] = a 
    B[i] = b 
    
    if a == 0 and b == 0:
        #最初から取れている
        have[i] = True 
        q.append(i)
    else:
        #aまたはbを取ったらiが取れる
        need[a].append(i)
        need[b].append(i)

#取れたスキルを起点に広げる
while q:
    x =  q.popleft()
    
    for nxt in need[x]:
        if not have[nxt]:
            have[nxt] = True 
            q.append(nxt)
            
#取れたスキルを数える
ans = sum(have[1:])

print(ans)