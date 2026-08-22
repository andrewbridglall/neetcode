# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get middle of list
        s = head
        f = head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        
        # s will be first middle node
        # s.next is first node of second half
        second = s.next
        s.next = None
        # reverse second half of ll
        prev, curr = None, second 
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        # set l r ptrs to ends and reorder list
        # prev is new head of second half and is shorter than first

        l,r = head, prev
        while r:
            lnext = l.next
            rnext = r.next
            l.next = r
            r.next = lnext

            l = lnext
            r = rnext