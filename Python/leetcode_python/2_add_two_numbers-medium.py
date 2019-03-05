# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stored_dummy = ListNode(None)
        dummy = stored_dummy
        runner1, runner2 = l1, l2
        
        carry = False
        while runner1 or runner2:
            digit = (runner1.val if runner1 else 0) + (runner2.val if runner2 else 0) + carry
            if digit > 9:
                carry = True
                digit = digit % 10
            else:
                carry = False
            dummy.next = ListNode(digit)
            dummy = dummy.next
            if runner1:
                runner1 = runner1.next
            if runner2:
                runner2 = runner2.next
        
        if carry:
            dummy.next = ListNode(1)
        return stored_dummy.next
