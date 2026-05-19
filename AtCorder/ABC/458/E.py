import sys

# 再帰回数の上限を増やす（必要に応じて）
sys.setrecursionlimit(2000000)

MOD = 998244353

# グローバル変数の準備
frac = []
invf = []

def f_init(n):
    global frac, invf
    frac = [1] * (n + 1)
    invf = [1] * (n + 1)
    
    for i in range(1, n + 1):
        frac[i] = (frac[i - 1] * i) % MOD
        
    # フェルマーの小定理を用いて逆元を計算: a^(p-2) ≡ a^(-1) (mod p)
    invf[n] = pow(frac[n], MOD - 2, MOD)
    
    for i in range(n, 0, -1):
        invf[i - 1] = (invf[i] * i) % MOD

def ncr(n, r):
    if n < 0 or n < r:
        return 0
    return frac[n] * invf[r] % MOD * invf[n - r] % MOD

def part1(x, p):
    return ncr(x - 1, p - 1)

def solve():
    # 入力の受け取り
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    x1 = int(data[0])
    x2 = int(data[1])
    x3 = int(data[2])
    
    # 階乗テーブルの初期化
    f_init(x1 + x2 + x3 + 10)
    
    ans = 0
    
    # 13131...1
    for i in range(2, x1 + 1):
        term = part1(x1, i) * part1(x3, i - 1) % MOD * ncr(x1 + x2 + x3 - (i * 2 - 2), x1 + x3) % MOD
        ans = (ans + term) % MOD
        
    # 31313...3
    for i in range(2, x3 + 1):
        term = part1(x3, i) * part1(x1, i - 1) % MOD * ncr(x1 + x2 + x3 - (i * 2 - 2), x1 + x3) % MOD
        ans = (ans + term) % MOD
        
    # 1313...13, 3131...31
    limit = min(x1, x3)
    for i in range(1, limit + 1):
        term = 2 * part1(x1, i) % MOD * part1(x3, i) % MOD * ncr(x1 + x2 + x3 - (i * 2 - 1), x1 + x3) % MOD
        ans = (ans + term) % MOD
        
    print(ans)

if __name__ == '__main__':
    solve()