N,M = map(int,input().split())
for i in range(N):
    if i>M-1:
        print("Too Many Requests")
    else:
        print("OK")