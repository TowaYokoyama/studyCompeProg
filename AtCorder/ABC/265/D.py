"""
AtCorder.ABC.265.D の Docstring
問題文
長さ N の数列 A=(A 
0
​	
 ,…,A 
N−1
​	
 ) があります。
次の条件を全て満たす整数の組 (x,y,z,w) が存在するか判定してください。

0≤x<y<z<w≤N
A 
x
​	
 +A 
x+1
​	
 +…+A 
y−1
​	
 =P
A 
y
​	
 +A 
y+1
​	
 +…+A 
z−1
​	
 =Q
A 
z
​	
 +A 
z+1
​	
 +…+A 
w−1
​	
 =R
制約
3≤N≤2×10 
5
 
1≤A 
i
​	
 ≤10 
9
 
1≤P,Q,R≤10 
15
 
入力に含まれる値は全て整数である
入力
入力は以下の形式で標準入力から与えられる。

N P Q R
A 
0
​	
  A 
1
​	
  … A 
N−1
​	
 
出力
条件を満たす組が存在するなら Yes、存在しないなら No を出力せよ。

入力例 1
Copy
10 5 7 5
1 3 2 2 2 3 1 4 3 2
出力例 1
Copy
Yes
(x,y,z,w)=(1,3,6,8) が条件を満たします。

入力例 2
Copy
9 100 101 100
31 41 59 26 53 58 97 93 23
出力例 2
Copy
No
入力例 3
Copy
7 1 1 1
1 1 1 1 1 1 1
出力例 3
Copy
Yes
"""
N,P,Q,R = map(int,input().split())
A = list(map(int,input().split()))

S = [0]
for a in A:
    S.append(S[-1] + a)

S_set = set(S)

for x in range(N):
    s = S[x]
    if (s + P in S_set and 
        s + P + Q in S_set and 
        s + P +Q + R in S_set
        ):
        print("Yes")
        exit()
        
        
print("No")