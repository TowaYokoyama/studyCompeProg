"""
AtCorder.ABC.360.B の Docstring
英小文字からなる文字列 S と T が与えられます。

以下の条件を満たす 1≤c≤w<∣S∣ となる整数の組 c と w が存在するか判定してください。ただし、 ∣S∣ は文字列 S の長さを表します。ここで、w は ∣S∣ 未満である必要があることに注意してください。

S を先頭から順に w 文字毎に区切ったとき、長さが c 以上の文字列の c 文字目を順番に連結した文字列が T と一致する
制約
S と T は英小文字からなる文字列
1≤∣T∣≤ ∣S∣≤100
入力
入力は以下の形式で標準入力から与えられる。

S T
出力
条件を満たすような 1≤c≤w<∣S∣ となる整数の組 c と w が存在する場合は Yes を、存在しない場合は No を出力せよ。

入力例 1
Copy
atcoder toe
出力例 1
Copy
Yes
S を 2 文字毎に区切ると以下のようになります。

at
co
de
r
区切った後、 2 文字以上の文字列の 2 文字目を取り出し連結させたときの文字列は、 toe となり T と一致します。よって、 Yes を出力します。

入力例 2
Copy
beginner r
出力例 2
Copy
No
w=∣S∣ であることはないため、条件を満たすような 1≤c≤w<∣S∣ となる整数の組 c と w は存在しません。よって、 No を出力します。

入力例 3
Copy
verticalreading agh
出力例 3
Copy
No
"""
S,T = input().split()
n = len(S)

for w in range(1,n):#区切りはば
    for c in range(1,w+1):#何文字めか
        res = []
        for i in range(0,n,w):
            block = S[i:i+w]
            if len(block) >= c:
                res.append(block[c-1])#c文字め
        if "".join(res) == T:
            print("Yes")
            exit()
print("No")