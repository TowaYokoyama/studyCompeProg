#例1:

#入力: nums = [5,7,7,8,8,10]、target = 8
#例2:

#入力: nums = [5,7,7,8,8,10]、target = 6
#例3:

#入力: nums = [], target = 0
#出力: [-1,-1]
 
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left,right = -1,-1 #見つからないときの処理
        #左から右にleft探す
        for i in range(len(nums)):
            if nums[i] == target:
                 left = i #indexが知りたい
                 break #1回だけでいいから
         
        reversed_nums = nums[::-1]      
        for j in range(len(reversed_nums)):
            if reversed_nums[j] == target:
                right = len(reversed_nums) -1 -j
                break #重複除く
                
        return(left,right)
                