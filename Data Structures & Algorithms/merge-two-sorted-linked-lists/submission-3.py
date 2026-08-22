# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create dummy node and tail ptr
        dummy = ListNode(-1)
        tail = dummy
        # while both lists non null
        while list1 and list2:
            if list1.val <= list2.val:
                # choose list1 and update list1 ptr
                tail.next = list1
                list1 = list1.next

            else:
                # choose list2 and update ptr
                tail.next = list2
                list2 = list2.next
            # update tail 
            tail = tail.next
        # ...

        # one list oob
        # while list1
        while list1:
            tail.next = list1
            list1 = list1.next
            tail = tail.next
        
        # while list2
        while list2:
            tail.next = list2
            list2 = list2.next
            tail = tail.next

        # return dummy next
        return dummy.next