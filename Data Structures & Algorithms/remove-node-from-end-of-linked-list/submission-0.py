# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get len
        length = 0
        curr = head
        while curr:
            length+=1
            curr = curr.next
        # edge case -remove head
        if length == n:
            return head.next
        # iterate to prev
        prev = head
        i = 0
        while i < length-n-1:
            prev = prev.next
            i+=1
        curr = prev.next
        next = curr.next
        
        # remove nth - curr
        prev.next = next
        # return head
        return head