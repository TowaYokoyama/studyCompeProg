"""
AtCorder.ABC.420.C の Docstring
長さ N の整数列 A=(A 
1
​	
 ,A 
2
​	
 ,…,A 
N
​	
 ),B=(B 
1
​	
 ,B 
2
​	
 ,…,B 
N
​	
 ) が与えられます。

Q 個のクエリが与えられるので順に処理してください。 i 番目 (1≤i≤Q) のクエリは以下で説明されます。

文字 c 
i
​	
  と整数 X 
i
​	
 ,V 
i
​	
  が与えられる。 c 
i
​	
 = A ならば A 
X 
i
​	
 
​	
  を、 c 
i
​	
 = B ならば B 
X 
i
​	
 
​	
  を V 
i
​	
  に変更する。その後、 
k=1
∑
N
​	
 min(A 
k
​	
 ,B 
k
​	
 ) を出力する。
制約
1≤N,Q≤2×10 
5
 
1≤A 
i
​	
 ,B 
i
​	
 ≤10 
9
 
c 
i
​	
  は A か B のいずれか
1≤X 
i
​	
 ≤N
1≤V 
i
​	
 ≤10 
9
 
入力される数値は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N Q
A 
1
​	
  A 
2
​	
  … A 
N
​	
 
B 
1
​	
  B 
2
​	
  … B 
N
​	
 
c 
1
​	
  X 
1
​	
  V 
1
​	
 
c 
2
​	
  X 
2
​	
  V 
2
​	
 
⋮
c 
Q
​	
  X 
Q
​	
  V 
Q
​	
 
出力
Q 行出力せよ。 i 行目 (1≤i≤Q) には i 番目のクエリに対する答えを出力せよ。

入力例 1
Copy
4 3
3 1 4 1
2 7 1 8
A 2 3
B 3 3
A 1 7
出力例 1
Copy
7
9
9
1 番目のクエリでは A=(3,3,4,1),B=(2,7,1,8) となります。したがって、1 行目には min(3,2)+min(3,7)+min(4,1)+min(1,8)=7 を出力してください。

2 番目のクエリでは A=(3,3,4,1),B=(2,7,3,8) となります。したがって、 2 行目には min(3,2)+min(3,7)+min(4,3)+min(1,8)=9 を出力してください。

3 番目のクエリでは A=(7,3,4,1),B=(2,7,3,8) となります。したがって、 3 行目には min(7,2)+min(3,7)+min(4,3)+min(1,8)=9 を出力してください。

入力例 2
Copy
1 3
1
1000000000
A 1 1
A 1 1
A 1 1
出力例 2
Copy
1
1
1
入力例 3
Copy
5 3
100 100 100 100 100
100 100 100 100 100
A 4 21
A 2 99
B 4 57
出力例 3
Copy
421
420
420

"""
N,Q = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
# for _ in range(Q):
#   c,x,v = input().split()
#   sum = 0
#   if c == 'A':
#     A[int(x)-1] = int(v)
#     #print(A)
#     for i in range(N):
#       sum+=min(A[i],B[i])
#     print(sum)
  
#   else:
#     if c == 'B':
#       B[int(x)-1] = int(v)
#       for i in range(N):
#         sum+=min(A[i],B[i])
#     print(sum)
total = 0
for i in range(N):
    total += min(A[i], B[i])

for _ in range(Q):
  c,x,v = input().split()
  x = int(x)-1#インデックス対策
  v = int(v)#int型に変換
  # ① 変更前
  old = min(A[x], B[x])

# ② 更新
  if c == 'A':
    A[x] = v
  else:
    B[x] = v
  
  new = min(A[x],B[x])
  total+=new-old
  
  print(total)