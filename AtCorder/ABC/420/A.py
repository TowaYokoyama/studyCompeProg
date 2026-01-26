X,Y = map(int,input().split())
if X+Y<12:
    print(X+Y)
elif (X+Y)%12 == 0:
    print(12)
else:
    print((X+Y)%12)
      