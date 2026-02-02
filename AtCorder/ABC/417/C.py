"""
AtCorder.ABC.417.C の Docstring
長さ N の整数列 A=(A 
1
​	
 ,A 
2
​	
 ,…,A 
N
​	
 ) が与えられます。

整数の 2 つ組 (i,j) (1≤i<j≤N) のうち、j−i=A 
i
​	
 +A 
j
​	
  を満たすものがいくつあるか求めてください。

制約
1≤N≤2×10 
5
 
1≤A 
i
​	
 ≤2×10 
5
  (1≤i≤N)
入力はすべて整数
入力
入力は以下の形式で標準入力から与えられる。

N
A 
1
​	
  A 
2
​	
  … A 
N
​	
 
出力
答えを出力せよ。

入力例 1
Copy
9
3 1 4 1 5 9 2 6 5
出力例 1
Copy
3
例えば、(i,j)=(4,7) とすると、j−i=7−4=3 かつ A 
i
​	
 +A 
j
​	
 =1+2=3 が成り立つので、j−i=A 
i
​	
 +A 
j
​	
  です。

一方で、(i,j)=(3,8) とすると、j−i=8−3=5 かつ A 
i
​	
 +A 
j
​	
 =4+6=10 となるので、j−i

=A 
i
​	
 +A 
j
​	
  です。

(i,j)=(1,9),(2,4),(4,7) の 3 組だけが条件を満たすので、3 を出力してください。

入力例 2
Copy
3
123456 123456 123456
出力例 2
Copy
0
条件を満たす組が存在しない場合もあります。

入力例 3
Copy
30
8 3 6 4 9 6 5 6 5 6 3 4 7 3 7 4 9 8 5 8 3 6 8 8 4 5 5 5 6 5
出力例 3
Copy
17
"""


"""
j−i=Ai​+Aj​(i<j)を式変形
j − Aj = i + Ai​
"""
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

cnt = defaultdict(int)
ans = 0

# j を後ろから
for j in range(N-1, -1, -1):
    key_j = j + 1 - A[j]        # j - A[j]（1-index）
    ans += cnt[j + 1 + A[j]]   # i + A[i] と一致するもの
    cnt[key_j] += 1

print(ans)
