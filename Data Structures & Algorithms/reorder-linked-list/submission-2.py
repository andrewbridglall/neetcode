# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # slow fast ptr to find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # from middle to end reverse linked list
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        head1 = head
        head2 = prev
        while head1 and head2:
            
            n1, n2 = head1.next, head2.next
            
            head1.next = head2
            head2.next = n1


            head1 = n1
            head2 = n2
            