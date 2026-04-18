def lcs_length(str1, str2):
    m, n = len(str1), len(str2)
    # dpテーブルの初期化（全て0）
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # dpテーブルの更新
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

def lcs(str1, str2):
    # 最長共通部分列の実際の文字列を復元する
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # dpテーブルを構築
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]

    # LCSを復元
    lcs_seq = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs_seq.append(str1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs_seq))

# 使用例
str1 = "AGGTAB"
str2 = "GXTXAYB"
print("LCSの長さ:", lcs_length(str1, str2))  # -> 4
print("LCS:", lcs(str1, str2))               # -> "GTAB"