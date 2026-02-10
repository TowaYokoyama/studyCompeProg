"""
AtCorder.鉄則本.A06 の Docstring
問題文
遊園地「ALGO-RESORT」では N 日間にわたるイベントが開催され、 i 日目 (1≤i≤N) には A 
i
​	
  人が来場しました。

以下の合計 Q 個の質問に答えるプログラムを作成してください。

1 個目の質問：L 
1
​	
  日目から R 
1
​	
  日目までの合計来場者数は？
2 個目の質問：L 
2
​	
  日目から R 
2
​	
  日目までの合計来場者数は？
:
Q 個目の質問：L 
Q
​	
  日目から R 
Q
​	
  日目までの合計来場者数は？
制約
1≤N,Q≤10 
5
 
1≤A 
i
​	
 ≤10000
1≤L 
i
​	
 ≤R 
i
​	
 ≤N
入力はすべて整数
入力
入力は以下の形式で標準入力から与えられます。

N Q
A 
1
​	
  A 
2
​	
  ⋯ A 
N
​	
 
L 
1
​	
  R 
1
​	
 
L 
2
​	
  R 
2
​	
 
 :
L 
Q
​	
  R 
Q
​	
 
出力
全体で Q 行出力してください。

i 行目 (1≤i≤Q) には、i 個目の質問への答えを整数で出力してください。

入力例 1
Copy
10 5
8 6 9 1 2 1 10 100 1000 10000
2 3
1 4
3 9
6 8
1 10
出力例 1
Copy
15
24
1123
111
11137
この入力には 5 個の質問が含まれています。

1 個目の質問は 2 日目から 3 日目までの合計来場者数を尋ねるもので、これに対する答えは 6+9=15 です。
2 個目の質問は 1 日目から 4 日目までの合計来場者数を尋ねるもので、これに対する答えは 8+6+9+1=24 です。
"""
N,Q = map(int,input().split())
A = list(map(int,input().split()))
S = []
s = 0
for x in A: 
    S.append(s+x)
    s +=x
for _ in range(Q):
    A,B = map(int,input().split())
    print(S[B-1] - (S[A-2] if A > 1 else 0))

import sys
input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    
    # 累積和（先頭に0を入れる）
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    
    for _ in range(Q):
        L, R = map(int, input().split())
        print(S[R] - S[L - 1])

if __name__ == "__main__":
    main()
