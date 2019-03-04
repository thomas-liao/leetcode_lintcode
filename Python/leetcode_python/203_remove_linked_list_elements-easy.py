# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        cur = head
        
        while(cur):
            if cur.val == val:
                # delete
                prev.next = cur.next
                cur.next = None
                cur = prev.next
            else:
                prev = prev.next
                cur = cur.next
                
        return dummy.next
