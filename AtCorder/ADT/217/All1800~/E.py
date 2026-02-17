"""
AtCorder.ADT.217.All1800~.E の Docstring
文字列 S,T が与えられます。S は英小文字からなり、T は S に英小文字を 1 つ挿入して作られたことがわかっています。

挿入された文字は T の先頭から何番目の文字であるか求めてください。
複数の候補が考えられる場合はいずれか 1 つを求めてください。

制約
1≤∣S∣≤5×10 
5
 
S は英小文字からなる
T は S に英小文字を 1 つ挿入して作られた文字列である
入力
入力は以下の形式で標準入力から与えられる。

S
T
出力
答えを出力せよ。なお、答えが複数考えられる場合はどれを出力しても正解となる。

入力例 1
Copy
atcoder
atcorder
出力例 1
Copy
5
T の先頭から 5 番目の文字 r が挿入された文字です。

入力例 2
Copy
million
milllion
出力例 2
Copy
5
T の先頭から 3,4,5 番目の文字のいずれかが挿入された文字です。
よって、3,4,5 のいずれかを出力すると正解となります。

入力例 3
Copy
vvwvw
vvvwvw
出力例 3
Copy
3
"""
S = input()
T = input()
#S = atcoder
#T = atcorder
#出力５
for i in range(len(S)):
    if S[i] != T[i]:
        print(i+1)
        break 
else:
        # 最後に追加された場合
    print(len(T))