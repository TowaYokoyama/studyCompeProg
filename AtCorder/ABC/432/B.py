"""
正整数 X が与えられます。

X を（先頭に 0 を含まない形で）十進表記した際に現れる数字を、先頭に 0 が来ないように 並び替えることで得られる正整数のうち、値が最小のものを求めてください。

制約
1≤X<10 
5
 
X は整数
入力
入力は以下の形式で標準入力から与えられる。

X
出力
答えを出力せよ。

入力例 1
Copy
903
出力例 1
Copy
309
X を十進表記した際に現れる数字を先頭に 0 が来ないように並び替えることで得られる正整数は、903, 930, 309, 390 の 4 通りであり、このうち値が最小のものは 309 です。

入力例 2
Copy
432
出力例 2
Copy
234
入力例 3
Copy
100
出力例 3
Copy
100
"""
X = input()
s = len(X)
K = []
for i in range(s):
    K.append(int(X[i]))
K.sort()

ans = 0
if K[0] != 0:
    for i in range(s):
        ans += K[i] * 10 ** (s-i-1)
        
else:
    #先頭が0の時
    #0じゃない最小の数字を探す
    for i in range(s):
        if K[i] != 0:
            first = K[i]
            K.pop(i)
            break
    #firstを先頭に置く
    ans += first * 10 **(s-1)
    
    #残りを後ろに並べる
    for i in range(s-1):
        ans += K[i] * 10 ** (s - i - 2)

print(ans)