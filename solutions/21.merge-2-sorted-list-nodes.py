# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=None
        current=None
        l1=list1
        l2=list2
        if l1==None:
            return l2
        elif l2==None:
            return l1
        elif l1.val<l2.val:
            head=l1
            l1=l1.next
        else:
            head=l2
            l2=l2.next
        current=head
        while l1!=None and l2!=None:
            if l1.val<l2.val:
                current.next=l1
                current=current.next
                l1=l1.next
            else:
                current.next=l2
                current=current.next
                l2=l2.next
        if l1==None:
            current.next=l2
        else:
            current.next=l1
        return head
        
        """l1=list1
        l2=list2
        if l1==None:
            return l2
        elif l2==None:
            return l1
        elif l1.val<l2.val:
            return ListNode(l1.val,self.mergeTwoLists(l1.next,l2))
        else:
            return ListNode(l2.val,self.mergeTwoLists(l2.next,l1))"""
        