"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
"""
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # ヒープを用意
        heap = []
        
        # 各リストの先頭ノードをヒープに追加
        # (値, インデックス, ノード) のタプルをpushする
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        current = dummy
        
        while heap:
            # 最小値をもつノードを取り出す
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            
            # そのノードの次があればヒープに追加
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next
