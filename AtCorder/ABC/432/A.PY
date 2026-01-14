K = list(map(int,input().split()))
K.sort(reverse=True)
print(K[0]*100+K[1]*10+K[2])
