N,M = map(int,input().split())#人と缶の数

#禁止なドリンク
ban = set() 
for i in range(1,N+1):
    L = int(input())
    X = list(map(int,input().split()))#その缶ジュース番号先頭順ねuniqueで存在する
    #その人が缶ジュースを飲めるなら
     
    for x in X:
        if x not in ban:
            print(x)
            ban.add(x)
            break
    
    else:print(0)
    