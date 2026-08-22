# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # init vars
        # res
        if not lists:
            return None
        res = lists[0]
        # iterate through lists
        for i in range(1, len(lists)):
            res = self.mergeTwoLists(res, lists[i])
        # merge two linked lists and return res
        # define merge two linked lists
        # feed res into next merge
        # return res
        return res
    
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        while list1:
            tail.next = list1
            list1 = list1.next
            tail = tail.next
        
        while list2:
            tail.next = list2
            list2 = list2.next
            tail = tail.next
        
        return dummy.next
