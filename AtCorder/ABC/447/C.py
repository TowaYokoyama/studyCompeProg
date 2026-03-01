"""
問題文
英大文字からなる文字列 S,T が与えられます。

あなたは以下の 2 種類の操作を好きな順序で好きな回数（0 回でも良い）行うことができます。

S の好きな位置（先頭および末尾を含む）に文字 A を 1 つ挿入する。
S に含まれる文字 A を 1 つ選んで削除する。なお、残った文字は元の順序を保ったまま連結される。
S を T に一致させることが可能かどうか判定し、可能な場合は必要な操作回数の合計の最小値を求めてください。

制約
S,T は英大文字からなる長さ 1 以上 3×10 
5
  以下の文字列
入力
入力は以下の形式で標準入力から与えられる。

S
T
出力
S を T に一致させることが可能ならば必要な操作回数の合計の最小値を、不可能ならば -1 を出力せよ。

入力例 1
Copy
ABC
BACA
出力例 1
Copy
3
以下のように、合計 3 回の操作で S を T に一致させることが可能です。

S の 2 文字目と 3 文字目の間に A を 1 つ挿入する。S= ABAC となる。
S の 1 文字目にある A を削除する。S= BAC となる。
S の末尾に A を 1 つ挿入する。S= BACA となる。
合計 2 回以下の操作で S を T に一致させることはできないため、答えは 3 です。

入力例 2
Copy
ABC
ARC
出力例 2
Copy
-1
どのように操作を行っても、S を T に一致させることはできません。

入力例 3
Copy
ABC
ABC
出力例 3
Copy
0
1 回も操作を行う必要がありません。

入力例 4
Copy
AAAWAZAAAABAAAU
AWAAZABAAAAAUA
出力例 4
Copy
9
"""
S = input()
T = input()

if [c for c in S if c != 'A'] != [c for c in T if c != 'A']:
    print(-1)#A以外の位置が違うなら即終了
else:
    i,j = 0,0
    ans = 0
    while i <len(S) or j <len(T):
        if i < len(S) and j < len(T) and S[i] != 'A' and T[j] != 'A':
            i+= 1
            j+= 1
        elif i < len(S) and S[i] == 'A' and (j >= len(T) or T[j] != 'A'):
            ans += 1 #Sのaを削除
            i += 1
        elif j < len(T) and T[j] == 'A' and (i >= len(S) or S[i] != 'A'):
            ans += 1
            j+= 1
        else:
            #両方A =>一致操作不要
            i+= 1
            j+= 1
    print(ans)