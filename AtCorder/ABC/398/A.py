"""
AtCorder.ABC.398.A の Docstring
問題文
以下の条件を全て満たす長さ N の文字列を求めてください。

各文字は - または = である
回文である
文字列中に = は 1 個または 2 個含まれる。 2 個含まれる場合、それらの = は隣接している
なお、そのような文字列はちょうど 1 つ存在します。

制約
1≤N≤100
N は整数である
入力
入力は以下の形式で標準入力から与えられる。

N
出力
答えを出力せよ。

入力例 1
Copy
4
出力例 1
Copy
-==-
入力例 2
Copy
7
出力例 2
Copy
---=---

"""
N = int(input())
ans = []

if N % 2 == 0:
    mid = N//2
    mid1= mid-1
    for i in range(N):
        if i == mid or i == mid1:
            ans.append('=') 
        else:
            ans.append('-')     
else:
    mid = N//2
    for i in range(N):
        if i == mid:
            ans.append('=')
        else:
            ans.append('-')

print("".join(ans)) 