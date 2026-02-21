K,M = map(int,input().split())
L = list(map(int,input().split()))
S = sum(L)
points = S%M
print(points)