"""
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(i,path):
            if i == len(nums):
                res.append(path[:])
                return 
            
            #nums[i]を入れない場合
            dfs(i+1,path)
            
            #nums[i]を入れる場合
            path.append(nums[i])
            dfs(i+1,path)
            path.pop()
            
        dfs(0,[])
        return res
    
class Solution:
    def subsets(self, nums:List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        
        for mask in range(1<<n):
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])
            res.append(subset)
        
        return res