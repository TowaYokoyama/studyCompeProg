"""
AtCorder.ABC.261.B の Docstring
N 人の人が総当り戦の試合をしました。

N 行 N 列からなる試合の結果の表 A が与えられます。A の i 行目 j 列目の要素を A 
i,j
​	
  と表します。
A 
i,j
​	
  は i=j のとき - であり、それ以外のとき W, L, D のいずれかです。
A 
i,j
​	
  が W, L, D であることは、人 i が人 j との試合に勝った、負けた、引き分けたことをそれぞれ表します。

与えられた表に矛盾があるかどうかを判定してください。

次のいずれかが成り立つとき、与えられた表には矛盾があるといいます。

ある組 (i,j) が存在して、人 i が人 j に勝ったが、人 j が人 i に負けていない
ある組 (i,j) が存在して、人 i が人 j に負けたが、人 j が人 i に勝っていない
ある組 (i,j) が存在して、人 i が人 j に引き分けたが、人 j が人 i に引き分けていない
制約
2≤N≤1000
A 
i,i
​	
  は - である
i

=j のとき、A 
i,j
​	
  は W, L, D のいずれかである
入力
入力は以下の形式で標準入力から与えられる。

N
A 
1,1
​	
 A 
1,2
​	
 …A 
1,N
​	
 
A 
2,1
​	
 A 
2,2
​	
 …A 
2,N
​	
 
⋮
A 
N,1
​	
 A 
N,2
​	
 …A 
N,N
​	
 
出力
与えられた表に矛盾がないとき correct、矛盾があるとき incorrect と出力せよ。

入力例 1
Copy
4
-WWW
L-DD
LD-W
LDW-
出力例 1
Copy
incorrect
人 3 が人 4 に勝ったにもかかわらず、人 4 も人 3 に勝ったことになっており、矛盾しています。

入力例 2
Copy
2
-D
D-
出力例 2
Copy
correct
矛盾はありません。
"""
N = int(input())
A = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if A[i][j] == '-' or A[i][j] == 'W' and A[j][i] == 'L' or A[i][j] == 'L' and A[j][i] == 'W' or A[i][j] == 'D' and A[j][i] == 'D':
            continue
        else:
            print("incorrect")
            exit()

print("correct")