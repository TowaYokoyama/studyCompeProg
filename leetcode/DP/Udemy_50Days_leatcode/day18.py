class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """
        Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
        """
        #O(n*4)でばちくそおそい
        count = 0
        for a in nums1:
            for b in nums2:
                for c in nums3:
                    for d in nums4:
                        if a + b + c + d == 0:
                            count +=1
        return count
    
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum12 = {}
        for a in nums1:
            for b in nums2:
                s = a + b 
                sum12[s] = sum12.get(s,0) + 1 #「キー s がまだ無いなら0を返す」
        count = 0
        for c in nums3:
            for d in nums4:
                t = -(c+d)
                if t in sum12:
                    count += sum12[t]
        return count