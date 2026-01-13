"""
AtCorder.typically90.6 の Docstring
英小文字のみからなる、長さ N の文字列 S が与えられます。

長さが K である S の部分列のうち、辞書順で最小であるものを出力してください。

注意
文字列 T の 部分列 とは、T から 0 個以上の文字を取り除いた後、残りの文字を元の順序を保ったまま連結して得られる文字列を指します。

「辞書順」での大小の定義
X=x 
1
​	
 x 
2
​	
 …x 
n
​	
 , Y=y 
1
​	
 y 
2
​	
 …y 
m
​	
  を二つの異なる文字列とするとき、X が Y の接頭辞であるか、j を x 
j
​	
 

=y 
j
​	
  であるような最小の整数として x 
j
​	
 <y 
j
​	
  である場合、そしてその場合に限って「X は Y より辞書順で小さい」と言います。
制約
1≤K≤N≤100000
S は英小文字のみからなる長さ N の文字列
N,K は整数
入力
入力は以下の形式で標準入力から与えられます。

N K
S
出力
答えとなる文字列を出力してください。

入力例 1
Copy
7 3
atcoder
出力例 1
Copy
acd
1,3,5 文字目のみを取り出すことで文字列 acd ができます。
この文字列はあり得る 3 文字の部分列のなかで辞書順最小です。

入力例 2
Copy
14 5
kittyonyourlap
出力例 2
Copy
inlap
"""
def solve():
    N, K = map(int, input().split())
    S = input().strip()

    # next_pos[i][c] = i以降で文字cが最初に出る位置
    INF = N
    next_pos = [[INF]*26 for _ in range(N+1)]

    # 後ろから埋める
    for c in range(26):
        next_pos[N][c] = INF

    for i in range(N-1, -1, -1):
        next_pos[i] = next_pos[i+1][:]
        next_pos[i][ord(S[i]) - ord('a')] = i

    ans = []
    pos = 0

    for i in range(K):
        # 選べる最大位置
        limit = N - (K - i)

        for c in range(26):
            nx = next_pos[pos][c]
            if nx <= limit:
                ans.append(chr(c + ord('a')))
                pos = nx + 1
                break

    print("".join(ans))
