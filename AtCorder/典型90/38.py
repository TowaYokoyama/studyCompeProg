import math
A,B = map(int,input().split())
THRESHOLD = 10 ** 18 
C = A // math.gcd(A,B)
if B <= THRESHOLD // C :
    print(C*B)
else:
    print("Large")