# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        
        dummy = ListNode(None)
        dummy.next = head
        
        prev = None
        slow = dummy
        fast = dummy
        # for _ in range(n): # @ wrong
        for _ in range(n-1):
        
            fast = fast.next
            
        while fast.next:
            prev = slow
            fast = fast.next
            slow = slow.next
        # remove slow
        prev.next = slow.next
        slow.next = None
        
        return dummy.next
