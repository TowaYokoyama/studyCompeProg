"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # dp[i][j]: word1 の先頭 i 文字 → word2 の先頭 j 文字に変換する最小操作数
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 初期化：空文字にするまで全部削除 / 空文字から全部挿入
        for i in range(m + 1):
            dp[i][0] = i  
        for j in range(n + 1):
            dp[0][j] = j  

        # DPテーブルを埋める
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if word1[i - 1] == word2[j - 1]:
                    # 文字が同じなら操作なし
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 1 + (削除 / 挿入 / 置換 の最小)
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],    # 削除
                        dp[i][j - 1],    # 挿入
                        dp[i - 1][j - 1] # 置換
                    )

        return dp[m][n]
