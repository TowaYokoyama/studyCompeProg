"""
Example 1:

Input: nums = [3,0,1]

Output: 2

Explanation:

n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:

Input: nums = [0,1]

Output: 2

Explanation:

n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]

Output: 8

Explanation:

n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

"""

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length_list = len(nums)
        # 1. リストをソートする (二分探索の必須条件)
        sorted_list = sorted(nums)
        
        # 2. 探索範囲の設定
        # left: 配列の開始インデックス
        # right: 配列の終了インデックス (最後の要素)
        left, right = 0, length_list - 1 
        
        # 欠落した数字のインデックスを保持する変数 (初期値として n を設定)
        # 欠落が配列の末尾の場合 (例: [0, 1] で 2 が欠落) に対応するため
        missing_index = length_list 
        
        while left <= right:
            # 3. 中央値の計算 (整数除算 // を使用)
            # Pythonの // は小数点以下を切り捨てるため、(left + right) // 2 が正しい
            mid = (left + right) // 2 
            
            # 4. 欠落箇所のチェック
            # インデックス mid の実際の値が、期待される値 (mid) よりも大きい場合、
            # mid の値かそれより左側で欠落が発生している
            if sorted_list[mid] > mid:
                # mid の値が欠落候補。結果を一旦保持し、さらに左側 (小さいインデックス) を探す
                missing_index = mid
                right = mid - 1
            else:
                # sorted_list[mid] <= mid の場合 (値がインデックスと一致または小さい場合)
                # 欠落は mid より右側 (大きいインデックス) にある
                left = mid + 1
        
        # ループ終了後、missing_index が欠落した数字 (0からnの範囲の数) のインデックスを示す
        return missing_index
        