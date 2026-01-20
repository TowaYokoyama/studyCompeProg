from collections import Counter
c = list(map(int,input().split()))#c = list(A,B,C,D,E)
d = Counter(c)
threecard = False
twocard = False
for a in d:
    if d[a] ==3:
        threecard = True
    elif d[a] == 2:
        twocard = True 

if threecard == True and twocard == True:
    print("Yes")
else:
    print("No")