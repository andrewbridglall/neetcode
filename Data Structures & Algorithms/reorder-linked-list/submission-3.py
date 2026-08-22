# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # bf soln
        # init vars
        nodes = []
        # append nodes to list
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        # using two pointers iterate through list and link nodes
        n = len(nodes)
        l, r = 0, n-1
        curr = None
        while True:
            if curr:
                curr.next = nodes[l]
            if l == r:
                nodes[l].next = None
                break
            elif l > r:
                curr.next = None
                break
            nodes[l].next = nodes[r]
            curr = nodes[r]
            l+=1
            r-=1
        # handle even odd length lists and overwrite last node next
        # no return