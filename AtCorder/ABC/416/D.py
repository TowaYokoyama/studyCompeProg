"""
AtCorder.ABC.416.D の Docstring
長さ N の非負整数列 A=(A 
1
​	
 ,A 
2
​	
 ,…,A 
N
​	
 ),B=(B 
1
​	
 ,B 
2
​	
 ,…,B 
N
​	
 ) と正整数 M が与えられます。

A の要素を自由に並び替えることが出来るとき、  
i=1
∑
N
​	
 ((A 
i
​	
 +B 
i
​	
 )modM) としてありうる最小値を求めて下さい。

T 個のテストケースが与えられるので、それぞれについて答えを求めてください。

制約
1≤T≤10 
5
 
1≤N≤3×10 
5
 
1≤M≤10 
9
 
0≤A 
i
​	
 ,B 
i
​	
 <M
全てのテストケースにおける N の総和は 3×10 
5
  以下
入力される値は全て整数
入力
入力は以下の形式で標準入力から与えられる。

T
case 
1
​	
 
case 
2
​	
 
⋮
case 
T
​	
 
各テストケース case 
i
​	
  は以下の形式で与えられる。

N M
A 
1
​	
  A 
2
​	
  … A 
N
​	
 
B 
1
​	
  B 
2
​	
  … B 
N
​	
 
出力
T 行出力せよ。

j 行目には j 番目のテストケースについて、  
i=1
∑
N
​	
 ((A 
i
​	
 +B 
i
​	
 )modM) としてありうる最小値を出力せよ。

入力例 1
Copy
3
3 6
3 1 4
2 0 1
1 1000000000
999999999
999999999
10 201
144 150 176 154 110 187 38 136 111 46
96 109 73 63 85 1 156 7 13 171
出力例 1
Copy
5
999999998
619
1 つ目のテストケースについて、 A を 4,3,1 と並び替えると (A 
i
​	
 +B 
i
​	
 )modM はそれぞれ 0,3,2 となり、これらの総和は 5 となります。

"""
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    b = sorted(list(map(int, input().split())))
    c, idx = 0, 0
    for v in a:
        while idx < n and b[idx] + v < m:
            idx += 1
        if idx >= n:
            break
        c += 1
        idx += 1
    print(sum(a) + sum(b) - m * c)
