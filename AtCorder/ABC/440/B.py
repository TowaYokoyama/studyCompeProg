"""
AtCorder.ABC.440.B の Docstring
1 から N の番号がついた N 頭の馬が競争をしました。

全ての馬は同時にスタートし、 i 番の馬はスタートからゴールまで T 
i
​	
  秒かかりました。

1,2,3 着の馬の番号を求めてください。なお、 T 
i
​	
  は相異なることが保証されます。

制約
3≤N≤32
1≤T 
i
​	
 ≤200
T 
i
​	
  は相異なる
入力は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N
T 
1
​	
  … T 
N
​	
 
出力
1,2,3 着の馬の番号をそれぞれ空白区切りでこの順に出力せよ。

入力例 1
Copy
4
100 110 105 95
出力例 1
Copy
4 1 3
4,1,3,2 番の順にゴールしました。1,2,3 着の番号である 4,1,3 をこの順に空白区切りで出力してください。

入力例 2
Copy
8
72 74 69 70 73 75 71 77
出力例 2
Copy
3 4 7

"""
N = int(input())
T = list(map(int,input().split()))
K = sorted(T)
t1 = K[0]
t2 = K[1]
t3 = K[2]
ans = []
for i in range(N):
  if T[i] == t1:
    ans.append(i+1)
for i in range(N):
  if T[i] == t2:
    ans.append(i+1)
for i in range(N):
  if T[i] == t3:
    ans.append(i+1)
print(*ans)