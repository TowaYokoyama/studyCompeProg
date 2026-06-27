"""
高橋君は鳥 1,2,…,N の N 羽の鳥を M 日間観察しました。
高橋君が観察した鳥には色 1,2,…,N の N 色のうちいずれか 1 色がついていますが、これらの鳥には観察期間中に色が変化するという興味深い特徴があります。

鳥 i は D 
i
​	
 −1 日目以前の観察では色 A 
i
​	
  であり、 D 
i
​	
  日目以降の観察では色 B 
i
​	
  になりました。
ただし、 D 
i
​	
 =1 である場合はその鳥の色は 1 日目の観察から B 
i
​	
  であり、 A 
i
​	
 =B 
i
​	
  である場合はその鳥の色は観察期間中に変化しませんでした。

j=1,2,…,M について、 j 日目の観察で鳥の色が何種類あったかを求めてください。

制約
1≤N≤3×10 
5
 
1≤M≤3×10 
5
 
1≤A 
i
​	
 ,B 
i
​	
 ≤N
1≤D 
i
​	
 ≤M
入力はすべて整数
入力
入力は以下の形式で標準入力から与えられる。

N M
A 
1
​	
  D 
1
​	
  B 
1
​	
 
A 
2
​	
  D 
2
​	
  B 
2
​	
 
⋮
A 
N
​	
  D 
N
​	
  B 
N
​	
 
出力
M 行出力せよ。
そのうち j 行目には、 j 日目に鳥の色が何種類あったかを出力せよ。

入力例 1
Copy
6 7
1 3 2
2 6 5
5 5 1
3 3 5
4 1 6
6 3 6
出力例 1
Copy
5
5
3
3
4
4
4
この入力では、 6 羽の鳥を 7 日間観察します。

1 日目の観察で、各鳥の色は 1,2,5,3,6,6 でした。鳥の色は全部で 5 種類です。
2 日目の観察で、各鳥の色は 1,2,5,3,6,6 でした。鳥の色は全部で 5 種類です。
3 日目の観察で、各鳥の色は 2,2,5,5,6,6 でした。鳥の色は全部で 3 種類です。
4 日目の観察で、各鳥の色は 2,2,5,5,6,6 でした。鳥の色は全部で 3 種類です。
5 日目の観察で、各鳥の色は 2,2,1,5,6,6 でした。鳥の色は全部で 4 種類です。
6 日目の観察で、各鳥の色は 2,5,1,5,6,6 でした。鳥の色は全部で 4 種類です。
7 日目の観察で、各鳥の色は 2,5,1,5,6,6 でした。鳥の色は全部で 4 種類です。
"""
from collections import defaultdict
N,M = map(int,input().split())

birds = []
for _ in range(N):
    A,D,B = map(int,input().split())
    
    birds.append((A,D,B))
    
#color_count[color]　＝その色の鳥の羽数
color_count = defaultdict(int)

# 変化イベント: events[day] = [(color_remove, color_add), ...]
events = defaultdict(list)

for A,D,B in birds:
    if D == 1:
        color_count[B] += 1
    else:
        color_count[A]+=1
        if A != B:
             events[D].append((A, B)) 
    
# 種類数 = color_count の中で count > 0 のキー数
# これを効率よく管理するため、0でない色の集合を追跡
active_colors = {c for c, cnt in color_count.items() if cnt > 0}

for day in range(1, M + 1):
    # この日に色が変わるイベントを処理
    for (remove_color, add_color) in events.get(day, []):
        color_count[remove_color] -= 1
        if color_count[remove_color] == 0:
            active_colors.discard(remove_color)
        
        color_count[add_color] += 1
        if color_count[add_color] == 1:
            active_colors.add(add_color)
    
    print(len(active_colors))