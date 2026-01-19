N = int(input())
S = []
for _ in range(N):
    k = input()
    S.append(k)
X,Y = input().split()
x = int(X)

if  Y == S[x-1]:
    print("Yes")
else:
    print("No") 