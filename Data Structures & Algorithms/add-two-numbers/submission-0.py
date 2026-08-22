# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # decode l1 to num
        str1 = ""
        tail1 = l1
        while tail1:
            str1 += str(tail1.val)
            tail1 = tail1.next
        num1 = int("".join(reversed(str1)))

        # decode l2 to num
        str2 = ""
        tail2 = l2
        while tail2:
            str2 += str(tail2.val)
            tail2 = tail2.next
        num2 = int("".join(reversed(str2)))

        # calc sum
        summ = num1+num2
        strRes = reversed(str(summ))
        # build res based on conditions
        dummy = ListNode(-1)
        tail = dummy
        for c in strRes:
            newNode = ListNode(int(c))
            tail.next = newNode
            tail = tail.next
        
        # return res
        return dummy.next