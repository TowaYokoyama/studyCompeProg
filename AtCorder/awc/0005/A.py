N,K = map(int,input().split())
P =list(map(int,input().split()))
ans = 0
for x in P:
    if x % K == 0:
        ans+= x 
print(ans) 