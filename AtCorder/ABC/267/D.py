# 入力の受け取り
N,M=map(int,input().split())
A=[0]+list(map(int,input().split()))

# (1)表を作る
dp=[[-10**15]*(N+1) for i in range(M+1)]

# (2)すぐにわかるところを埋める
# x=1~N
for x in range(1,N+1):
    dp[1][x]=A[x]

# (3)表の小さい方から答えにたどり着くまで埋める
# k=2~M
for k in range(2,M+1):
    # (k-1)行目の最大値
    dpMax=dp[k-1][0]
    # x=k~N
    for x in range(k,N+1):
        # (k-1)行目の最大値 dp[k-1][x-1]がそれまでの最大値より大きければ更新
        dpMax=max(dp[k-1][x-1],dpMax)
        # (2≤k,k≤x)dp[i][x]=「「(k-1)行目,(1~(x-1))列の最大値」+k*Ax
        dp[k][x]=dpMax+k*A[x]

# (4)答えを出力する
# M行目の最大値
print(max(dp[M]))
