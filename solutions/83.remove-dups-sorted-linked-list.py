class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        
        tval=head.val
        tnode=head

        while tnode!=None:    
            if tnode.next!=None and tnode.next.val==tval :
                tnode.next=tnode.next.next
            elif tnode.next==None:
                tnode=None
            else:
                tval=tnode.next.val
                tnode=tnode.next
        return head