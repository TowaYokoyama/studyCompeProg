X,Y = map(int,input().split())
if X > Y and X - Y <= 3:
    print("Yes")
    exit()
if X < Y and Y - X <=2:
    print("Yes")
else:
    print("No")