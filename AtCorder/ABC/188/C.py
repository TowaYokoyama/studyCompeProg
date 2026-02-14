"""
AtCorder.ABC.188.C の Docstring
問題文
選手 1 から選手 2 
N
  までの 2 
N
  人の選手がトーナメント形式のプログラミング対決をします。
選手 i のレートは A 
i
​	
  です。どの 2 人の選手のレートも異なり、2 人の選手が対戦すると常にレートが高い方が勝ちます。

トーナメント表は完全二分木の形をしています。
より正確には、このトーナメントは以下の要領で行われます。

i=1,2,3,…,N について順に、以下のことが行われる。

各整数 j(1≤j≤2 
N−i
 ) について、まだ負けたことのない選手のうち、 2j−1 番目に番号の小さい選手と 2j 番目に番号の小さい選手が対戦する。
準優勝する、すなわち最後に行われる対戦において負ける選手の番号を求めてください。

制約
1≤N≤16
1≤A 
i
​	
 ≤10 
9
 
A 
i
​	
  は相異なる
入力に含まれる値は全て整数である
入力
入力は以下の形式で標準入力から与えられる。

N
A 
1
​	
  A 
2
​	
  A 
3
​	
  … A 
2 
N
 
​	
 
出力
準優勝する選手の番号を出力せよ。

入力例 1
Copy
2
1 4 2 5
出力例 1
Copy
2
まず選手 1 と 2、選手 3 と 4 がそれぞれ対戦し、レートの大小から選手 2 と 4 が勝利します。
次に選手 2 と選手 4 が対戦し、選手 4 が勝利してトーナメントが終了します。
最後の対戦で負けるのは選手 2 なので、2 を出力します。

入力例 2
Copy
2
3 1 5 4
出力例 2
Copy
1
まず選手 1 と 2、選手 3 と 4 がそれぞれ対戦し、レートの大小から選手 1 と 3 が勝利します。
次に選手 1 と選手 3 が対戦し、選手 3 が勝利してトーナメントが終了します。
最後の対戦で負けるのは選手 1 なので、1 を出力します。

入力例 3
Copy
4
6 13 12 5 3 7 10 11 16 9 8 15 2 1 14 4
出力例 3
Copy
2
"""
from collections import deque

N = int(input())
A = list(map(int, input().split()))

# (番号, レート) を入れる
queue = deque((i+1, A[i]) for i in range(len(A)))

while len(queue) > 1:
    next_round = deque()
    
    while queue:
        p1 = queue.popleft()
        p2 = queue.popleft()
        
        # 勝者を次ラウンドへ
        if p1[1] > p2[1]:
            next_round.append(p1)
            loser = p2
        else:
            next_round.append(p2)
            loser = p1
    
    # 決勝だった場合（次ラウンドが1人）
    if len(next_round) == 1:
        print(loser[0])
        break
    
    queue = next_round




N = int(input())
A = list(map(int, input().split()))

mid = len(A) // 2

left_max = max(A[:mid])
right_max = max(A[mid:])

if left_max > right_max:
    # 右が準優勝
    print(A.index(right_max) + 1)
else:
    # 左が準優勝
    print(A.index(left_max) + 1)
