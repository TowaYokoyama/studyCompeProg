"""
AtCorder.ABC.250.A の Docstring
A - Adjacent Squares   / 
実行時間制限: 2 sec / メモリ制限: 1024 MiB

配点 : 100 点

問題文
縦 H 行、横 W 列のマス目があり、このうち上から i 個目、左から j 個目のマスを (i,j) と呼びます。
このとき、マス (R,C) に辺で隣接するマスの個数を求めてください。

ただし、ある 2 つのマス (a,b),(c,d) が辺で隣接するとは、 ∣a−c∣+∣b−d∣=1 (∣x∣ を x の絶対値とする) であることを言います。

制約
入力は全て整数
1≤R≤H≤10
1≤C≤W≤10
入力
入力は以下の形式で標準入力から与えられる。

H W
R C
出力
答えを整数として出力せよ。

入力例 1
Copy
3 4
2 2
出力例 1
Copy
4
入出力例 1,2,3 に対する説明は、出力例 3 の下にまとめて示します。

入力例 2
Copy
3 4
1 3
出力例 2
Copy
3
入力例 3
Copy
3 4
3 4
出力例 3
Copy
2
H=3,W=4 のとき、マス目は以下のようになります。

入力例 1 について、マス (2,2) に隣接するマスは 4 つです。
入力例 2 について、マス (1,3) に隣接するマスは 3 つです。
入力例 3 について、マス (3,4) に隣接するマスは 2 つです。


入力例 4
Copy
1 10
1 5
出力例 4
Copy
2
入力例 5
Copy
8 1
8 1
出力例 5
Copy
1
入力例 6
Copy
1 1
1 1
出力例 6
Copy
0

"""
H,W = map(int,input().split())
R,C = map(int,input().split()) #与えられる点
ans = 0
for x in range(1,H+1):
  for y in range(1,W+1):
    #結局これであればいい
    """
   (a,b),(c,d). があった時∣a−c∣+∣b−d∣=1.  =>隣接すると言うこと
    """
    adjacent = abs(R-x) + abs(C-y)
    if adjacent == 1:
        ans +=1
  
print(ans)  
    
H, W = map(int, input().split())
R, C = map(int, input().split())

ans = 0
if R > 1:
    ans += 1
if R < H:
    ans += 1
if C > 1:
    ans += 1
if C < W:
    ans += 1

print(ans)
