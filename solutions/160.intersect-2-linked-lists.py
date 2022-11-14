# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1=headA
        l2=headB
        listA=set()
        while l1!=None:
            listA.add(id(l1))
            l1=l1.next
        intersectId=0
        while l2!=None:
            if id(l2) in listA:
                intersectId=id(l2)
                return l2
            else:
                l2=l2.next
        return None
        """while l2!=None:
            listB.append(id(l2))
            l2=l2.next"""
        """goNext=listA.index(intersectId)
        mergedNode=headA
        for lp in range(0,goNext):
            mergedNode=mergedNode.next
            print(mergedNode.val)
        return mergedNode"""
        
        