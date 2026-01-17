"""
AtCorder.ABC.423.B の Docstring
問題文
N+1 個の部屋が一列に並んでおり、順に 0,1,…,N の番号が付けられています。

部屋の間には N 個のドアがあり、1,2,…,N の番号が付けられています。ドア i は部屋 i−1 と部屋 i の間にあります。

各ドアについて鍵の状態を表す値 L 
i
​	
  が与えられ、L 
i
​	
 =0 のときドア i の鍵は開いており、L 
i
​	
 =1 のときドア i の鍵は閉まっています。

2 人の人がおり、1 人は部屋 0 に、もう 1 人は部屋 N にいます。それぞれの人は、ドア i の鍵が開いているときに限り、部屋 i−1 と部屋 i の間を移動することができます。

このとき、2 人のいずれも到達できない部屋の個数を求めてください。

制約
2≤N≤100
L 
i
​	
 ∈{0,1}
入力される値はすべて整数
入力
入力は以下の形式で標準入力から与えられる。

N
L 
1
​	
  L 
2
​	
  … L 
N
​	
 
出力
答えを出力せよ。

入力例 1
Copy
5
0 1 0 0 1
出力例 1
Copy
3
2 人のいずれも到達できない部屋は部屋 2,3,4 の 3 つです。

入力例 2
Copy
3
1 0 1
出力例 2
Copy
2
入力例 3
Copy
8
0 0 1 1 0 1 0 0
出力例 3
Copy
3

"""
N = int(input())#ドアの数
L = list(map(int,input().split()))

room = [False]*(N+1)
l = 0
r = len(room)-1


room[l] = True
room[r] = True 
for i in range(len(L)):
    if L[i] == 1:
        break
    else:
        l +=1
        room[l] = True 
        
for j in range(len(L)-1,-1,-1):
    if L[j] == 1:
        break
    else:
        r -=1
        room[r] = True 
cnt = 0
for k in room:
    if k == False:
        cnt +=1

print(cnt) 