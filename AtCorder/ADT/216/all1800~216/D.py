"""
AtCorder.ADT.all1800~216.D の Docstring
健康に気を使っている高橋君は、M 種類の栄養素について、食事によって十分な量を摂取できているか気になりました。

i 番目の栄養素は 1 日あたり A 
i
​	
  以上摂取することが目標です。

高橋君は今日 N 品の食品を食べ、i 品目の食品からは栄養素 j を X 
i,j
​	
  摂取しました。

M 種類全ての栄養素で目標を達成しているかどうかを判定してください。

制約
1≤N≤100
1≤M≤100
0≤A 
i
​	
 ,X 
i,j
​	
 ≤10 
7
 
入力は全て整数である
入力
入力は以下の形式で標準入力から与えられる。

N M
A 
1
​	
  … A 
M
​	
 
X 
1,1
​	
  … X 
1,M
​	
 
⋮
X 
N,1
​	
  … X 
N,M
​	
 
出力
M 種類全ての栄養素で目標を達成しているなら Yes、そうでないならば No を出力せよ。

入力例 1
Copy
2 3
10 20 30
20 0 10
0 100 100
出力例 1
Copy
Yes
栄養素 1 は 1 品目から 20、2 品目から 0 摂取したため、合わせて 20 摂取しており、10 以上摂取するという目標を達成しています。
栄養素 2,3 についても同様に目標を達成しています。

入力例 2
Copy
2 4
10 20 30 40
20 0 10 30
0 100 100 0
出力例 2
Copy
No
栄養素 4 について目標を達成していません。
"""
N,M = map(int,input().split())
A = list(map(int,input().split()))
X = [list(map(int, input().split())) for _ in range(N)]
ok = True
for j in range(M):
    total = 0
    for i in range(N):
        total+=X[i][j]
    
    if total < A[j]:
        ok = False
print("Yes" if ok else "No")