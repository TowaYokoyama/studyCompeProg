N,K = map(int,input().split())
A = list(map(int,input().split()))
for _ in range(K):
    A.remove(A[0])
    A.append(0)
print(*A)