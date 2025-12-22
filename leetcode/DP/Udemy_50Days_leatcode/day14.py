"""

例1:

入力: nums = [2,7,11,15]、target = 9
出力: [0,1]
説明: nums[0] + nums[1] == 9 なので、[0, 1] を返します。
例2:

入力: nums = [3,2,4]、target = 6
出力: [1,2]
例3:

入力: nums = [3,3]、target = 6
出力: [0,1]
 
制約:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
有効な回答は 1 つだけ存在します。
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] + nums[i] == target:
                    return(i,j)
                
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            seen = {}
            for i, num in enumerate(nums): 
                complement = target - num
                if complement in seen:
                    return [seen[complement], i]
                seen[num] = i
                
                
