# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return_head=ListNode((l1.val+l2.val)%10,None)
        head = return_head
        remainder = (l1.val+l2.val)//10
        l1=l1.next
        l2=l2.next
        while l1!=None and l2!=None:
            next_node=ListNode((l1.val+l2.val+remainder)%10,None)
            remainder = (l1.val+l2.val+remainder)//10
            return_head.next = next_node
            return_head = next_node
            next_node = return_head.next
            l1=l1.next
            l2=l2.next
        if l1==None:
            while l2!=None:
                next_node = ListNode((l2.val+remainder)%10,None)
                remainder = (l2.val+remainder)//10
                return_head.next = next_node
                return_head = next_node
                l2=l2.next
        if l2==None:
            while l1!=None:
                next_node = ListNode((l1.val+remainder)%10,None)
                remainder = (l1.val+remainder)//10
                return_head.next = next_node
                return_head = next_node
                l1=l1.next
        if remainder:
            return_head.next = ListNode(remainder,None)
        return head
