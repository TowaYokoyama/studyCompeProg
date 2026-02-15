"""
AtCorder.ABC.216.D の Docstring
2N 個のボールがあります。各ボールには 1 以上 N 以下の整数によって表される色が塗られており、各色で塗られたボールはちょうど 2 個ずつ存在します。

これらのボールが、底が地面と平行になるように置かれた M 本の筒に入れられています。はじめ、i (1≤i≤M) 本目の筒には k 
i
​	
  個のボールが入っており、上から j (1≤j≤k 
i
​	
 ) 番目のボールの色は a 
i,j
​	
  です。

あなたの目標は、以下の操作を繰り返すことで M 本の筒全てを空にすることです。

異なる 2 本の空でない筒を選び、それぞれの筒の一番上にあるボールを取り出して捨てる。ここで、取り出して捨てた 2 つのボールは同じ色で塗られている必要がある。
目標が達成可能かを判定してください。

制約
1≤N≤2×10 
5
 
2≤M≤2×10 
5
 
1≤k 
i
​	
  (1≤i≤M)
1≤a 
i,j
​	
 ≤N (1≤i≤M,1≤j≤k 
i
​	
 )
∑ 
i=1
M
​	
 k 
i
​	
 =2N
全ての x (1≤x≤N) について、1≤i≤M かつ 1≤j≤k 
i
​	
  かつ a 
i,j
​	
 =x なる整数の組 (i,j) はちょうど 2 つ存在する
入力は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N M
k 
1
​	
 
a 
1,1
​	
  a 
1,2
​	
  … a 
1,k 
1
​	
 
​	
 
k 
2
​	
 
a 
2,1
​	
  a 
2,2
​	
  … a 
2,k 
2
​	
 
​	
 
⋮
k 
M
​	
 
a 
M,1
​	
  a 
M,2
​	
  … a 
M,k 
M
​	
 
​	
 
出力
目標が達成可能なら Yes を、達成不可能なら No を出力せよ。

入力例 1
Copy
2 2
2
1 2
2
1 2
出力例 1
Copy
Yes
以下のように操作を行えばよいです。

1 つ目の筒と 2 つ目の筒を選び、それぞれの筒の一番上にあるボールを取り出して捨てる。捨てられるボールの色は共に 1 であり等しいので、この操作は有効である。
1 つ目の筒と 2 つ目の筒を選び、それぞれの筒の一番上にあるボールを取り出して捨てる。捨てられるボールの色は共に 2 であり等しいので、この操作は有効である。
入力例 2
Copy
2 2
2
1 2
2
2 1
出力例 2
Copy
No
そもそも一度も操作を行うことができないため、目標を達成する、すなわち M 本の筒全てを空にすることは不可能です。
"""
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 各筒をdequeで管理
tubes = []
for _ in range(M):
    k = int(input())
    balls = list(map(int, input().split()))
    tubes.append(deque(balls))

# 色ごとに「今トップにある筒番号」を記録
color_pos = [[] for _ in range(N + 1)]

# 処理待ちキュー
queue = deque()

# 初期トップ登録
for i in range(M):
    if tubes[i]:
        c = tubes[i][0]
        color_pos[c].append(i)
        if len(color_pos[c]) == 2:
            queue.append(c)

removed = 0  # 消したペア数

while queue:
    color = queue.popleft()
    i, j = color_pos[color]

    # トップを取り除く
    tubes[i].popleft()
    tubes[j].popleft()
    removed += 1

    color_pos[color] = []

    # 新しいトップを確認
    for idx in (i, j):
        if tubes[idx]:
            new_c = tubes[idx][0]
            color_pos[new_c].append(idx)
            if len(color_pos[new_c]) == 2:
                queue.append(new_c)

if removed == N:
    print("Yes")
else:
    print("No")
