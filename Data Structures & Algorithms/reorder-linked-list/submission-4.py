# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # optimal linear time soln
        
        # init vars
        # calc len linked list
        curr = head
        n = 0
        while curr:
            n +=1
            curr = curr.next
        # traverse to middle of ll and reverse
        middle = n//2
        i = 0
        curr = head
        while curr:
            if i == middle:
                # curr will be start of linked list second half
                break
            curr = curr.next
            i+=1
        # reverse from curr to end
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        # init tail ptrs at first and second half of ll and link
        tail1 = head
        tail2 = prev
        curr = None
        while True:
            # check edge case to end loop
            if curr and curr == tail1:
                curr.next = None
                break
            if curr:
                curr.next = tail1
            next1 = tail1.next
            next2 = tail2.next
            if tail1 == tail2:
                tail1.next = None
                break
            tail1.next = tail2
            curr = tail2
            tail1 = next1
            tail2 = next2
        # when curr == t1 or t1 == t2 set next to None and break