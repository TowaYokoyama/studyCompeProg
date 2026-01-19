"""
AtCorder.ABC.421.B の Docstring
問題文
正整数 x に対し、f(x) を以下のように定義します。

x を（先頭に余分な 0 をつけずに）十進表記して得られる文字列を s 
x
​	
 、s 
x
​	
  を反転して得られる文字列を rev(s 
x
​	
 ) とおく。 f(x) の値は、rev(s 
x
​	
 ) を整数の十進表記としてみなすことで得られる整数である。
例えば、x=13 のとき rev(s 
x
​	
 )= 31 より f(x)=31 であり、x=10 のとき rev(s 
x
​	
 )= 01 より f(x)=1 です。 特に、どのような正整数 x に対しても f(x) の値は正整数です。

正整数 X,Y が与えられます。 正整数列 A=(a 
1
​	
 ,a 
2
​	
 ,…,a 
10
​	
 ) を以下のように定義します。

a 
1
​	
 =X
a 
2
​	
 =Y
a 
i
​	
 =f(a 
i−1
​	
 ＋a 
i−2
​	
 ) (i≥3)
a 
10
​	
  の値を求めてください。

制約
1≤X,Y≤10 
5
 
入力は全て整数
入力
入力は以下の形式で標準入力から与えられる。

X Y
出力
a 
10
​	
  の値を出力せよ。

入力例 1
Copy
1 1
出力例 1
Copy
415
A の各要素の値は以下の通りです。

a 
1
​	
 =1
a 
2
​	
 =1
a 
3
​	
 =2
a 
4
​	
 =3
a 
5
​	
 =5
a 
6
​	
 =8
a 
7
​	
 =31
a 
8
​	
 =93
a 
9
​	
 =421
a 
10
​	
 =415
よって 415 を出力します。

入力例 2
Copy
3 7
出力例 2
Copy
895
入力例 3
Copy
90701 90204
出力例 3
Copy
9560800101
"""
X,Y = map(int,input().split())
ans = []
for i in range(1,11):
    if i ==1:
        ans.append(X)
    elif i == 2:
        ans.append(Y)
    else:
        calc = ans[i-2]+ans[i-3]
        #反転操作
        rev = int(str(calc)[::-1])
        ans.append(rev)
print(ans[9])