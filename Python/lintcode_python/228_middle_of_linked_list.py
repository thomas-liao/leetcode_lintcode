"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middleNode(self, head):
        # write your code here
        if head is None or head.next is None:
            return head
        
        slow = head;
        fast = head.next;
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow
