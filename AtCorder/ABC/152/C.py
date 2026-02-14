"""
AtCorder.ABC.152.C の Docstring
問題文
1,…,N の順列 P 
1
​	
 ,…,P 
N
​	
  が与えられます。
次の条件を満たす整数 i(1≤i≤N) の個数を数えてください。

任意の整数 j(1≤j≤i) に対して、 P 
i
​	
 ≤P 
j
​	
 
制約
1≤N≤2×10 
5
 
P 
1
​	
 ,…,P 
N
​	
  は 1,…,N の順列である。
入力はすべて整数である。
入力
入力は以下の形式で標準入力から与えられる。

N
P 
1
​	
  ... P 
N
​	
 
出力
条件を満たす整数 i の個数を出力せよ。

入力例 1
Copy
5
4 2 5 1 3
出力例 1
Copy
3
i=1,2,4 が条件を満たします。
i=3 は条件を満たしません。
例えば、 j=1 とすると、 P 
i
​	
 >P 
j
​	
  となります。
同様に、 i=5 も条件を満たしません。
したがって、条件を満たす整数 i の個数は 3 となります。

入力例 2
Copy
4
4 3 2 1
出力例 2
Copy
4
すべての整数 i(1≤i≤N) が条件を満たします。

入力例 3
Copy
6
1 2 3 4 5 6
出力例 3
Copy
1
i=1 のみが条件を満たします。

入力例 4
Copy
8
5 7 4 2 6 8 1 3
出力例 4
Copy
4
入力例 5
Copy
1
1
出力例 5
Copy
1
"""
N = int(input())
P = list(map(int,input().split()))
min_num = float('inf')
cnt = 0
for x in P:
    if x <= min_num:
        cnt +=1
        min_num = x
print(cnt)