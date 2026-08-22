# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # init arr
        arr = []
        # build arr
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next
        # build new ll
        head = tail = ListNode(-1)
        l, r = 0, len(arr)-1
        while l <= r:
            tail.next = arr[l]
            arr[l].next = arr[r]
            tail = arr[r]
            l+=1
            r-=1
        tail.next = None
        

