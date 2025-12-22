"""
02. Binary Tree Level Order Traversal
Medium
Topics
premium lock icon
Companies
Hint
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 
"""

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []  # 空の木なら空リストを返す

        result = []
        queue = deque([root])  # BFS用キュー（最初はrootだけ）

        while queue:
            level = []  # 現在のレベルのノード値を格納
            for _ in range(len(queue)):  # この時点のqueueのサイズが、そのレベルのノード数
                node = queue.popleft()
                level.append(node.val)

                # 左右の子を次のレベルのためにキューへ追加
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)  # 現レベルが終わったら結果に追加

        return result