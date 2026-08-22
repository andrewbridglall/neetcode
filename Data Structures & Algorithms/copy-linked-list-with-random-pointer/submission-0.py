"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # init vars
        tail1 = head

        dummy = Node(-1)
        tail2 = dummy
        new = {}
        # create linked list without random
        while tail1:
            # create new node at tail1
            node = Node(tail1.val)
            # store new node in map
            new[tail1] = node
            # link new node to new list
            tail2.next = node
            tail2 = tail2.next

            tail1 = tail1.next
        # create random ptr linkages
        tail1 = head
        tail2 = dummy.next
        
        while tail1:
            # tail1 and tail2 map to old - new pair
            # set tail2 random ptr
            if tail1.random:
                newrand = new[tail1.random]
                tail2.random = newrand

            tail1 = tail1.next
            tail2 = tail2.next
        
        return dummy.next

