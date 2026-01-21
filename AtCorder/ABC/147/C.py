"""
AtCorder.ABC.147.C の Docstring
 から N までの番号がついた N 人の人がいます。彼らはみな、必ず正しい証言を行う「正直者」か、真偽不明の証言を行う「不親切な人」のいずれかです。

人 i は A 
i
​	
  個の証言を行っています。人 i の j 個目の証言は 2 つの整数 x 
ij
​	
  , y 
ij
​	
  で表され、y 
ij
​	
 =1 のときは「人 x 
ij
​	
  は正直者である」という証言であり、y 
ij
​	
 =0 のときは「人 x 
ij
​	
  は不親切な人である」という証言です。

この N 人の中には最大で何人の正直者が存在し得るでしょうか？

制約
入力は全て整数
1≤N≤15
0≤A 
i
​	
 ≤N−1
1≤x 
ij
​	
 ≤N
x 
ij
​	
 

=i
x 
ij 
1
​	
 
​	
 

=x 
ij 
2
​	
 
​	
 (j 
1
​	
 

=j 
2
​	
 )
y 
ij
​	
 =0,1
入力
入力は以下の形式で標準入力から与えられる。

N
A 
1
​	
 
x 
11
​	
  y 
11
​	
 
x 
12
​	
  y 
12
​	
 
:
x 
1A 
1
​	
 
​	
  y 
1A 
1
​	
 
​	
 
A 
2
​	
 
x 
21
​	
  y 
21
​	
 
x 
22
​	
  y 
22
​	
 
:
x 
2A 
2
​	
 
​	
  y 
2A 
2
​	
 
​	
 
:
A 
N
​	
 
x 
N1
​	
  y 
N1
​	
 
x 
N2
​	
  y 
N2
​	
 
:
x 
NA 
N
​	
 
​	
  y 
NA 
N
​	
 
​	
 
出力
存在し得る正直者の最大人数を出力せよ。

入力例 1
Copy
3
1
2 1
1
1 1
1
2 0
出力例 1
Copy
2
人 1 と人 2 が正直者であり、人 3 が不親切な人であると仮定すると、正直者は 2 人であり、矛盾が生じません。これが存在し得る正直者の最大人数です。

入力例 2
Copy
3
2
2 1
3 0
2
3 1
1 0
2
1 1
2 0
出力例 2
Copy
0
1 人でも正直者が存在すると仮定すると、直ちに矛盾します。

入力例 3
Copy
2
1
2 0
1
1 0
出力例 3
Copy
1
"""
N = int(input())
testsimony = []
for _ in range(N):
    A = int(input())
    lst = []
    for _ in range(A):
        x,y = map(int,input().split())
        lst.append((x-1,y)) #0~indexedに戻す
    testsimony.append(lst)
    
ans = 0

#bit全探索
for mask in range(1<<N):
    ok = True 
    
    #人１が正直ものだと仮定しているのか？
    for i in range(N):
        if not ((mask >> i) &1):
            continue #嘘つきの証言は無視
        #正直ものiの証言は全て本当ではない
        for x,y in testsimony[i]:
            if ((mask>>x)&1) != y:
                ok = False 
                break 
        if not ok:
            break 
    if ok:
        ans = max(ans,bin(mask).count("1"))
print(ans)