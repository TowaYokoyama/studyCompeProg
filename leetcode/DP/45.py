"""
長さ の整数の0から始まる配列が与えられます。初期位置はインデックス0です。numsn

各要素は、nums[i]インデックス から前方にジャンプできる最大距離を表しますi。つまり、インデックス にいる場合i、以下の条件を満たす任意のインデックスにジャンプできます(i + j) 。

0 <= j <= nums[i]そして
i + j < n
インデックス に到達するための最小ジャンプ回数を返しますn - 1。テストケースは、インデックス に到達できるように生成されます n - 1。

例1:

入力: nums = [2,3,1,1,4]
出力: 2
説明:最後のインデックスに到達するための最小ジャンプ数は 2 です。インデックス 0 から 1 に 1 ステップジャンプし、次に最後のインデックスまで 3 ステップジャンプします。
例2:

入力: nums = [2,3,0,1,4]
出力: 2
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        farthest = 0
        current_end = 0
        #最後の要素についたらジャンプ不要なので、n-1まで
        for i in range(len(nums)-1):
            #iから飛べる最も遠い位置を更新
            farthest = max(farthest, i+nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps

