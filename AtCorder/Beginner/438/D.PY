"""
AtCorder.Beginner.438.D の Docstring
問題文
すぬけ君は蛇を観察しており、どこからどこまでが頭・胴・尾なのかが気になっています。 すぬけ君は蛇を N 個のブロックに区切り、それぞれのブロックについて頭らしさ・胴らしさ・尾らしさを評価しました。 そして、らしさの合計が最大になる分け方を考えることにしました。
長さ N の整数列 A=(A 
1
​	
 ,A 
2
​	
 ,…,A 
N
​	
 ), B=(B 
1
​	
 ,B 
2
​	
 ,…,B 
N
​	
 ), C=(C 
1
​	
 ,C 
2
​	
 ,…,C 
N
​	
 ) が与えられます。

整数の組 (x,y) が 1≤x<y<N を満たすとき、 
i=1
∑
x
​	
 A 
i
​	
 + 
i=x+1
∑
y
​	
 B 
i
​	
 + 
i=y+1
∑
N
​	
 C 
i
​	
  の値として取り得る最大値を求めてください。

制約
3≤N≤3×10 
5
 
1≤A 
i
​	
 ,B 
i
​	
 ,C 
i
​	
 ≤10 
6
 
入力される値はすべて整数
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
 
C 
1
​	
  C 
2
​	
  … C 
N
​	
 
出力
答えを出力せよ。

入力例 1
Copy
5
1 4 2 4 3
2 3 4 2 2
3 2 4 4 3
出力例 1
Copy
16
(x,y)=(2,3) とすると  
i=1
∑
x
​	
 A 
i
​	
 + 
i=x+1
∑
y
​	
 B 
i
​	
 + 
i=y+1
∑
N
​	
 C 
i
​	
 =1+4+4+4+3=16 となります。

入力例 2
Copy
3
1 1 1
1 1 1
1 1 1
出力例 2
Copy
3
入力例 3
Copy
6
2 10 7 7 7 11
5 7 9 10 9 12
6 6 7 10 12 7
出力例 3
Copy
50

"""
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# 累積和
SA = [0] * (N + 1)
SB = [0] * (N + 1)
SC = [0] * (N + 1)

for i in range(N):
    SA[i+1] = SA[i] + A[i]
    SB[i+1] = SB[i] + B[i]
    SC[i+1] = SC[i] + C[i]

ans = -10**30
best = -10**30  # max(SA[x] - SB[x]) for x < y

for y in range(2, N):  # y < N
    # x = y-1 を候補に追加
    best = max(best, SA[y-1] - SB[y-1])

    # 今の y での値
    val = best + (SB[y] - SC[y])
    ans = max(ans, val)

# SC[N] を最後に足す
ans += SC[N]

print(ans)
