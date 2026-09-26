"""
問題文
数直線上に N 人の人がいます。人には 1 から N までの番号がついており、人 i は座標 X 
i
​	
  にいます。ただし、同じ座標に複数の人がいる場合もあります。

ある人が「一線を画す」とは、自分以外のどの人との距離も D 以上であることをいいます。

厳密には、人 i が「一線を画す」とは、 すべての j (1≤j≤N, j

=i) に対して ∣X 
i
​	
 −X 
j
​	
 ∣≥D が成り立つことをいいます。

「一線を画す」人の番号をすべて昇順に出力してください。

LLM向けの情報はこちら: https://atcoder.jp/r/TPx-P9pAcjQeFT8zKzK1rD5e7KN99jYeJLMwNJOfP-XaH0jSA5EjEsSCTtyutUsmSEcDmnA0eysPbMlNBYqWbEeyDt1UEUY
翻訳に関する情報はこちら: https://atcoder.jp/r/TPx-P9pAcjQeFT8zKzK1rD5e7KN99jYeJLMwNJOfP-XaH0jSA5EjEsSCTtyutUsmSEcDmnA0eysPbMlNBYqWbEeyDt1UEUY?reason=t
制約
2≤N≤100
1≤D≤10 
9
 
1≤X 
i
​	
 ≤10 
9
 
入力される値は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N D
X 
1
​	
  X 
2
​	
  … X 
N
​	
 
出力
一線を画す人の人数を K、その人たちの番号を昇順に並べた列を (P 
1
​	
 ,P 
2
​	
 ,…,P 
K
​	
 ) とする。以下の形式で出力せよ。

K
P 
1
​	
  P 
2
​	
  … P 
K
​	
 
ただし K=0 の場合、2 行目は空行とせよ。

入力例 1
Copy
3 3
1 5 7
出力例 1
Copy
1
1
人 1 は、人 2 との距離が 4 、人 3 との距離が 6 で、自分以外のどの人との距離も D 以上です。よって「一線を画す」人です。
人 2 は人 3 との距離が 2 ですから、「一線を画す」人ではありません。
同様に、人 3 も人 2 との距離が 2 ですから、「一線を画す」人ではありません。

よって、「一線を画す」人は人 1 のみです。

入力例 2
Copy
3 2
1 1 1
出力例 2
Copy
0

同じ座標の人がいることもあります。また、「一線を画す」人がいない場合は 2 行目は空行としてください。

入力例 3
Copy
8 3
4 77 20 26 9 26 22 40
出力例 3
Copy
4
1 2 5 8
「一線を画す人」の番号は昇順に出力してください。

"""
N,D = map(int,input().split())
X = list(map(int,input().split()))
K = 0
ans = []

for i in range(N):
    ok = True
    for j in range(N):
            if i == j:
                continue
            if abs(X[i] - X[j]) <D:
                ok = False
                break 
    
    if ok:
        ans.append(i+1)
print(len(ans))
print(*ans)

          