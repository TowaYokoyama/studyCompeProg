"""
AtCorder.ABC.259.C の Docstring
英小文字からなる 2 つの文字列 S,T が与えられます。 次の操作を好きな回数（ 0 回でも良い）行うことで、S を T と一致させることができるかを判定してください。

S において同じ文字が 2 文字連続しているところの間に、その文字と同じ文字を 1 つ挿入する。 すなわち、下記の 3 つの手順からなる操作を行う。

現在の S の長さを N とし、S=S 
1
​	
 S 
2
​	
 …S 
N
​	
  とする。
1 以上 N−1 以下の整数 i であって、S 
i
​	
 =S 
i+1
​	
  を満たすものを 1 つ選択する。（ただし、そのような i が存在しない場合は、何もせずに手順 3.をスキップして操作を終了する。）
S の i 文字目と i+1 文字目の間に文字 S 
i
​	
 (=S 
i+1
​	
 ) を 1 つ挿入する。その結果、S は長さ N+1 の文字列 S 
1
​	
 S 
2
​	
 …S 
i
​	
 S 
i
​	
 S 
i+1
​	
 …S 
N
​	
  となる。
制約
S と T はそれぞれ英小文字からなる長さ 2 以上 2×10 
5
  以下の文字列
入力
入力は以下の形式で標準入力から与えられる。

S
T
出力
S を T と一致させることができる場合は Yes を、そうでない場合は No を出力せよ。 ジャッジは英小文字と英大文字を厳密に区別することに注意せよ。

入力例 1
Copy
abbaac
abbbbaaac
出力例 1
Copy
Yes
下記の 3 回の操作によって、S= abbaac を T= abbbbaaac に一致させることができます。

まず、S の 2 文字目と 3 文字目の間に b を挿入する。その結果、S= abbbaac となる。
次に、再び S の 2 文字目と 3 文字目の間に b を挿入する。その結果、S= abbbbaac となる。
最後に、S の 6 文字目と 7 文字目の間に a を挿入する。その結果、S= abbbbaaac となる。
よって、Yes を出力します。

入力例 2
Copy
xyzz
xyyzz
出力例 2
Copy
No
どのように操作を行っても、 S= xyzz を T= xyyzz に一致させることはできません。 よって、No を出力します。

"""
S = input()
T = input()

rle_s = []
rle_t = []

# ---------- S の RLE ----------
i = 0
k = len(S)
while i < k:
    j = i
    while j < k and S[i] == S[j]:
        j += 1
    rle_s.append((S[i], j - i))
    i = j

# ---------- T の RLE ----------
i = 0
l = len(T)
while i < l:
    j = i
    while j < l and T[i] == T[j]:
        j += 1
    rle_t.append((T[i], j - i))
    i = j

# ---------- 判定 ----------
z = len(rle_s)
y = len(rle_t)

# ブロック数が違う
if z != y:
    print("No")
    exit()

for x in range(z):
    a, la = rle_s[x]
    b, lb = rle_t[x]

    # 文字が違う
    if a != b:
        print("No")
        exit()

    # 個数が減っている
    if la > lb:
        print("No")
        exit()

    # 1個のブロックは増やせない
    if la == 1 and lb > 1:
        print("No")
        exit()

print("Yes")
