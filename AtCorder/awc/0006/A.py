N,L,W = map(int,input().split())
D = list(map(int,input().split()))
ans = 0
for x in D:
    if L-W<= x <= L+W:
        ans+=1
print(ans)