"""You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
          # dp[x] = 金額 x を作るために必要な「最小コイン枚数」
        # 最初は「作れない」という意味で全部大きい値にしておく
        INF = 10**9
        dp = [INF] * (amount + 1)
        #0円は0枚で作る
        dp[0] = 0

        for x in range(1,amount +1):
            for c in coins:
                if x - c >= 0:
                     # c を使うと、 (x-c) を作る枚数 + 1 になる
                    dp[x] = min(dp[x], dp[x - c] + 1)

        
        # 最後の dp[amount] が更新されていない（＝INF のまま）
        # つまりその金額は作れなかった → -1
        return dp[amount] if dp[amount] != INF else -1