N,K = map(int,input().split())
A = [0] +list(map(int,input().split()))
for i in range(1,N+1):
    if A[i] == K:
        print(i)
        exit() 
    
print(-1)