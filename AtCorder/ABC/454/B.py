""""
問題文
1 から N の番号が付いた N 人の人がいます。
また、1 から M の番号が付いた M 種類の服があります。人 i は服 F 
i
​	
  を着ています。
次の 2 個の質問に Yes か No で答えてください。

質問 1: N 人全員が異なる種類の服を着ていますか？
質問 2: M 種類の服全てについて、その服を着ている人が少なくとも 1 人ずついますか？
制約
1≤N≤100
1≤M≤100
1≤F 
i
​	
 ≤M
入力される値は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N M
F 
1
​	
  F 
2
​	
  … F 
N
​	
 
出力
2 行出力せよ。i 行目には質問 i の答えが Yes であれば Yes を、No であれば No を出力せよ。

入力例 1
Copy
3 4
1 2 4
出力例 1
Copy
Yes
No
全員が異なる種類の服を着ているので、1 番目の質問の答えは Yes です。
また、服 3 を着ている人は存在しないので、2 番目の質問の答えは No です。

入力例 2
Copy
4 2
1 2 1 2
出力例 2
Copy
No
Yes
入力例 3
Copy
4 4
1 3 2 1
出力例 3
Copy
No
No
入力例 4
Copy
5 5
1 3 4 2 5
出力例 4
Copy
Yes
Yes 
"""
N,M = map(int,input().split())
F = list(map(int,input().split()))

# 質問1: 全員が異なる服を着ているか？
unique = set(F)
if len(unique) == N:
    print("Yes")
else:
    print("No")

# 質問2: M種類全ての服を着ている人が少なくとも1人いるか？
if len(unique) == M:
    print("Yes")
else:
    print("No")