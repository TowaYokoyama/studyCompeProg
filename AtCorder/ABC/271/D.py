import itertools
N=int(input())
A=[int(a) for a in input().split()]
AA=set(A)
X=[0 for _ in range(N+2)]
for a in AA:
    if a<=N:
        X[a+1]+=1

# 累積和で、その巻の前に何巻あるか管理する
X=list(itertools.accumulate(X))

ok=0
ng=N+1
while ng-ok!=1:
    mid=(ok+ng)//2

    # mid巻目まで各巻ごとに1冊だけ残してそれ以外全部売っても、1～mid巻を読めなければ mid巻は読めない
    if (N-X[mid+1])//2+X[mid+1]<mid:
        ng=mid
    else:
        ok=mid

print(ok)
