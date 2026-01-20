"""
AtCorder.ABC.263.B の Docstring
N 人の人がいます。N 人の人には人 1, 人 2,…, 人 N と番号がついています。

人 i(2≤i≤N) の親は人 P 
i
​	
  です。ここで、P 
i
​	
 <i が保証されます。

人 1 が人 N の何代前か求めてください。

制約
2≤N≤50
1≤P 
i
​	
 <i(2≤i≤N)
入力は全て整数。
入力
入力は以下の形式で標準入力から与えられる。

N
P 
2
​	
  P 
3
​	
  … P 
N
​	
 
出力
答えを整数として出力せよ。

入力例 1
Copy
3
1 2
出力例 1
Copy
2
人 2 は人 3 の親であるため、人 3 の 1 代前です。

人 1 は人 2 の親であるため、人 3 の 2 代前です。

よって解は 2 です。

入力例 2
Copy
10
1 2 3 4 5 6 7 8 9
出力例 2
Copy
9

"""
N = int(input())
P = list(map(int, input().split()))


cur = N
ans = 0

while cur != 1:
    cur = P[cur - 2]
    ans += 1

print(ans)
