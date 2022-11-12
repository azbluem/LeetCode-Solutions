# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        if node==None or node.next==None:
            return node
        future = node.next
        node.next = node.next.next
        future.next = node
        node.next = self.swapPairs(node.next)
        return future