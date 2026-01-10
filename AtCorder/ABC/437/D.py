"""
AtCorder.ABC.437.D の Docstring
配点 : 400 点

問題文
長さ N の正整数列 A=(A 
1
​	
 ,A 
2
​	
 ,…,A 
N
​	
 ) および長さ M の正整数列 B=(B 
1
​	
 ,B 
2
​	
 ,…,B 
M
​	
 ) が与えられます。

i=1
∑
N
​	
  
j=1
∑
M
​	
 ∣A 
i
​	
 −B 
j
​	
 ∣ の値を 998244353 で割ったあまりを求めてください。

制約
1≤N,M≤3×10 
5
 
1≤A 
i
​	
 ,B 
j
​	
 <998244353
入力される値はすべて整数
入力
入力は以下の形式で標準入力から与えられる。

N M
A 
1
​	
  A 
2
​	
  ⋯ A 
N
​	
 
B 
1
​	
  B 
2
​	
  ⋯ B 
M
​	
 
出力
答えを 1 行に出力せよ。

入力例 1
Copy
4 2
1 6 9 2
3 1
出力例 1
Copy
26
答えは ∣1−3∣+∣1−1∣+∣6−3∣+∣6−1∣+∣9−3∣+∣9−1∣+∣2−3∣+∣2−1∣=2+0+3+5+6+8+1+1=26 です。

入力例 2
Copy
8 8
185991676 311812083 311812083 84357963 185991676 185991676 724020528 369175631
455049197 387671868 4361724 724020528 724020528 455049197 455049197 724020528
出力例 2
Copy
529117255
"""
import bisect

MOD = 998244353

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# ① B をソート
B.sort()

# ② B の累積和を作る
prefix = [0] * (M + 1)
for i in range(M):
    prefix[i + 1] = prefix[i] + B[i]

ans = 0

# ③ 各 A_i について処理
for a in A:
    # B の中で a 未満の個数
    k = bisect.bisect_left(B, a)

    # B_j < a の部分
    left = a * k - prefix[k]

    # B_j >= a の部分
    right = (prefix[M] - prefix[k]) - a * (M - k)
    
    ans = (ans + left + right) % MOD

print(ans)
