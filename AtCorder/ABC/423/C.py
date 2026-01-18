"""
AtCorder.ABC.423.C の Docstring
問題文
N+1 個の部屋が一列に並んでおり、順に 0,1,…,N の番号が付けられています。

部屋の間には N 個のドアがあり、1,2,…,N の番号が付けられています。ドア i は部屋 i−1 と部屋 i の間にあります。

各ドアについて鍵の状態を表す値 L 
i
​	
  が与えられ、L 
i
​	
 =0 のときドア i の鍵は開いており、L 
i
​	
 =1 のときドア i の鍵は閉まっています。

高橋君ははじめ部屋 R におり、ドア i の鍵が開いているときに限り、部屋 i−1 と部屋 i の間を移動することができます。また、高橋君は部屋 i−1 または部屋 i にいるときに限り、ドア i の鍵に対して 開閉操作 を行うことができます。ドア i の鍵に対して開閉操作を行ったとき、その鍵が開いているときは閉まり、閉まっているときは開きます。

すべてのドアの鍵が閉まった状態にするために行う鍵の開閉操作の回数として考えられる最小値を求めてください。

制約
2≤N≤2×10 
5
 
0≤R≤N
L 
i
​	
 ∈{0,1}
入力される値はすべて整数
入力
入力は以下の形式で標準入力から与えられる。

N R
L 
1
​	
  L 
2
​	
  … L 
N
​	
 
出力
答えを出力せよ。

入力例 1
Copy
6 3
1 0 0 1 0 0
出力例 1
Copy
6
高橋君は以下のように行動することで 6 回の開閉操作ですべてのドアの鍵が閉まった状態にすることができます。

部屋 2 に移動する。
ドア 2 に対して開閉操作を行い、ドア 2 の鍵を閉める。
部屋 3 に移動する。
ドア 4 に対して開閉操作を行い、ドア 4 の鍵を開ける。
ドア 3 に対して開閉操作を行い、ドア 3 の鍵を閉める。
部屋 4 に移動する。
ドア 4 に対して開閉操作を行い、ドア 4 の鍵を閉める。
部屋 5 に移動する。
ドア 5 に対して開閉操作を行い、ドア 5 の鍵を閉める。
ドア 6 に対して開閉操作を行い、ドア 6 の鍵を閉める。
入力例 2
Copy
2 1
0 0
出力例 2
Copy
2
入力例 3
Copy
8 2
0 1 0 0 1 0 1 1
出力例 3
Copy
8

"""
N, R = map(int, input().split())
L = [0] + list(map(int, input().split()))  # 1-indexed

# 開いているドアの位置を集める
opens = [i for i in range(1, N + 1) if L[i] == 0]

# すでに全部閉まっている
if not opens:
    print(0)
    exit()

a = min(opens)
b = max(opens)

# prefix sums
# open_ps[i] = ドア1..iまでに「開いている」数
# close_ps[i] = ドア1..iまでに「閉まっている」数
open_ps = [0] * (N + 1)
close_ps = [0] * (N + 1)

for i in range(1, N + 1):
    open_ps[i] = open_ps[i - 1]
    close_ps[i] = close_ps[i - 1]
    if L[i] == 0:
        open_ps[i] += 1
    else:
        close_ps[i] += 1

# 区間 (l, r] を通過するコスト
# 開いてる → 1回、閉まってる → 2回
def cost(l, r):
    o = open_ps[r] - open_ps[l]
    c = close_ps[r] - close_ps[l]
    return o * 1 + c * 2

ans = 10**18

# 左 → 右
if R <= a:
    ans = min(ans, cost(R, b))
elif R >= b:
    ans = min(ans, cost(a, R))
else:
    ans = min(ans, cost(R, a) + cost(a, b))
    ans = min(ans, cost(R, b) + cost(a, b))

print(ans)
