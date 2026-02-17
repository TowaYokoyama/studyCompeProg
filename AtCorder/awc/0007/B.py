"""
AtCorder.awc.0007.B の Docstring
高橋君は大学の研究支援センターで働いています。大学には N 個の研究室があり、それぞれの研究室はいくつかの研究テーマに取り組んでいます。研究室 i（1≤i≤N）は M 
i
​	
  個の研究テーマに取り組んでおり、それらのテーマはそれぞれ英小文字からなる文字列 W 
i,1
​	
 ,W 
i,2
​	
 ,…,W 
i,M 
i
​	
 
​	
  で表されます。なお、同じ研究室内で同じ研究テーマが複数回現れることはありません。

大学では、共同研究を促進するために、「共同研究可能」な研究室のペアを調査することになりました。研究室 i が取り組んでいる研究テーマの集合を S 
i
​	
 ={W 
i,1
​	
 ,W 
i,2
​	
 ,…,W 
i,M 
i
​	
 
​	
 } とします。2つの研究室 i,j（i

=j）が「共同研究可能」であるとは、S 
i
​	
  と S 
j
​	
  に共通して含まれる研究テーマの数が K 個以上であること、すなわち ∣S 
i
​	
 ∩S 
j
​	
 ∣≥K が成り立つことを指します。ここで、2つの研究テーマが同一であるかどうかは、テーマを表す文字列が完全に一致するかどうかで判定します。

高橋君は各研究室が取り組んでいる研究テーマのリストを持っています。これらの情報をもとに、「共同研究可能」な研究室のペアの数を求めてください。ただし、研究室 i と研究室 j のペアと研究室 j と研究室 i のペアは同一のペアとみなし、1≤i<j≤N を満たす (i,j) の組のうち条件を満たすものの個数を答えてください。

制約
2≤N≤500
1≤K≤50
1≤M 
i
​	
 ≤50（1≤i≤N）
W 
i,j
​	
  は英小文字のみからなる長さ 1 以上 20 以下の文字列である（1≤i≤N,1≤j≤M 
i
​	
 ）
同じ研究室内で同じ研究テーマが複数回現れることはない（すなわち、j

=k ならば W 
i,j
​	
 

=W 
i,k
​	
 ）
入力
入力は以下の形式で標準入力から与えられる。

N K
M 
1
​	
 
W 
1,1
​	
  W 
1,2
​	
  … W 
1,M 
1
​	
 
​	
 
M 
2
​	
 
W 
2,1
​	
  W 
2,2
​	
  … W 
2,M 
2
​	
 
​	
 
⋮
M 
N
​	
 
W 
N,1
​	
  W 
N,2
​	
  … W 
N,M 
N
​	
 
​	
 
最初の行には、研究室の数 N と「共同研究可能」の判定に用いる閾値 K が、スペース区切りで与えられる。

続いて、各研究室 i（i=1,2,…,N）について、以下の 2 行が順に与えられる。

第 1 行には、研究室 i が取り組んでいる研究テーマの数 M 
i
​	
  が与えられる。
第 2 行には、研究室 i が取り組んでいる M 
i
​	
  個の研究テーマを表す文字列 W 
i,1
​	
 ,W 
i,2
​	
 ,…,W 
i,M 
i
​	
 
​	
  がスペース区切りで与えられる。
出力
「共同研究可能」な研究室のペアの数を 1 行で出力してください。

入力例 1
Copy
3 2
3
ai ml data
4
ml data web security
2
ai ml
出力例 1
Copy
2
入力例 2
Copy
4 1
3
biology chemistry physics
2
chemistry medicine
4
physics math statistics chemistry
3
biology ecology environment
出力例 2
Copy
4
入力例 3
Copy
5 3
5
deeplearning nlp vision robotics optimization
4
nlp vision speech recognition
6
deeplearning nlp vision gan transformer diffusion
3
robotics control automation
5
nlp vision deeplearning bert attention
出力例 3
Copy
3
"""
N,K = map(int,input().split())

labs = []
for _ in range(N):
    M = int(input())
    W = set(input().split())
    #2つの研究室の間で共通テーマが K 個以上あるか？
    labs.append(W)
    
ans = 0 
    #全ペアをチェック
for i in range(N):
    for j in range(i+1,N):
        if len(labs[i] & labs[j]) >= K:
            ans += 1

print(ans)