"""
AtCorder.ABC.190.C の Docstring
,2,…,N の番号がついた N 個の皿と、1,2,…,M の番号がついた M 個の条件があります。
条件 i は、皿 A 
i
​	
  と皿 B 
i
​	
  の両方にボールが (1 個以上) 置かれているとき満たされます。
1,2,…,K の番号がついた K 人の人がいて、人 i は皿 C 
i
​	
  か皿 D 
i
​	
  のどちらか一方にボールを置きます。
満たされる条件の個数は最大でいくつでしょうか？

制約
入力は全て整数
2≤N≤100
1≤M≤100
1≤A 
i
​	
 <B 
i
​	
 ≤N
1≤K≤ 16
1≤C 
i
​	
 <D 
i
​	
 ≤N
入力
入力は以下の形式で標準入力から与えられる。

N M
A 
1
​	
  B 
1
​	
 
⋮
A 
M
​	
  B 
M
​	
 
K
C 
1
​	
  D 
1
​	
 
⋮
C 
K
​	
  D 
K
​	
 
出力
答えを出力せよ。

入力例 1
Copy
4 4
1 2
1 3
2 4
3 4
3
1 2
1 3
2 3
出力例 1
Copy
2
例えば、人 1,2,3 がそれぞれ皿 1,3,2 にボールを置くと、条件 1,2 の 2 つが満たされます。

入力例 2
Copy
4 4
1 2
1 3
2 4
3 4
4
3 4
1 2
2 4
2 4
出力例 2
Copy
4
例えば、人 1,2,3,4 がそれぞれ皿 3,1,2,4 にボールを置くと、全ての条件が満たされます。

入力例 3
Copy
6 12
2 3
4 6
1 2
4 5
2 6
1 5
4 5
1 3
1 2
2 6
2 3
2 5
5
3 5
1 4
2 6
4 6
5 6
出力例 3
Copy
9
"""
N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(M)]

K = int(input())
CD = [tuple(map(int, input().split())) for _ in range(K)]

ans = 0

# bit 全探索
for mask in range(1 << K):
    balls = [0] * (N + 1)  # balls[x] = 皿xにボールがあるか

    # 人ごとの選択
    for i in range(K):
        if (mask >> i) & 1:
            balls[CD[i][1]] = 1  # D_i
        else:
            balls[CD[i][0]] = 1  # C_i

    # 条件チェック
    cnt = 0
    for a, b in AB:
        if balls[a] and balls[b]:
            cnt += 1

    ans = max(ans, cnt)

print(ans)
