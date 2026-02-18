"""
AtCorder.ADT.218.all1600~.F の Docstring
長さ N の数列 A=(A 
1
​	
 ,…,A 
N
​	
 ) が与えられます。

i=1,…,N のそれぞれについて次の問題を解いてください。

問題：A の要素のうち A 
i
​	
  より大きな要素全ての和を求めよ。

制約
1≤N≤2×10 
5
 
1≤A 
i
​	
 ≤10 
6
 
入力は全て整数である
入力
入力は以下の形式で標準入力から与えられる。

N
A 
1
​	
  … A 
N
​	
 
出力
各 1≤k≤N について、i=k に対する問題の答えを B 
k
​	
  とする。B 
1
​	
 ,…,B 
N
​	
  をこの順に空白区切りで出力せよ。

入力例 1
Copy
5
1 4 1 4 2
出力例 1
Copy
10 0 10 0 8
i=1 のとき A 
1
​	
 =1 より大きな要素の和は 4+4+2=10
i=2 のとき A 
2
​	
 =4 より大きな要素の和は 0
i=3 のとき A 
3
​	
 =1 より大きな要素の和は 4+4+2=10
i=4 のとき A 
4
​	
 =4 より大きな要素の和は 0
i=5 のとき A 
5
​	
 =2 より大きな要素の和は 4+4=8
入力例 2
Copy
10
31 42 59 26 53 58 97 93 23 54
出力例 2
Copy
456 414 190 487 361 249 0 97 513 307
入力例 3
Copy
50
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
出力例 3
Copy
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
"""
N = int(input())
A = list(map(int, input().split()))

s = sorted(A)

# 右から累積和
suffix = [0] * (N+1)
for i in range(N-1, -1, -1):
    suffix[i] = suffix[i+1] + s[i]

# 値ごとに「より大きい値の合計」を記録
value_to_sum = {}
for i in range(N):
    if s[i] not in value_to_sum:
        # s[i] より大きいのは i+1 以降
        value_to_sum[s[i]] = suffix[i+1]

# 元の順で出力
ans = [value_to_sum[a] for a in A]
print(*ans)

import bisect

N = int(input())
A = list(map(int,input().split()))

s = sorted(A)

prefix = [0] * (N+1)
for i in range(N):
    prefix[i+1] = prefix[i] + s[i]

ans = []

for a in A:
    pos = bisect.bisect_right(s, a)
    total = prefix[N] - prefix[pos]
    ans.append(total)

print(*ans)
