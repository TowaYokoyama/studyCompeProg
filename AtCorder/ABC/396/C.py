"""
AtCorder.ABC.396.C の Docstring
N 個の黒色のボールと M 個の白色のボールがあります。
ボールにはそれぞれ価値がつけられており、i (1≤i≤N) 個目の黒色のボールの価値は B 
i
​	
 、j (1≤j≤M) 個目の白色のボールの価値は W 
j
​	
  です。

黒色のボールの個数が白色のボールの個数以上になるようにボールを 0 個以上選ぶとき、選んだボールの価値の総和としてありうる最大値を求めてください。

制約
1≤N,M≤2×10 
5
 
−10 
9
 ≤B 
i
​	
 ,W 
j
​	
 ≤10 
9
 
入力は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N M
B 
1
​	
  B 
2
​	
  … B 
N
​	
 
W 
1
​	
  W 
2
​	
  … W 
M
​	
 
出力
答えを出力せよ。

入力例 1
Copy
4 3
8 5 -1 3
3 -2 -4
出力例 1
Copy
19
1,2,4 個目の黒色のボールと 1 個目の白色のボールを選ぶとき、選んだボールの価値の総和は 8+5+3+3=19 となりこれが最大です。

入力例 2
Copy
4 3
5 -10 -2 -5
8 1 4
出力例 2
Copy
15
1,3 個目の黒色のボールと 1,3 個目の白色のボールを選ぶとき、選んだボールの価値の総和は 5+(−2)+8+4=15 となりこれが最大です。

入力例 3
Copy
3 5
-36 -33 -31
12 12 28 24 27
出力例 3
Copy
0
ボールを 1 つも選ばないことも可能です。
"""
N, M = map(int, input().split())
B = list(map(int, input().split()))
W = list(map(int, input().split()))

B.sort(reverse=True)
W.sort(reverse=True)

B_prefix = [0]*(N+1)
for i in range(N):
    B_prefix[i+1] = B_prefix[i] + B[i]

W_prefix = [0]*(M+1)
for i in range(M):
    W_prefix[i+1] = W_prefix[i] + W[i]

# 白のprefix最大値
W_best = [0]*(M+1)
for i in range(M+1):
    if i == 0:
        W_best[i] = 0
    else:
        W_best[i] = max(W_best[i-1], W_prefix[i])

ans = 0
#黒の個数分白は制限される！
for k in range(N+1):
    black_sum = B_prefix[k]#「黒を上からk個取った合計」
    max_white = min(k, M)#白は最大Kまでに制限
    ans = max(ans, black_sum + W_best[max_white])#黒k個 + 白最大k個までの最良の選び方

print(ans)
