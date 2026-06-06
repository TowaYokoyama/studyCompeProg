"""
N 個の宝石があります。i 番目の宝石の色（整数で表されます）は C 
i
​	
  で価値は V 
i
​	
  です。

この N 個の宝石の中から K 個を選びます。ただし、選んだ宝石の色が M 種類以上なければなりません。

このとき、選んだ宝石の価値の総和としてありうる最大値を求めてください。（与えられる入力では、このような選択が必ず可能です。）

制約
1≤M≤K≤N≤2×10 
5
 
1≤C 
i
​	
 ≤N
1≤V 
i
​	
 ≤10 
9
 
M 種類以上の色の宝石が存在する
入力される値はすべて整数
入力
入力は以下の形式で標準入力から与えられる。

N K M
C 
1
​	
  V 
1
​	
 
C 
2
​	
  V 
2
​	
 
⋮
C 
N
​	
  V 
N
​	
 
出力
選んだ宝石の価値の総和としてありうる最大値を整数として出力せよ。

入力例 1
Copy
5 3 2
1 30
1 40
1 50
2 10
3 20
出力例 1
Copy
110
この例では 5 個の宝石から 3 個を選びます。選んだ宝石の色が 2 種類以上なければなりません。

宝石 2,3,5 を選ぶと、それらの色は 1,1,3 で 2 種類あります。それらの価値の総和は 40+50+20=110 で、これがありうる最大値です。

入力例 2
Copy
5 3 3
1 30
1 40
1 50
2 10
3 20
出力例 2
Copy
80
宝石や選ぶ個数は入力例 1 と同じですが、選んだ宝石の色が 3 種類以上なければなりません。

宝石 3,4,5 を選ぶと、それらの色は 1,2,3 で 3 種類あります。それらの価値の総和は 50+10+20=80 で、これがありうる最大値です。

入力例 3
Copy
5 5 1
4 1000000000
5 1000000000
4 1000000000
5 1000000000
4 1000000000
出力例 3
Copy
5000000000
"""
from collections import defaultdict 
N,K,M = map(int,input().split())#宝石の数,選ぶ数、Cの最低数
gems = []
color_map = defaultdict(list)
#各色から「最高価値の宝石」をM個の色分 → 強制的に選ぶ
#の頃のK-M枠は全宝石の中から価値が高い順に埋めていく。
for _ in range(N):
    C,V = map(int,input().split())#Color,value
    #価値の最大でソート
    gems.append((V,C))
    color_map[C].append(V)
# 各色の最大価値を取得してソート（色の代表）
color_best = sorted([max(v) for v in color_map.values()], reverse=True)
# M種類の色を確保（各色の最大価値の宝石を選ぶ）
must_pick = set()
forced = color_best[:M]  # M色分の代表
# 強制選択した宝石を除いた残り全部を価値順に並べる
# 全宝石を価値順にソート
gems.sort(reverse=True)

# M色それぞれから1個ずつ確保する処理
color_used = defaultdict(int)
selected = []
remaining = []

for V, C in gems:
    if color_used[C] == 0 and len(selected) < M:
        selected.append(V)
        color_used[C] += 1
    else:
        remaining.append(V)

# 残りK-M枠を価値が高い順に埋める
result = sum(selected) + sum(remaining[:K-M])
print(result)