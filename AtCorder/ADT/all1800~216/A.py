"""
AtCorder.ADT.all1800~216.A の Docstring

5 枚のカードがあり、それぞれのカードには整数 A,B,C,D,E が書かれています。

この 5 枚組は以下の条件を満たすとき、またそのときに限って、フルハウスであると呼ばれます。

同じ数が書かれたカード 3 枚と、別の同じ数が書かれたカード 2 枚からなる。
5 枚組がフルハウスであるか判定してください。

制約
1≤A,B,C,D,E≤13
A,B,C,D,E 全てが同じ値ではない
入力は全て整数
入力
入力は以下の形式で標準入力から与えられる。

A B C D E
出力
フルハウスである場合 Yes を、そうでないとき No を出力せよ。

入力例 1
Copy
1 2 1 2 1
出力例 1
Copy
Yes
1 が書かれたカード 3 枚と、2 が書かれたカード 2 枚からなるため、これはフルハウスです。

入力例 2
Copy
12 12 11 1 2
出力例 2
Copy
No
フルハウスの条件を満たしません。
"""
from collections import Counter
A, B, C, D, E = input().split()
a = [A, B, C, D, E]
c = Counter(a)
if sorted(c.values()) == [2, 3]:
    print("Yes")
else:
    print("No")