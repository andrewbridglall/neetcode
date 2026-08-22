# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for node in lists:
            curr = node
            while curr:
                arr.append(curr)
                curr = curr.next
        
        arr.sort(key=lambda x: x.val)
        
        if len(arr):
            i=0
            while i+1 < len(arr):
                arr[i].next = arr[i+1]
                i+=1
            arr[-1].next = None
        
        return arr[0] if len(arr) else None