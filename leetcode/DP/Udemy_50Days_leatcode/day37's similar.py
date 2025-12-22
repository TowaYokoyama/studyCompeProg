"""
rootバイナリ ツリーのが与えられた場合、そのノードの値の順序どおりのトラバーサルを返します。
例1:

入力: root = [1,null,2,3]

出力: [1,3,2]

説明：

例2:

入力: root = [1,2,3,4,5,null,8,null,null,6,7,9]

出力: [4,2,6,5,7,1,3,9,8]

説明：

例3:

入力: root = []

出力: []

例4:

入力: root = [1]

出力: [1]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []      # 出力するリスト
        stack = []       # 未処理のノードを入れておく
        current = root   # 現在のノード

        while current or stack:
            # 左へ行けるだけ進む
            while current:
                stack.append(current)
                current = current.left

            # 左がもうない → スタックから戻って「自分」を処理
            current = stack.pop()
            result.append(current.val)

            # 右の子を探索
            current = current.right

        return result