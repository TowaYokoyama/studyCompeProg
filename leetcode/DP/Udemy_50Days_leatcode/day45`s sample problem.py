class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        if n == 1:
            return nums[0]

        # 線形（直線上）の場合の通常の House Robber DP
        def rob_linear(arr):
            if not arr:
                return 0
            if len(arr) == 1:
                return arr[0]
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
            return dp[-1]

        # --- ここが「先頭と末尾を一緒に取れない」部分 ---
        # 先頭を含める場合 → 末尾は除外
        # 末尾を含める場合 → 先頭は除外
        # → 2通りを比べて大きい方を取る
        return max(
            rob_linear(nums[:-1]),  # 末尾を除いたケース
            rob_linear(nums[1:])    # 先頭を除いたケース
        )
