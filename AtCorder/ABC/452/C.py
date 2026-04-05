"""
問題文
アーティストの高砂君は、魚の骨をかたどったオブジェを作りました。

オブジェは N 本の肋骨と 1 本の脊椎からなります。 肋骨には 1 から N までの番号が付けられています。

高砂君は、以下の条件をすべて満たすように N+1 本の骨に 1 つずつ文字列を書こうと考えています。

脊椎に書く文字列の長さは N である。
肋骨 i=1,…,N に対して、以下が成り立つ。
肋骨 i に書く文字列の長さは A 
i
​	
  である。
肋骨 i に書く文字列の B 
i
​	
  文字目は、脊椎に書く文字列の i 文字目に一致する。
N+1 本の骨に書く文字列はいずれも、S 
1
​	
 ,⋯,S 
M
​	
  のいずれかである(重複してもよい)。
S 
1
​	
 ,⋯,S 
M
​	
  は英小文字からなる文字列であり、互いに異なります。

j=1,⋯,M に対して、以下の質問に答えてください。

条件を満たす書き方のうち、脊椎に書く文字列が S 
j
​	
  であるものは存在しますか？
制約
N は整数
1≤N≤10
A 
i
​	
 ,B 
i
​	
  は整数 (1≤i≤N)
1≤B 
i
​	
 ≤A 
i
​	
 ≤10 (1≤i≤N)
M は整数
1≤M≤200000
S 
j
​	
  は英小文字からなる文字列 (1≤j≤M)
1≤∣S 
j
​	
 ∣≤10 (1≤j≤M)
S 
1
​	
 ,⋯,S 
M
​	
  は相異なる
入力
入力は以下の形式で標準入力から与えられる。

N
A 
1
​	
  B 
1
​	
 
⋮
A 
N
​	
  B 
N
​	
 
M
S 
1
​	
 
⋮
S 
M
​	
 
出力
M 行出力せよ。

j 行目 (1≤j≤M) には、条件を満たす書き方のうち脊椎に書く文字列が S 
j
​	
  のものが存在するならば Yes を、存在しないならば No を出力せよ。

入力例 1
Copy
5
5 3
5 2
4 1
5 1
3 2
8
retro
chris
itchy
tuna
crab
rock
cod
ash
出力例 1
Copy
Yes
Yes
No
No
No
No
No
No
肋骨 1,2,3,4,5 にそれぞれ chris, retro, tuna, retro, cod と書くことで、脊椎に retro を書いたときに条件を満たします。



retro の長さは 5 文字。
各肋骨について、以下が成り立つ。
肋骨 1 に書かれる文字列 chris の長さは 5 文字である。その 3 文字目は r であり、retro の 1 文字目に一致する。
肋骨 2 に書かれる文字列 retro の長さは 5 文字である。その 2 文字目は e であり、retro の 2 文字目に一致する。
肋骨 3 に書かれる文字列 tuna の長さは 4 文字である。その 1 文字目は t であり、retro の 3 文字目に一致する。
肋骨 4 に書かれる文字列 retro の長さは 5 文字である。その 1 文字目は r であり、retro の 4 文字目に一致する。
肋骨 5 に書かれる文字列 cod の長さは 3 文字である。その 2 文字目は o であり、retro の 5 文字目に一致する。
肋骨 1,2,3,4,5 にそれぞれ itchy, chris, rock, itchy, ash と書くことで、脊椎に chris を書いたときに条件を満たします。



入力例 2
Copy
5
5 1
5 2
5 3
5 4
5 5
8
retro
chris
itchy
tuna
crab
rock
cod
ash
出力例 2
Copy
Yes
Yes
Yes
No
No
No
No
No
"""
N = int(input())
AB = [tuple(map(int,input().split())) for _ in range(N)]
M = int(input())
strings = [input() for _ in range(M)]

#前処理(長さ、いち、文字)
valid = set()
for s in strings:
    for pos,c in enumerate(s):
        valid.add((len(s),pos,c))

#各単語をチェック
for s in strings:
    #長さがNじゃない
    if len(s)!= N:
        print("No")
        continue
    
    ok = True 
    for i,(A,B) in enumerate(AB):
        c = s[i]
        if (A,B-1,c) not in valid:
            ok = False
            break

    print("Yes" if ok else "No")