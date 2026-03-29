"""
以下の条件を満たす正整数を 良い整数 とします。

条件：一つ以上の 2 の冪（1,2,4,8,16,…）を（重複と並び替えを許して）選んで文字列として結合し、それを整数として解釈することで得られる。
良い整数のうち N 番目に小さいものを求めてください。 ただし N 番目に小さい良い整数は 10 
9
  以下であることが保証されます。

制約
N は正整数
N 番目に小さい良い整数は 10 
9
  以下
入力
入力は以下の形式で標準入力から与えられる。

N
出力
答えを出力せよ。

入力例 1
Copy
10
出力例 1
Copy
21
良い整数を小さい方から列挙すると 1,2,4,8,11,12,14,16,18,21,… です。

入力例 2
Copy
69
出力例 2
Copy
328
入力例 3
Copy
1099898
出力例 3
Copy
819264512
"""
from collections import deque 
powers = []
p = 1
N = int(input())
#２の指数リスト　
while p <= 10 ** 9:
  powers.append(str(p))
  p *= 2

queue = deque()
for pw in powers:
  queue.append(int(pw))

cnt = 0
while queue:
  num = queue.popleft()
  cnt+= 1
  if cnt == N:
    print(num)
    break 
  for pw in powers:
    next_num = int(str(num)+pw)
    if next_num <= 10** 9:
      queue.append(next_num)