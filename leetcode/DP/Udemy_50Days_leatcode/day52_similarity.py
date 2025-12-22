"""
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.


Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #動的計画法の考え方 + 最小積と最大積を追っていきたいです
        dp_max = nums[0]
        dp_min =  nums[0]
        sofar = nums[0]

        #ここから二番目を追って更新していきたいです
        for i in range(1,len(nums)):
            num = nums[i]
            
            #負の数が来た時のために最大と最小を入れ替える
            if num < 0:
                dp_max,dp_min = dp_min,dp_max 

            dp_max = max(num,dp_max * num)
            dp_min = min(nums,dp_min * num)

            sofar = max(dp_max,sofar)


        return sofar