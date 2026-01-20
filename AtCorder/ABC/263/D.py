# 入力の受け取り
N,L,R=map(int,input().split())
A=list(map(int,input().split()))

# fの計算
# A[0]を埋める
A1=[0]+A
# fを作る(f(0)=0)
f=[0]*(N+1)

# i=1~N
for i in range(1,N+1):
    # fの計算
    f[i]=min(f[i-1]+A1[i],L*i)

# Aをひっくり返す
A=A[::-1]
# A[0]を埋める
A2=[0]+A

# gを作る(g(0)=0)
g=[0]*(N+1)

# i=1~N
for i in range(1,N+1):
    # fの計算
    g[i]=min(g[i-1]+A2[i],R*i)

# 答え
ans=10**15
# i=0~N
for i in range(N+1):
    # これまでの答えとf[i]+g[N-i]の小さい方で更新
    ans=min(ans,f[i]+g[N-i])

# 答えの出力
print(ans)
