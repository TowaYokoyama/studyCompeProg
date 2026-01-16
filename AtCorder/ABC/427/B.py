"""
AtCorder.ABC.427.B の Docstring
問題文
正整数 x に対して、f(x) を x の十進表記における各桁の和として定義します。例えば、f(123)=1+2+3=6 です。

無限数列 A=(A 
0
​	
 ,A 
1
​	
 ,A 
2
​	
 ,…) を以下の式により定義します。

A 
0
​	
 =1
i≥1 のとき A 
i
​	
 = 
j=0
∑
i−1
​	
 f(A 
j
​	
 )
正整数 N が与えられます。A 
N
​	
  の値を求めてください。

制約
N は 1 以上 100 以下の整数
入力
入力は以下の形式で標準入力から与えられる。

N
出力
答えを出力せよ。

入力例 1
Copy
6
出力例 1
Copy
23
A 
0
​	
 =1
A 
1
​	
 =f(A 
0
​	
 )=1
A 
2
​	
 =f(A 
0
​	
 )+f(A 
1
​	
 )=2
A 
3
​	
 =f(A 
0
​	
 )+f(A 
1
​	
 )+f(A 
2
​	
 )=4
A 
4
​	
 =f(A 
0
​	
 )+f(A 
1
​	
 )+f(A 
2
​	
 )+f(A 
3
​	
 )=8
A 
5
​	
 =f(A 
0
​	
 )+f(A 
1
​	
 )+f(A 
2
​	
 )+f(A 
3
​	
 )+f(A 
4
​	
 )=16
A 
6
​	
 =f(A 
0
​	
 )+f(A 
1
​	
 )+f(A 
2
​	
 )+f(A 
3
​	
 )+f(A 
4
​	
 )+f(A 
5
​	
 )=23
であるため、A 
6
​	
 =23 です。

入力例 2
Copy
45
出力例 2
Copy
427

"""
N = int(input())

def f(x):
    return sum(map(int,str(x)))

A = [0]* (N+1)
A[0] = 1

for i in range(1,N+1):
    s = 0
    for j in range(i):
        s+= f(A[j])
    A[i] = s
    
print(A[N]) 


#######################################
N = int(input())
def f(x):
    return sum(map(int, str(x)))

A = [0] * (N + 1)
A[0] = 1

sum_f = f(A[0])   # f(A0)

for i in range(1, N + 1):
    A[i] = sum_f
    sum_f += f(A[i])

print(A[N])
