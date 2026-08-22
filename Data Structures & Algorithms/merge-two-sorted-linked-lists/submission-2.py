# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create result head node to build list
        head = ListNode(-1)
        k = head
        p1, p2 = list1, list2
        while p1 and p2:
            # compare and choose smaller val
            newNode = None
            if p1.val < p2.val:
                newNode = ListNode(p1.val)
                p1 = p1.next
            else:
                newNode = ListNode(p2.val)
                p2 = p2.next

            k.next = newNode
            k = k.next

        if p1:
            k.next = p1
        else:
            
            k.next = p2
        return head.next