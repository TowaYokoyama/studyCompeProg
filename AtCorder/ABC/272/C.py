"""
AtCorder.ABC.272.C の Docstring
長さ N の非負整数列 A=(A 
1
​	
 ,A 
2
​	
 ,…,A 
N
​	
 ) が与えられます。

A の異なる 2 要素の和として表せる値の中に偶数が存在するか判定し、存在する場合その最大値を求めてください。

制約
2≤N≤2×10 
5
 
0≤A 
i
​	
 ≤10 
9
 
A の要素は相異なる
入力は全て整数
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
A の異なる 2 要素の和として表せる値の中に偶数が存在しない場合、-1 を出力せよ。

偶数が存在する場合、その最大値を出力せよ。

入力例 1
Copy
3
2 3 4
出力例 1
Copy
6
A の異なる 2 要素の和として表せる値は 5,6,7 です。この中に偶数は存在し、その最大値は 6 です。

入力例 2
Copy
2
1 0
出力例 2
Copy
-1
A の異なる 2 要素の和として表せる値は 1 です。この中に偶数は存在しないので、 -1 を出力してください。
"""
N = int(input())
A = list(map(int,input().split()))
even = []
odd = []
for x in A:
    if x %2 == 0:
        even.append(x)
    else:
        odd.append(x)
even.sort(reverse=True)
odd.sort(reverse=True)

ans = -1
if len(even) >= 2:
    ans = max(ans,even[0]+even[1])
if len(odd) >=2:
    ans = max(ans,odd[0]+odd[1])
        
print(ans)