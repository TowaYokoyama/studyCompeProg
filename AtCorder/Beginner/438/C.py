"""
AtCorder.Beginner.438.C の Docstring
問題文
長さ N の整数列 A=(A 
1
​	
 ,A 
2
​	
 ,…,A 
N
​	
 ) が与えられます。

あなたは以下の操作を 0 回以上好きな順番で好きな回数行うことができます：

A 
k
​	
 =A 
k+1
​	
 =A 
k+2
​	
 =A 
k+3
​	
  を満たす 1 以上 ∣A∣−3 以下の整数 k を選び、A から A 
k
​	
 ,A 
k+1
​	
 ,A 
k+2
​	
 ,A 
k+3
​	
  を削除する。（より厳密には、 A を (A 
1
​	
 ,A 
2
​	
 ,…,A 
k−1
​	
 ,A 
k+4
​	
 ,A 
k+5
​	
 ,…,A 
N
​	
 ) に置き換える。）
ここで、 ∣A∣ は整数列 A の長さを表します。

操作を繰り返した後の最終的な ∣A∣ としてあり得る最小値を求めてください。

制約
1≤N≤2×10 
5
 
1≤A 
i
​	
 ≤N
入力される値は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N
A 
1
​	
  A 
2
​	
  … A 
N
​	
 
出力
操作を繰り返した後の最終的な ∣A∣ としてあり得る最小値を出力せよ。

入力例 1
Copy
10
1 1 1 4 4 4 4 1 2 3
出力例 1
Copy
2
以下のように 2 回操作することで ∣A∣=2 にすることができます。

k=4 を選ぶ。A 
4
​	
 =A 
5
​	
 =A 
6
​	
 =A 
7
​	
 =4 が成り立つためこの選択は正当である。 A=(1,1,1,1,2,3) となる。
k=1 を選ぶ。A 
1
​	
 =A 
2
​	
 =A 
3
​	
 =A 
4
​	
 =1 が成り立つためこの選択は正当である。 A=(2,3) となる。
∣A∣ を 2 未満にすることはできないため、 2 を出力してください。

入力例 2
Copy
3
2 1 3
出力例 2
Copy
3
はじめから操作を行うことができません。

入力例 3
Copy
13
1 1 4 4 4 1 1 1 1 4 1 4 1
出力例 3
Copy
5

"""
N = int(input())
A = list(map(int, input().split()))

stack = []

def check(stack):
    while len(stack) >= 4:
        if stack[-1] == stack[-2] == stack[-3] == stack[-4]:
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
        else:
            break

for a in A:
    stack.append(a)
    check(stack)

print(len(stack))
