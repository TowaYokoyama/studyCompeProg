#フェニック木
class BIT:
    def __init__(self,n):
        self.n = n
        self.bit = [0]*(n+1)
    
    def add(self,i,x):
        while i<=self.n:
            self.bit[i] +=x
            i+=i&-i 
    def sum(self,i):
        s = 0 
        while i>0:
            s+=self.bit[i]
            i-=i&-i 
        return s 
    
n,q = map(int,input().split())
A = list(map(int,input().split()))

bit = BIT(n)
for i,v in enumerate(A,start=1):
    bit.add(i,v)
for _ in range(q):
    t,*rest = input().split()
    if t == '1':
        x = int(rest[0])
        #swapA[x],A[x+1]
        A[x-1],A[x] = A[x],A[x-1]
        bit.add(x,A[x-1]-A[x])
        bit.add(x+1,A[x]-A[x-1])
    else:
        l,r = map(int,rest)
        print(bit.sum(r)-bit.sum(l-1))