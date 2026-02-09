from collections import defaultdict

N ,M = map(int,input().split())#N個数と最低単位数
#必要な最小労力の出力 otherwise -1

INF = 10**18


#dp[d] =単位数における労力 
dp = [INF] * (M+1)
dp[0] = 0

#bが同じなら取れない <=>コマかぶり
groups = defaultdict(list)
for a,b,c in range(N):
    a, b, c = map(int, input().split())
    groups[b].append((a,c))

for group in groups.values():
    new_dp = dp[:] #同じ時間で２回取らないためコピー
    
    for a,c in group:
        for d in range(M+1):
            if dp[d] == INF:
                continue
            nd = min(M,d+c) #単位数がMを超えたならそれを吸着
            
            new_dp[nd] = min(new_dp[nd] , dp[d]+a)
    
    dp = new_dp 
    
ans = dp[M]

print(ans if ans != INF else -1)
    