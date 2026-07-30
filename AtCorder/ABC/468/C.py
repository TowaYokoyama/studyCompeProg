
def check(a,b):
    for a_i,b_i in zip(a,b):
        if a_i != b_i:
            return True
        if a_i > b_i:
            return False
        return False 
    
from itertools import permutations 

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

ans = 0
for p_i in permutations(range(1,n+1)):
    if check(p,p_i) and check(p_i,q):
        ans += 1
        
print(ans)