"""
高橋君は庭に N 個の花の種を植えようとしています。

日付は第 1 日目、第 2 日目、…と続きます。高橋君は第 1 日目から順に各日について、種を植えられるかどうかを判断していきます。

天気予報によると M 回の雨の期間が予定されており、i 番目の雨の期間は第 L 
i
​	
  日から第 R 
i
​	
  日まで（両端を含む）続きます。ある日が M 回の雨の期間のうち少なくとも 1 つに含まれている場合、その日は雨の日です。雨の日は地面がぬかるんで作業ができないため、種を植えることができません。雨の日でない日には、種をちょうど 1 個植えます。

なお、雨の期間同士が重なったり一方が他方に含まれたりすることもあります。その場合も、いずれかの雨の期間に含まれる日はすべて雨の日として扱います。

雨の期間は有限であるため、最後の雨の期間が終わった後にはすべての日が晴れとなり、十分な日数が経てば必ずすべての種を植え終えることができます。

N 個すべての種を植え終えるのは第何日目になるかを求めてください。

制約
1≤N≤10 
9
 
0≤M≤10 
5
 
1≤L 
i
​	
 ≤R 
i
​	
 ≤10 
18
 
雨の期間はソートされているとは限らない
入力はすべて整数である
入力
Copy
N M
L 
1
​	
  R 
1
​	
 
L 
2
​	
  R 
2
​	
 
⋮
L 
M
​	
  R 
M
​	
 
1 行目には、植える種の数を表す整数 N と、雨の期間の数を表す整数 M が、スペース区切りで与えられる。
2 行目から M 行にわたって、各雨の期間の情報が与えられる。1+i 行目には、i 番目の雨の期間の開始日 L 
i
​	
  と終了日 R 
i
​	
  が、スペース区切りで与えられる。これは、第 L 
i
​	
  日から第 R 
i
​	
  日まで（両端を含む）雨が降ることを意味する。
出力
N 個すべての種を植え終える日の番号を 1 行で出力せよ。

入力例 1
Copy
5 2
2 4
7 7
出力例 1
Copy
9
入力例 2
Copy
10 3
3 8
5 12
20 25
出力例 2
Copy
26
入力例 3
Copy
1000000000 3
1 500000000
500000000001 999999999999
1000000000002 1000000000002
出力例 3
Copy
1500000000
"""
import bisect
N, M = map(int, input().split())
intervals = [tuple(map(int, input().split())) for _ in range(M)]

#左端をソート
intervals.sort()
#マージ
merged = []
for L,R in intervals:
    if not merged or merged[-1][1] < L -1:
        merged.append([L,R])
    else:
        merged[-1][1] = max(merged[-1][1], R)
        
#左端リスト
starts = [L for L,R in merged]

#Xまでの雨日数
def rain_days(X):
    idx = bisect.bisect_right(starts,X)
    total = 0
    for i in range(idx):
        L,R = merged[i]
        total+= min(R,X) - L+1
    return total 

#二分探索
left = 0
right = 2 * 10 ** 18

while left < right:
    mid = (left+right) // 2
    if mid - rain_days(mid) >= N:
        right = mid 
    else:
        left = mid +1

print(left)