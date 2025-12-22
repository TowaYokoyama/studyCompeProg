"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
"""

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')  # 全体の最大値をグローバルに記録

        def dfs(node):
            if not node:
                return 0

            # 左右の枝から得られる「片側の最大和」を再帰的に計算
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # 「このノードを経由したときの最大経路和」を候補にする
            current_sum = node.val + left + right
            self.max_sum = max(self.max_sum, current_sum)

            # 親に返すのは「片方の枝を使った場合の最大和」
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum
