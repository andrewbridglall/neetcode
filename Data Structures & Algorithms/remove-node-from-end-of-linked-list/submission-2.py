# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # main case

        # get size of ll
        sz = 0
        curr = head
        while curr:
            sz +=1
            curr = curr.next
        
        # handle edge cases
        # if rm head
        if sz == n:
            return head.next
        
        # iterate to prev
        prev = head
        for i in range(1, sz-n):
            prev = prev.next
        # remove
        prev.next = prev.next.next
        # return head
        return head