from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find(is_left):
            l, r, ans = 0, len(nums)-1, -1
            while l <= r:
                m = (l+r)//2
                if nums[m] > target or (is_left and nums[m] == target):
                    r = m-1
                else:
                    l = m+1
                if nums[m] == target: ans = m
            return ans
        return [find(True), find(False)]
