"""
AtCorder.ADT.all1800~216.E の Docstring
N 棟のビルが等間隔に一列に並んでいます。手前から i 番目のビルの高さは H 
i
​	
  です。

あなたは次の条件をともに満たすようにいくつかのビルを選んで電飾で飾ろうとしています。

選んだビルたちは高さが等しい
選んだビルたちは等間隔に並んでいる
最大でいくつのビルを選ぶことができますか？　なお、ちょうど 1 つのビルを選んだときは条件を満たすとみなします。

制約
1≤N≤3000
1≤H 
i
​	
 ≤3000
入力は全て整数である
入力
入力は以下の形式で標準入力から与えられる。

N
H 
1
​	
  … H 
N
​	
 
出力
答えを出力せよ。

入力例 1
Copy
8
5 7 5 7 7 5 7 7
出力例 1
Copy
3
手前から 2,5,8 番目のビルを選ぶと条件を満たします。

入力例 2
Copy
10
100 200 300 400 500 600 700 800 900 1000
出力例 2
Copy
1
1つのビルを選んだときは条件を満たすとみなします。

入力例 3
Copy
32
3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6 4 3 3 8 3 2 7 9 5
出力例 3
Copy
3
"""
N = int(input())
H = list(map(int,input().split()))
from collections import defaultdict

N = int(input())
H = list(map(int, input().split()))

# 高さごとに「出現位置」をまとめる
pos = defaultdict(list)
for i, h in enumerate(H):
    pos[h].append(i)

ans = 1  # 1個選ぶのは常にOK

for indices in pos.values():
    m = len(indices)
    if m <= 1:
        continue
    
    # 2点を始点にして差を決める
    for i in range(m):
        for j in range(i + 1, m):
            d = indices[j] - indices[i]   # 間隔
            count = 2
            next_pos = indices[j] + d

            # 同じ間隔で続くか確認
            while next_pos in indices:
                count += 1
                next_pos += d

            ans = max(ans, count)

print(ans)
