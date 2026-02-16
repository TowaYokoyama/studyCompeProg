"""
AtCorder.ADT.all1800~216.C の Docstring
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
A の要素はすべて異なります。B の要素もすべて異なります。

次の 2 つを出力してください。

A にも B にも含まれ、その位置も一致している整数の個数。言い換えると、A 
i
​	
 =B 
i
​	
  を満たす整数 i の個数。
A にも B にも含まれるが、その位置は異なる整数の個数。言い換えると、A 
i
​	
 =B 
j
​	
 ,i

=j を満たす整数の組 (i,j) の個数。
制約
1≤N≤1000
1≤A 
i
​	
 ≤10 
9
 
1≤B 
i
​	
 ≤10 
9
 
A 
1
​	
 ,A 
2
​	
 ,…,A 
N
​	
  はすべて異なる。
B 
1
​	
 ,B 
2
​	
 ,…,B 
N
​	
  はすべて異なる。
入力はすべて整数である。
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
 
B 
1
​	
  B 
2
​	
  … B 
N
​	
 
出力
答えを 2 行出力せよ。1 行目には 1. の個数、2 行目には 2. の個数を出力せよ。

入力例 1
Copy
4
1 3 5 2
2 3 1 4
出力例 1
Copy
1
2
A にも B にも含まれ、その位置も一致している整数は A 
2
​	
 =B 
2
​	
 =3 の 1 個です。
A にも B にも含まれるが、その位置は異なる整数は A 
1
​	
 =B 
3
​	
 =1 と A 
4
​	
 =B 
1
​	
 =2 の 2 個です。

入力例 2
Copy
3
1 2 3
4 5 6
出力例 2
Copy
0
0
1., 2. ともに条件を満たす整数は存在しません。

入力例 3
Copy
7
4 8 1 7 9 5 6
3 5 1 7 8 2 6
出力例 3
Copy
3
2
"""
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
first = 0
second = 0
for i in range(N):
    if A[i] == B[i]:
        first+=1
print(first)

for x in B:
    if x in A:
        second+=1
print(second - first)