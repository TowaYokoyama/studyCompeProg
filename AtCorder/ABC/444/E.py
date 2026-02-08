"""
AtCorder.ABC.444.E の Docstring
長さ N の整数列 (A 
1
​	
 ,…,A 
N
​	
 ) と正整数 D が与えられます。

以下の条件をともに満たす整数の組 (L,R) の個数を求めてください。

1≤L≤R≤N
(A 
L
​	
 ,A 
L+1
​	
 ,…,A 
R
​	
 ) のどの 2 つの要素も差が D 以上である
すなわち、 L≤i<j≤R を満たす全ての整数の組 (i,j) について、 ∣A 
i
​	
 −A 
j
​	
 ∣≥D である
制約
2≤N≤4×10 
5
 
1≤A 
i
​	
 ≤10 
9
 
1≤D≤10 
9
 
入力
入力は以下の形式で標準入力から与えられる。

N D
A 
1
​	
  … A 
N
​	
 
出力
答えを出力せよ。

入力例 1
Copy
5 3
3 1 4 1 5
出力例 1
Copy
8
(1,1),(2,2),(3,3),(4,4),(5,5),(2,3),(3,4),(4,5) の 8 組が条件を満たします。

入力例 2
Copy
9 1
1 2 3 4 5 6 7 8 9
出力例 2
Copy
45
入力例 3
Copy
6 1000000000
123456789 234567891 987654321 321987654 1000000000 1
出力例 3
Copy
6
"""
from sortedcontainers import SortedList

n, d = map(int, input().split())
a = list(map(int, input().split()))

s = SortedList([])
ans = 0
right = 0
for left in range(n):
    while right < n:
        ind = s.bisect_left(a[right])
        if ind - 1 >= 0 and abs(a[right] - s[ind - 1]) < d:
            break
        if ind < len(s) and abs(a[right] - s[ind]) < d:
            break
        s.add(a[right])
        right += 1
    ans += right - left

    s.discard(a[left])

print(ans)
