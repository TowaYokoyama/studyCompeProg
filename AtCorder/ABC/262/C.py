"""
AtCorder.ABC.262.C の Docstring
1 以上 N 以下の整数からなる長さ N の数列 a=(a 
1
​	
 ,…,a 
N
​	
 ) が与えられます。

以下の条件を全て満たす整数 i,j の組の総数を求めてください。

1≤i<j≤N
min(a 
i
​	
 ,a 
j
​	
 )=i
max(a 
i
​	
 ,a 
j
​	
 )=j
制約
2≤N≤5×10 
5
 
1≤a 
i
​	
 ≤N(1≤i≤N)
入力は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N
a 
1
​	
  … a 
N
​	
 
出力
答えを出力せよ。

入力例 1
Copy
4
1 3 2 4
出力例 1
Copy
2
(i,j)=(1,4),(2,3) が条件を満たします。

入力例 2
Copy
10
5 8 2 2 1 6 7 2 9 10
出力例 2
Copy
8

"""
N = int(input())
A = list(map(int,input().split()))

#固定点の考えかた 
fixed = 0
for i in range(N):
    if A[i] == i+1:
        fixed +=1 

#2-cycleの数
swap = 0 
for i in range(N):
    j = A[i] -1
    if j >i and A[j] == i+1:
        swap +=1 

#組み合わせ
ans = fixed * (fixed -1) //2 +swap 
print(ans)

N = int(input())
a = list(map(int,input().split()))

ans = 0
cnt = 0
for i in range(N):
    if a[i] == i+1:
        cnt += 1
    
    elif a[i]>i+1 and a[a[i]-1] == i+1:
        ans += 1

ans += (cnt-1)*cnt//2
print(ans)