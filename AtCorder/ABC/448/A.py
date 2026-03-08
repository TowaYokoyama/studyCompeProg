N,X = map(int,input().split())
A = list(map(int,input().split()))
for a in A:
    if a <X:
        print(1)
        X = a 
    else:
        print(0)
 