X,Y,N = map(int,input().split())
pera = X #1個あたりのえん
perb = Y //3#1個あたりの円

cost = 0
if pera > perb:#bの方が安いなら
        mod = N % 3
        syou = N//3
        if mod:
            cost = mod*pera + syou*Y
            
        else:
            cost = syou * Y
        
else:
    cost = N * pera 
    
print(cost)