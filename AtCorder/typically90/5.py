"""
AtCorder.typically90.5 の Docstring

数字 c 
1
​	
 ,c 
2
​	
 ,…,c 
K
​	
  のみを使うことで作れる N 桁の正の整数のうち B の倍数であるものは何個あるでしょうか。 10 
9
 +7 で割った余りを求めてください。

制約
1≤K≤9
1≤c 
1
​	
 <c 
2
​	
 <⋯<c 
K
​	
 ≤9
1≤N≤10 
18
 
2≤B≤1000
入力はすべて整数
小課題・得点
この問題はいくつかの小課題に分けられ、その小課題のすべてのテストケースに正解した場合に「この小課題に正解した」とみなされます。
提出したソースコードの得点は、正解した小課題の点数の合計となります。

(1 点)： N≤10000, B≤30
(3 点)： B≤30
(3 点)： 追加の制約はない。
入力
入力は以下の形式で標準入力から与えられます。

N B K
c 
1
​	
  c 
2
​	
  ⋯ c 
K
​	
 
出力
答えを 10 
9
 +7 で割った余りを出力してください。

入力例 1
Copy
3 7 3
1 4 9
出力例 1
Copy
3
1,4,9 から作れる 3 桁の 7 の倍数は 119,441,994 の 3 個です。

入力例 2
Copy
5 2 3
1 4 9
出力例 2
Copy
81
入力例 3
Copy
10000 27 7
1 3 4 6 7 8 9
出力例 3
Copy
989112238
入力例 4
Copy
1000000000000000000 29 6
1 2 4 5 7 9
出力例 4
Copy
853993813
※この入力例は小課題 2,3 のみの制約を満たします。

入力例 5
Copy
1000000000000000000 957 7
"""
import sys

MOD = 10**9 + 7

def combine(a, b, shift, B):
    """
    a: 長さLAの dp（余りごとの個数）
    b: 長さLBの dp
    shift = 10^LB mod B
    連結した dp を返す
    """
    res = [0] * B
    mod = MOD
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        base = (i * shift) % B
        # res[(base + j) % B] += ai * b[j]
        for j, bj in enumerate(b):
            if bj:
                res[(base + j) % B] = (res[(base + j) % B] + ai * bj) % mod
    return res

def main():
    input = sys.stdin.readline
    N, B, K = map(int, input().split())
    digits = list(map(int, input().split()))

    # dp_blocks[p] : 長さ 2^p のときの余りDP
    # pow10[p]     : 10^(2^p) mod B
    dp_blocks = []
    pow10 = []

    # p=0（長さ1）
    dp0 = [0] * B
    for d in digits:
        dp0[d % B] = (dp0[d % B] + 1) % MOD
    dp_blocks.append(dp0)
    pow10.append(10 % B)  # 10^(1) mod B

    # 2^p を作っていく（N <= 1e18 なので 60 ビット程度）
    MAXP = 0
    while (1 << MAXP) <= N:
        MAXP += 1

    for p in range(1, MAXP):
        # 長さ 2^p = (2^(p-1)) + (2^(p-1))
        prev = dp_blocks[p - 1]
        shift = pow10[p - 1]              # 10^(2^(p-1)) mod B
        dp_blocks.append(combine(prev, prev, shift, B))
        pow10.append((shift * shift) % B) # 10^(2^p) mod B

    # N のビットに従って連結
    ans = [0] * B
    ans[0] = 1  # 長さ0（空）を余り0として1通り
    p = 0
    while N > 0:
        if N & 1:
            ans = combine(ans, dp_blocks[p], pow10[p], B)
        N >>= 1
        p += 1

    print(ans[0] % MOD)

if __name__ == "__main__":
    main()
