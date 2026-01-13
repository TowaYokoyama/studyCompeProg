"""
AtCorder.ABC.258.C の Docstring
正整数 N,Q と、長さ N の英小文字からなる文字列 S が与えられます。

以下で説明されるクエリを Q 個処理してください。クエリは次の 2 種類のいずれかです。

1 x: 「S の末尾の文字を削除し、先頭に挿入する」という操作を x 回連続で行う。
2 x: S の x 番目の文字を出力する。
制約
2≤N≤5×10 
5
 
1≤Q≤5×10 
5
 
1≤x≤N
∣S∣=N
S は英小文字からなる。
2 x の形式のクエリが 1 個以上与えられる。
N,Q,x はすべて整数。
入力
入力は以下の形式で標準入力から与えられる。

N Q
S
query 
1
​	
 
query 
2
​	
 
⋮
query 
Q
​	
 
それぞれのクエリは以下の形式で与えられる。ここで、t は 1 または 2 である。

t x
出力
2 x の形式の各クエリについて、答えを一行に出力せよ。

入力例 1
Copy
3 3
abc
2 2
1 1
2 2
出力例 1
Copy
b
a
1 個目のクエリのとき、S は abc なので 2 文字目の b を出力します。 2 個目のクエリのとき、S は abc から cab に変わります。 3 個目のクエリのとき、S は cab なので 2 文字目の a を出力します。

入力例 2
Copy
10 8
dsuccxulnl
2 4
2 7
1 2
2 7
1 1
1 2
1 3
2 5
出力例 2
Copy
c
u
c
u

"""
N, Q = map(int, input().split())
S = input()

shift = 0#今先頭がどれだけ右にずれているのか

for _ in range(Q):
    t, x = map(int, input().split())

    if t == 1:
        shift = (shift + x) % N
    else:
        idx = (x - 1 - shift) % N
        print(S[idx])
