# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # merge k lists -> k/2 -> k/4 -> ... -> 1
        def mergeTwoLists(l1, l2):
            dummy = ListNode()
            node = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next
                node = node.next
            
            node.next = l1 or l2

            return dummy.next
        
        while len(lists) > 1:
            currlists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                currlists.append(mergeTwoLists(l1, l2))
            lists = currlists
        
        return lists[0] if len(lists) else None
        
