"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
最初は左⇒右
その次は左←右
"""


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])#bfsキュー　最初はrootだけにする
        
        
        left_to_right = True #最初は左から右へ
        while queue:
            Level = [] #現在のレベルのノード値を格納
            for _ in range(len(queue)):
                node = queue.popleft()
                Level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            if not left_to_right:
                Level.reverse() #右から左のターン(偶数回)は反転
                
            result.append(Level)
            left_to_right = not left_to_right #次のターンは逆方法
        
        return result