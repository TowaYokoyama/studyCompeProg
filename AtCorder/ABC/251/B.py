"""
AtCorder.ABC.251.B の Docstring
B - At Most 3 (Judge ver.)   / 
実行時間制限: 2 sec / メモリ制限: 1024 MiB

配点 : 200 点

問題文
おもり 1, おもり 2, …, おもり N の N 個のおもりがあります。おもり i の重さは A 
i
​	
  です。
以下の条件を満たす正整数 n を 良い整数 と呼びます。

3 個以下 の異なるおもりを自由に選んで、選んだおもりの重さの和を n にすることができる。
W 以下の正整数のうち、良い整数は何個ありますか？

制約
1≤N≤300
1≤W≤10 
6
 
1≤A 
i
​	
 ≤10 
6
 
入力される値はすべて整数
入力
入力は以下の形式で標準入力から与えられる。

N W
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
2 10
1 3
出力例 1
Copy
3
おもり 1 のみを選ぶと重さの和は 1 になります。よって 1 は良い整数です。
おもり 2 のみを選ぶと重さの和は 3 になります。よって 3 は良い整数です。
おもり 1 とおもり 2 を選ぶと重さの和は 4 になります。よって 4 は良い整数です。
これら以外に良い整数は存在しません。また、1,3,4 のいずれも W 以下の整数です。よって答えは 3 個になります。

入力例 2
Copy
2 1
2 3
出力例 2
Copy
0
W 以下の良い整数は存在しません。

入力例 3
Copy
4 12
3 3 3 3
出力例 3
Copy
3
良い整数は 3,6,9 の 3 個です。
たとえばおもり 1, おもり 2, おもり 3 を選ぶと重さの和は 9 になるので、9 は良い整数です。
12 は良い整数 ではない ことに注意してください。

入力例 4
Copy
7 251
202 20 5 1 4 2 100
出力例 4
Copy
48

"""
N,W = map(int,input().split())
A = list(map(int,input().split()))
weight = 0
allowed_w = []


#１個だけ試す
for i in range(N):
  weight = A[i]
  if weight <= W:
    allowed_w.append(weight)

  
#２個だけ試す
for i in range(N):
  for j in range(i+1,N):
    weight_one = A[i]
    weight_two = A[j]
    if weight_one + weight_two <= W:
      allowed_w.append(weight_one + weight_two)
      


#3個だけ
for i in range(N):
  for j in range(i+1,N):
    for k in range(j+1,N):
      weight_one = A[i]
      weight_two = A[j]
      weight_three = A[k]
      if weight_one + weight_two + weight_three <= W:
        allowed_w.append(weight_one + weight_two + weight_three)
        
good = set(allowed_w)
print(len(good))