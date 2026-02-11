N,K = map(int,input().split())
cnt = 0
for _ in range(N):
    A,B = map(int,input().split())
    if K <= A*B:
        cnt+=1
print(cnt) 