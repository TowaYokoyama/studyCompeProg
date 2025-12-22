# Definition for a binary tree node.
"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
「inorder traversal」
"""
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [] #ノードを一時的に保存するスタック
        
        current = root #現在のたんさくいちを表すポインタ 
        count = 0  #何個目のノードをみたかカウント
        
        while stack or current: #stackが空でもcurrentがまだある限り探索すする
            #左の子をたどればたどれるだけたどる
            while current:#bstでは左に行けば行くだけ小さい値なので、左を優先
                stack.append(current)#今ノードをstackに保存
                current = current.left#さらに左へ進む
                
            #左端まで行ったら、stackの一番上を取り出す
            #左の子がもうない=一番小さいノードに淘汰値    
            current = stack.pop() #左端のノードを処理する
            count += 1 #ノードを1つ処理したので、カウントを一つ進める
            if count == k: #k個目のノードが答え
                return current.val #中旬でk番目の値
            current = current.right #次に右部分木の右部分を処理していく
                
        