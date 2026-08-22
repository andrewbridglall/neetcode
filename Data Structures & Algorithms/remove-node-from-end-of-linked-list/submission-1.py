# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # init dummy node, ptrs
        dummy = ListNode(-1, head)
        p1 = p2 = dummy
        # move ptr2
        for _ in range(n+1):
            p2 = p2.next
        # traverse list
        while p2:
            p1 = p1.next
            p2 = p2.next
        # p1 next is target
        # remove node
        p1.next = p1.next.next
        # return dummy next
        return dummy.next