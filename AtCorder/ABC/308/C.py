"""
AtCorder.ABC.308.C の Docstring
問題文
1 から N の番号が付いた N 人がコイントスを何回かしました。人 i は A 
i
​	
  回表を出し、B 
i
​	
  回裏を出したこと分かっています。

人 i のコイントスの 成功率 は  
A 
i
​	
 +B 
i
​	
 
A 
i
​	
 
​	
  で定義されます。人 1,…,N の番号を、成功率の高い順に並び替えてください。成功率が同じ人が複数いる場合、その中では人の番号が小さい順になるように並び替えてください。

制約
2≤N≤2×10 
5
 
0≤A 
i
​	
 ,B 
i
​	
 ≤10 
9
 
A 
i
​	
 +B 
i
​	
 ≥1
入力される数値は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N
A 
1
​	
  B 
1
​	
 
⋮
A 
N
​	
  B 
N
​	
 
出力
人 1,…,N の番号を成功率の高い順に空白区切りで出力せよ。成功率が同じ人の番号は昇順に並び替えて出力せよ。

入力例 1
Copy
3
1 3
3 1
2 2
出力例 1
Copy
2 3 1
人 1 の成功率は 0.25、人 2 の成功率は 0.75、人 3 の成功率は 0.5 です。

成功率の高い順に並び替えると出力例の順番になります。

入力例 2
Copy
2
1 3
2 6
出力例 2
Copy
1 2
人 1,2 は成功率が同じなので、番号の昇順に出力することに注意してください。

入力例 3
Copy
4
999999999 1000000000
333333333 999999999
1000000000 999999997
999999998 1000000000
出力例 3
Copy
3 1 4 2
"""
from functools import cmp_to_key
N = int(input())
people  = []
for i in range(1,N+1):
    A,B = map(int,input().split())
    people.append((i, A, B))

def cmp(p,q):
    i,A,B = p
    j,C,D = q 
    #A/(A+B)とC/(C+D)を割り算せずに比較
    left = A*(C+D)
    right = C*(A+B)
    if left != right:
        return -1 if left > right else 1 #成功率が高い方を前に
    return i - j 
people.sort(key = cmp_to_key(cmp))

print(*[p[0] for p in people])