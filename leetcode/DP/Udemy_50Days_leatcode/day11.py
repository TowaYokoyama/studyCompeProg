from typing import List
#xor 排他的論理和
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            res ^= x
        return res

#カウントしてく

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        counts = {}  # 数字ごとの出現回数を記録する辞書
        for x in nums:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1
        
        # 出現回数が1のものを探す
        for num, count in counts.items():
            if count == 1:
                return num
