MOD = 998244353

N = int(input())
a = list(map(int, input().split()))

ans = 0

for i in range(1, N + 1):
    # dp[j][k][l]
    # j: 先頭から j 個見た
    # k: その中から k 個選んだ
    # l: 選んだ数の和 mod i
    dp = [[[0] * i for _ in range(i + 1)] for __ in range(N + 1)]
    
    dp[0][0][0] = 1

    for j in range(N):
        for k in range(i + 1):
            for l in range(i):
                val = dp[j][k][l]
                if val == 0:
                    continue

                # a[j] を選ばない
                dp[j + 1][k][l] = (dp[j + 1][k][l] + val) % MOD

                # a[j] を選ぶ
                if k != i:
                    nl = (l + a[j]) % i
                    dp[j + 1][k + 1][nl] = (dp[j + 1][k + 1][nl] + val) % MOD

    ans = (ans + dp[N][i][0]) % MOD

print(ans)
