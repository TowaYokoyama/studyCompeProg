"""
AtCorder.ABC.311.B の Docstring
問題文
1 から 
N までの番号がついた 
N 人の人がいます。
N 人の人の今後 
D 日間の予定が与えられます。人 
i の予定は長さ 
D の文字列 
S 
i
​
  で表されて、
S 
i
​
  の 
j 文字目が o ならば 
j 日目は暇であることを、x ならばそうでないことを意味します。

D 日間のうち全員が暇であるような 連続する 何日かを選ぶことを考えます。
選べる日数は最大で何日ですか？ただし、選べる日が存在しない場合は 
0 日と答えてください。

制約
1≤N≤100
1≤D≤100
N,D は整数
S 
i
​
  は o と x からなる長さ 
D の文字列
入力
入力は以下の形式で標準入力から与えられる。

N 
D
S 
1
​
 
S 
2
​
 
⋮
S 
N
​
 
出力
選べる日数の最大値を出力せよ。選べる日が存在しない場合は 0 を出力せよ。

入力例 1
Copy
3 5
xooox
oooxx
oooxo
出力例 1
Copy
2
2 日目と 
3 日目は全員が暇な日なので選ぶことができます。
この 
2 日間を選ぶと、連続する日にちを選ぶ方法の中で日数を最大にすることができます。

入力例 2
Copy
3 3
oxo
oxo
oxo
出力例 2
Copy
1
選ぶ日にちは連続している必要があるのに注意してください。(
1 日目と 
3 日目は全員が暇な日なので選ぶことができますが、この 
2 つを同時に選ぶことはできません)

入力例 3
Copy
3 3
oox
oxo
xoo
出力例 3
Copy
0
選べる日が存在しない場合は 0 を出力してください。

入力例 4
Copy
1 7
ooooooo
出力例 4
Copy
7
入力例 5
Copy
5 15
oxooooooooooooo
oxooxooooooooox
oxoooooooooooox
oxxxooooooxooox
oxooooooooxooox
出力例 5
Copy
5

"""
N,D = map(int,input().split())
S = []
for _ in range(N):
    S.append(input())

ans = 0
cur = 0
for day in range(D):
    ok = True 
    for person in range(N):
        if S[person][day] == 'x' :
            ok = False 
            break 
        
    if ok:
        cur+=1
        ans = max(ans,cur)
    else:
        cur = 0
        
print(ans)