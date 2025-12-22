class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        217. 重複が含まれています
    整数配列が与えられた場合nums、配列内にtrueいずれかの値が少なくとも 2 回false出現する場合は を返し、すべての要素が異なる場合は を返します。
    例1:
入力: nums = [1,2,3,1]
出力: true
説明：
要素 1 はインデックス 0 と 3 に出現します
例2:
入力: nums = [1,2,3,4]
出力: false
説明：
すべての要素は異なります。
例3:
入力: nums = [1,1,1,3,3,4,3,2,4,2]
出力: true
制約:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
        """
        set_nums = set(nums)
        if len(set_nums) == len(nums):
            return False 
        else:return True
        
             