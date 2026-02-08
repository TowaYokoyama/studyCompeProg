"""
AtCorder.ABC.444.D の Docstring
問題文
i=1,2,…,N に対して、1 を A 
i
​	
  個つなげた整数を B 
i
​	
  と表します。
より厳密には、B 
i
​	
 =∑ 
j=0
A 
i
​	
 −1
​	
 10 
j
  と表します。
∑ 
i=1
N
​	
 B 
i
​	
  を求めてください。

制約
1≤N≤2×10 
5
 
1≤A 
i
​	
 ≤2×10 
5
 
入力される値は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N  
A 
1
​	
  A 
2
​	
  … A 
N
​	
   
出力
答えを 1 行で出力せよ。

入力例 1
Copy
4
3 3 3 3
出力例 1
Copy
444
B 
1
​	
 =B 
2
​	
 =B 
3
​	
 =B 
4
​	
 =111 なので、B 
1
​	
 +B 
2
​	
 +B 
3
​	
 +B 
4
​	
 =444 です。

入力例 2
Copy
3
30 10 20
出力例 2
Copy
111111111122222222223333333333
答えは非常に大きくなる可能性があります。

入力例 3
Copy
10
1 2 3 4 5 6 7 8 9 10
出力例 3
Copy
1234567900
"""
N = int(input())
import math

n = int(input())
a = [int(x) for x in input().split()]
l = max(a) + 1 + int(math.log10(n))
tmp = [0] * l

# リスト内の数字のチェック
for i in a:
    tmp[i] += 1

# 上の桁から下の桁向きに累積和
for i in range(l-1,1,-1):
    tmp[i-1] += tmp[i]

# 下の桁から順に桁上がりを処理
for i in range(1,l):
    if tmp[i] >= 10:
        tmp[i+1] += tmp[i] // 10
        tmp[i] = tmp[i] % 10

# 計算結果を上の桁から順に入れていく
# リスト内の最大桁の位置を取得
ans = ''
i = l-1
while i > 0:
    if tmp[i] == 0:
        i -= 1
    else:
        break

# 最大桁から順に値を取得
for j in range(i,0,-1):
    ans += str(tmp[j])

print(ans)
