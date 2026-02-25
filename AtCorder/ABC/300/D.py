"""
問題文
N 以下の正整数のうち、 a<b<c なる 素数 a,b,c を用いて a 
2
 ×b×c 
2
  と表せるものはいくつありますか?

制約
N は 300≤N≤10 
12
  を満たす整数
入力
入力は以下の形式で標準入力から与えられる。

N
出力
答えを整数として出力せよ。

入力例 1
Copy
1000
出力例 1
Copy
3
1000 以下で条件を満たす整数は以下の 3 つです。

300=2 
2
 ×3×5 
2
 
588=2 
2
 ×3×7 
2
 
980=2 
2
 ×5×7 
2
 
入力例 2
Copy
1000000000000
出力例 2
Copy
2817785

"""
import sys
import threading

def solve():
    import math
    from bisect import bisect_right
    
    N = int(sys.stdin.readline())
    
    MAX = 10**6
    sieve = [True] * (MAX+1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(MAX**0.5)+1):
        if sieve[i]:
            for j in range(i*i, MAX+1, i):
                sieve[j] = False
    
    primes = [i for i in range(2, MAX+1) if sieve[i]]
    
    ans = 0
    L = len(primes)
    
    for i in range(L):
        a = primes[i]
        if a*a*a*a > N:
            break
        
        for k in range(i+2, L):
            c = primes[k]
            
            if a*a*c*c > N:
                break
            
            limit = N // (a*a*c*c)
            
            # b は primes[i+1] ～ primes[k-1]
            # b ≤ limit
            r = bisect_right(primes, limit)
            
            # b の有効範囲
            left = i + 1
            right = min(k, r)
            
            if right > left:
                ans += right - left
    
    print(ans)

if __name__ == "__main__":
    solve()
