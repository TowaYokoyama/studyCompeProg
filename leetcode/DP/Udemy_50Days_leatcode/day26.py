"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.
Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
"""
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head 
         
        current = head #現在の奇数ノード
        even_num = head.next #偶数ノードの開始
        even_head = head.next  #偶数リストの先頭を保持
        
        while even_num and even_num.next: #偶数ノードとその次のノードが存在する限りループする
            current.next = even_num.next #奇数ノードの次を更新
            current = current.next #奇数ノードを進める
            even_num.next = current.next #偶数ノードの次を進める
            even_num = even_num.next #偶数ノードを次に進める
        
        current.next = even_head #奇数リストの末尾に偶数リストを接続
        return head
            