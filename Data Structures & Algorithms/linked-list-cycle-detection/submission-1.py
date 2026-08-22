# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # init var
        path = set()
        # iterate thru ll
        while head:
        # if curr in path return true
            if head in path:
                return True
            path.add(head)
            head = head.next
        # default ret false
        return False