"""
AtCorder.アルゴリズム検定.11回.E の Docstring
問題文
数列 A があり、A は初め空です。 A, B, C, D, E, F, L, R からなる長さ N の文字列 S が与えられます。
S の i 文字目を S 
i
​	
  と表すことにします。
i=1,2,3,…,N のそれぞれについて、この順に以下の処理を行ってください。

S 
i
​	
  が L のとき : A の先頭に i を挿入する。
S 
i
​	
  が R のとき : A の末尾に i を挿入する。
S 
i
​	
  が A のとき : A の長さが 0 以下なら ERROR と出力する。そうでなければ、A の前から 1 番目の数を出力し削除する。
S 
i
​	
  が B のとき : A の長さが 1 以下なら ERROR と出力する。そうでなければ、A の前から 2 番目の数を出力し削除する。
S 
i
​	
  が C のとき : A の長さが 2 以下なら ERROR と出力する。そうでなければ、A の前から 3 番目の数を出力し削除する。
S 
i
​	
  が D のとき : A の長さが 0 以下なら ERROR と出力する。そうでなければ、A の後ろから 1 番目の数を出力し削除する。
S 
i
​	
  が E のとき : A の長さが 1 以下なら ERROR と出力する。そうでなければ、A の後ろから 2 番目の数を出力し削除する。
S 
i
​	
  が F のとき : A の長さが 2 以下なら ERROR と出力する。そうでなければ、A の後ろから 3 番目の数を出力し削除する。
制約
1≤N≤3×10 
5
 
S は A, B, C, D, E, F, L, R からなる長さ N の文字列
入力
入力は以下の形式で標準入力から与えられる。

N
S
出力
問題文の指示に従って、改行区切りで出力せよ。

入力例 1
Copy
11
LLRLRCDEFBA
出力例 1
Copy
1
5
2
ERROR
3
4
以下のように処理されます。

S 
1
​	
  は L なので、1 を先頭に挿入する。A=(1) となる。
S 
2
​	
  は L なので、2 を先頭に挿入する。A=(2,1) となる。
S 
3
​	
  は R なので、3 を末尾に挿入する。A=(2,1,3) となる。
S 
4
​	
  は L なので、4 を先頭に挿入する。A=(4,2,1,3) となる。
S 
5
​	
  は R なので、5 を末尾に挿入する。A=(4,2,1,3,5) となる。
S 
6
​	
  は C なので、前から 3 番目の数 1 を出力し削除する。A=(4,2,3,5) となる。
S 
7
​	
  は D なので、後ろから 1 番目の数 5 を出力し削除する。A=(4,2,3) となる。
S 
8
​	
  は E なので、後ろから 2 番目の数 2 を出力し削除する。A=(4,3) となる。
S 
9
​	
  は F であるが、長さが 2 以下なので、ERROR を出力する。
S 
10
​	
  は B なので、前から 2 番目の数 3 を出力し削除する。A=(4) となる。
S 
11
​	
  は A なので、前から 1 番目の数 4 を出力し削除する。A=() となる。
入力例 2
Copy
36
RLLDBBDDLCLDFRLRRLRRFLRDRLALLELCAARF
出力例 2
Copy
1
2
ERROR
3
ERROR
ERROR
9
ERROR
17
23
26
20
28
31
29
19
"""
from collections import deque 
N = int(input())
S = input()
"""
L のとき : A の先頭に i を挿入する
R のとき : A の末尾に i を挿入する
A のとき : A の長さが 0 以下なら ERROR と出力する。そうでなければ、A の前から 1 番目の数を出力し削除する。
B のとき : A の長さが 1 以下なら ERROR と出力する。そうでなければ、A の前から 2 番目の数を出力し削除する。
C のとき : A の長さが 2 以下なら ERROR と出力する。そうでなければ、A の前から 3 番目の数を出力し削除する。
D のとき : A の長さが 0 以下なら ERROR と出力する。そうでなければ、A の後ろから 1 番目の数を出力し削除 
E のとき : A の長さが 1 以下なら ERROR と出力する。そうでなければ、A の後ろから 2 番目の数を出力し削除す
F のとき : A の長さが 2 以下なら ERROR と出力する。そうでなければ、A の後ろから 3 番目の数を出力し削除す
"""
from collections import deque

N = int(input())
S = input()

dq = deque()

for i in range(1, N+1):
    c = S[i-1]

    if c == "L":
        dq.appendleft(i)

    elif c == "R":
        dq.append(i)

    elif c == "A":
        if len(dq) < 1:
            print("ERROR")
        else:
            print(dq.popleft())

    elif c == "B":
        if len(dq) < 2:
            print("ERROR")
        else:
            x = dq[1]
            del dq[1]
            print(x)

    elif c == "C":
        if len(dq) < 3:
            print("ERROR")
        else:
            x = dq[2]
            del dq[2]
            print(x)

    elif c == "D":
        if len(dq) < 1:
            print("ERROR")
        else:
            print(dq.pop())

    elif c == "E":
        if len(dq) < 2:
            print("ERROR")
        else:
            x = dq[-2]
            del dq[-2]
            print(x)

    elif c == "F":
        if len(dq) < 3:
            print("ERROR")
        else:
            x = dq[-3]
            del dq[-3]
            print(x)
