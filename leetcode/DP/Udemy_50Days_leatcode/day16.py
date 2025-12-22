class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Example 1:
Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109     more than  ⌊n / 2⌋ time >=であればいいんじゃ
        """
        
        seen = {}
        for num, count in enumerate(nums):
            if num in seen:
                seen[num] +=1 
            else:
                seen[num] = 1
                
        n = len(nums)
        for num,count in seen.items():
            if count > n //2:
                return num  
            
            
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

        
        
        
        