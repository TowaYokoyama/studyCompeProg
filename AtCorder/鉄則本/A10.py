"""
AtCorder.鉄則本.A10 の Docstring
問題文
あるリゾートホテルには，1 号室から N 号室までの N 個の部屋があります． i 号室は A 
i
​	
  人部屋です．このホテルでは D 日間にわたって工事が行われることになっており， d 日目は L 
d
​	
  号室から R 
d
​	
  号室までの範囲を使うことができません． d=1,2,⋯D について，d 日目に使える中で最も大きい部屋は何人部屋であるか，出力するプログラムを作成してください．

制約
3≤N≤100000
1≤D≤100000
1≤A 
i
​	
 ≤100
2≤L 
i
​	
 ≤R 
i
​	
 ≤N−1
入力はすべて整数
入力
入力は以下の形式で標準入力から与えられます．

N
A 
1
​	
  A 
2
​	
  ⋯ A 
N
​	
 
D
L 
1
​	
  R 
1
​	
 
⋮
L 
D
​	
  R 
D
​	
 
出力
D 行にわたって出力してください．d 行目には，d 日目に使える中で最も大きい部屋は何人部屋であるかを出力してください．

入力例 1
Copy
7
1 2 5 5 2 3 1
2
3 5
4 6
出力例 1
Copy
3
5
"""
N = int(input())
A = list(map(int, input().split()))
D = int(input())

left_max = [0]*(N+1)
for i in range(N):
    left_max[i+1] = max(left_max[i], A[i])

right_max = [0]*(N+2)
for i in range(N-1, -1, -1):
    right_max[i+1] = max(right_max[i+2], A[i])

for _ in range(D):
    L, R = map(int, input().split())
    print(max(left_max[L-1], right_max[R+1]))
