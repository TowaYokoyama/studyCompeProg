"""
AtCorder.ABC.383.D の Docstring
N 以下の正整数のうち、正の約数をちょうど 9 個持つものの個数を求めてください。

制約
1≤N≤4×10 
12
 
入力される数値は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N
出力
答えを出力せよ。

入力例 1
Copy
200
出力例 1
Copy
3
条件を満たす正整数は 36,100,196 の 3 個です。

入力例 2
Copy
4000000000000
出力例 2
Copy
407073
"""
import sys
import math
from bisect import bisect_right

def sieve(n: int):
    """return list of primes <= n"""
    if n < 2:
        return []
    is_prime = bytearray(b"\x01") * (n + 1)
    is_prime[0:2] = b"\x00\x00"
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            step = i
            start = i * i
            is_prime[start:n+1:step] = b"\x00" * ((n - start) // step + 1)
    return [i for i in range(2, n + 1) if is_prime[i]]

def main():
    N = int(sys.stdin.readline().strip())
    M = math.isqrt(N)  # floor(sqrt(N))

    primes = sieve(M)

    ans = 0

    # (1) p^8
    # p^8 <= N となる素数 p を数える
    for p in primes:
        if p**8 <= N:
            ans += 1
        else:
            break  # p は増えるので以降は無理

    # (2) p^2 q^2  <=>  p*q <= M
    # 素数リスト primes を使って、p<q のペア数を数える
    for i, p in enumerate(primes):
        limit = M // p
        # q <= limit の最後の index(排他的) を取る
        j = bisect_right(primes, limit)
        # q は primes[i+1 .. j-1]
        cnt = j - (i + 1)
        if cnt > 0:
            ans += cnt
        else:
            # p が大きくなると limit は小さくなるので、以降も 0 のまま
            # ただし p=2 以外でも一応早期終了可能
            if limit <= p:
                break

    print(ans)

if __name__ == "__main__":
    main()
