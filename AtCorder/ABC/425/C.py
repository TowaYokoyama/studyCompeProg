"""
AtCorder.ABC.425.C の Docstring
題文
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

Q 個のクエリが与えられるので順に処理してください。クエリは 2 種類あり、以下のいずれかの形式で与えられます。

1 c： A の先頭の要素を末尾に移動させる操作を c 回行う。
2 l r：  
i=l
∑
r
​	
 A 
i
​	
  の値を出力する。
制約
1≤N≤2×10 
5
 
1≤Q≤2×10 
5
 
1≤A 
i
​	
 ≤10 
9
 
1≤c≤N
1≤l≤r≤N
2 つ目の形式のクエリが 1 つ以上存在する
入力される値は全て整数
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
 
query 
1
​	
 
query 
2
​	
 
⋮
query 
Q
​	
 
各クエリ query 
i
​	
  は以下の 2 種類のいずれかの形式で与えられる。

1 c
2 l r
出力
問題文の指示に従って 2 つ目の形式のクエリへの答えを改行区切りで出力せよ。

入力例 1
Copy
4 3
3 1 4 5
2 1 3
1 1
2 2 3
出力例 1
Copy
8
9
各クエリは以下のように処理されます。

1 つ目のクエリ： A 
1
​	
 +A 
2
​	
 +A 
3
​	
 =3+1+4=8 なので 8 を出力します。
2 つ目のクエリ： A=(3,1,4,5) が A=(1,4,5,3) に変化します。
3 つ目のクエリ： A 
2
​	
 +A 
3
​	
 =4+5=9 なので 9 を出力します。
入力例 2
Copy
5 7
1 2 4 8 16
2 1 5
1 4
1 5
2 1 5
2 2 4
1 1
2 3 3
出力例 2
Copy
31
31
7
4
"""
N, Q = map(int, input().split())
A = list(map(int, input().split()))

# 累積和
prefix = [0] * (N + 1)
for i in range(N):
    prefix[i+1] = prefix[i] + A[i]

shift = 0  # 今の先頭位置

for _ in range(Q):
    query = input().split()
    
    if query[0] == "1":
        c = int(query[1])
        shift = (shift + c) % N

    else:
        l = int(query[1])
        r = int(query[2])

        L = (shift + l - 1) % N
        R = (shift + r - 1) % N

        if L <= R:
            ans = prefix[R+1] - prefix[L]
        else:
            ans = (prefix[N] - prefix[L]) + prefix[R+1]

        print(ans)
