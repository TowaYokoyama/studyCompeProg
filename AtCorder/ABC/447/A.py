N,M = map(int,input().split())
seats = [False]*N
seats[0] = True
M-=1
for i in range(2,N):
    if M == 0:
        print("Yes")
        exit()
    
    if seats[i-1] == True:
        continue
    else:
        seats[i] = True 
        M-=1

if M <= 0:
    print("Yes")
else:
    print("No")