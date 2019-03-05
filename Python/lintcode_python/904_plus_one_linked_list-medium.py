"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the first Node
    @return: the answer after plus one
    """
    def plusOne(self, head):
        # Write your code here
        if not head:
            return ListNode(1)
            
        carry = self.helper(head)
        if carry:
            dummy = ListNode(1)
            dummy.next = head
            return dummy
        return head

    def helper(self, head):
        # base cases
        if not head.next:
            if head.val == 9:
                head.val = 0
                return True # True: carry 1, False: no carry
            head.val = head.val + 1
            return False
            
        carry = self.helper(head.next)
        
        if not carry:
            return False
        # has carry
        if head.val == 9:
            head.val = 0
            return True
        head.val = head.val + 1
        return False
