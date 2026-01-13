"""
配列 nums が与えられます。
インデックス left から right まで（両端含む）の
要素の合計を求めてください。
次のクラスを実装してください：
NumArray(int[] nums)
→ 配列 nums を使ってオブジェクトを初期化する
sumRange(int left, int right)
→ nums[left] + nums[left+1] + ... + nums[right] を返す
※ sumRange は 何度も呼ばれる
Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

"""
class NumArray:

    def __init__(self, nums: List[int]):
        # 累積和を作る（前計算）
        self.prefix = [0]
        for x in nums:
            self.prefix.append(self.prefix[-1] + x)

    def sumRange(self, left: int, right: int) -> int:
        # 区間和を O(1) で返す
        return self.prefix[right + 1] - self.prefix[left]
