N = int(input())
ans = []
def rec(i):
  if i == 1:
    ans.append(i)
    return ans 
  else:
    ans.append(i)
    rec(i-1)
rec(N)

print(*ans,sep=",")
"""
問題文
正の整数 N が与えられます。

N,N−1,…,1 をこの順にカンマ , で区切って出力してください。

制約
1≤N≤9
N は整数
入力
入力は以下の形式で標準入力から与えられる。

N
出力
N,N−1,…,1 をこの順にカンマ区切りで出力せよ。

入力例 1
Copy
9
出力例 1
Copy
9,8,7,6,5,4,3,2,1
入力例 2
Copy
5
出力例 2
Copy
5,4,3,2,1
入力例 3
Copy
1
出力例 3
Copy
1

"""
