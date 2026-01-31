"""
AtCorder.ABC.371.A の Docstring
A, B, C の三兄弟がいます。この 3 人の年齢関係は、3 つの文字 S 
AB
​	
 ,S 
AC
​	
 ,S 
BC
​	
  によって与えられ、それぞれ以下を意味します。

S 
AB
​	
  が < の場合 A は B より年下であり、> の場合 A は B より年上である。
S 
AC
​	
  が < の場合 A は C より年下であり、> の場合 A は C より年上である。
S 
BC
​	
  が < の場合 B は C より年下であり、> の場合 B は C より年上である。
三兄弟の次男、つまり二番目に年上の人は誰ですか？

制約
S 
AB
​	
 ,S 
AC
​	
 ,S 
BC
​	
  はそれぞれ < または >
入力に矛盾は含まれない。つまり、与えられた大小関係を全て満たす年齢関係が必ず存在する入力のみが与えられる。
入力
入力は以下の形式で標準入力から与えられる。

S 
AB
​	
  S 
AC
​	
  S 
BC
​	
 
出力
三兄弟の次男、つまり二番目に年上の人の名前を出力せよ。

入力例 1
Copy
< < <
出力例 1
Copy
B
A が B より年下であり、B が C より年下であることから、C が長男、B が次男、A が三男であることがわかります。よって答えは B です。

入力例 2
Copy
< < >
出力例 2
Copy
C
"""
Sa,Sb,Sc = input().split()
score = {'A': 0, 'B': 0, 'C': 0}
if Sa == '<':
    score['B'] += 1
else:
    score['A']+=1
if Sb == '<':
    score['C']+=1
else:
    score['A']+=1

if Sc == '<':
   score['C'] += 1
else:
    score['B']+=1

for k,v in score.items():
    if v == 1:
        print(k)