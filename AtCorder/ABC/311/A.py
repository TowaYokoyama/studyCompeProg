N = int(input())
S = input()
a_cnt = 0
b_cnt = 0
c_cnt = 0

for x in range(N):
    if S[x] == 'A':
        a_cnt+=1
        if a_cnt >= 1 and b_cnt >= 1 and c_cnt >=1:
            print(x+1)
            exit()
    elif S[x] == 'B':
        b_cnt +=1
        if a_cnt >= 1 and b_cnt >= 1 and c_cnt >=1:
                print(x+1)
                exit()
    else:
        c_cnt+=1
        if a_cnt >= 1 and b_cnt >= 1 and c_cnt >=1:
            print(x+1)
            exit()
            
