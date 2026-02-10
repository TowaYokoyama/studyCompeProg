"""
AtCorder.awc.0001.E の Docstring
高橋君は気象データの分析をしています。ある地域で N 日間連続して気温を観測した記録があり、 i 日目の気温は H 
i
​	
  度でした。

高橋君は、この観測データから連続する K 日間を選び、その期間の気温の変動幅を調べたいと考えています。

ここで、連続する K 日間の「気温の変動幅」とは、その期間における最高気温と最低気温の差として定義されます。

高橋君は、気温の変動幅が最大となるような連続する K 日間を見つけたいと考えています。気温の変動幅の最大値を求めてください。

制約
1≤K≤N≤2×10 
5
 
−10 
9
 ≤H 
i
​	
 ≤10 
9
 
入力はすべて整数
入力
Copy
N K
H 
1
​	
  H 
2
​	
  … H 
N
​	
 
1 行目には、観測日数を表す N と、選ぶ連続した日数を表す K が、スペース区切りで与えられる。
2 行目には、各日の気温を表す H 
1
​	
 ,H 
2
​	
 ,…,H 
N
​	
  が、スペース区切りで与えられる。
出力
気温の変動幅の最大値を 1 行で出力してください。

入力例 1
Copy
5 3
2 5 1 8 4
出力例 1
Copy
7
入力例 2
Copy
7 4
-3 10 5 -2 8 1 6
出力例 2
Copy
13
入力例 3
Copy
12 5
100 -50 200 150 -100 300 50 -200 250 0 -150 400
出力例 3
Copy
600

"""
from collections import deque
#1つの要素が追加され、1つの要素が削除されるだけ
N,K = map(int,input().split())
H = list(map(int,input().split()))

#スライディングウィンドウで最大値と最小値を効率的に管理する
#単調キューを使用
max_deque = deque() #最大値を管理
min_deque = deque() #最小値を管理

max_variation = 0

for i in range(N):
    #新しい要素を追加
    #max_deque:後ろから、現在の要素よりも小さいものを削除
    while max_deque and H[max_deque[-1]] <= H[i]:
        max_deque.pop()
    max_deque.append(i)
    
    #min_deque:後ろから、現在の要素よりも大きいものを削除
    while min_deque and H[min_deque[-1]] >= H[i]:
        min_deque.pop()
    min_deque.append(i)
    
    #ウィンドウサイズがKとして完成したなら
    if i >= K-1:
        #ウィンドウ外の要素を前から削除
        while max_deque[0] < i-K+1:
            max_deque.popleft()
        while min_deque[0] <i-K+1:
            min_deque.popleft()
        
        #現在のウィンドウの変動幅を計算
        current_max = H[max_deque[0]]
        current_min = H[min_deque[0]]
        
        variation = current_max - current_min
        
        max_variation = max(max_variation, variation)

print(max_variation)