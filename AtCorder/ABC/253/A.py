"""
AtCorder.ABC.253.A の Docstring
実行時間制限: 2 sec / メモリ制限: 1024 MiB

配点 : 
100 点

問題文
整数 
a,b,c が与えられます。
b がこれらの整数の中央値であるかどうか判定してください。

制約
1≤a,b,c≤100
入力は全て整数
入力
入力は以下の形式で標準入力から与えられる。

a 
b 
c
出力
b が与えられた整数の中央値であるならば Yes、そうでないならば No と出力せよ。

入力例 1
Copy
5 3 2
出力例 1
Copy
Yes
与えられた整数を小さい順に並べると 
2,3,5 となり、
b はこれらの整数の中央値です。

入力例 2
Copy
2 5 3
出力例 2
Copy
No
b は与えられた整数の中央値ではありません。

入力例 3
Copy
100 100 100
出力例 3
Copy
Yes

"""
a,b,c = map(int,input().split())

k = [a,b,c]
k.sort()#昇順にソート
if k[1] == b:
    print("Yes")
else:
    print("No")
  