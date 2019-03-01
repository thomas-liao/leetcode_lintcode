# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# solution 1, my own version, kind of ugly...
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#         return self.recursionSwap(head, head.next)
        
#     def recursionSwap(self, node1, node2):
#         if not node1 and not node2:
#             return None
#         if node1 and not node2:
#             return node1
#         # node1 and node2:
#         ne = node2.next
#         node2.next = node1
#         node1.next = None
        
#         # be very careful about ne is None or ne.next is None situations!!!
#         if ne and ne.next:
#             node1.next = self.recursionSwap(ne, ne.next)
#         elif ne and not ne.next:
#             node1.next = self.recursionSwap(ne, None)
#         # elif not ne and not ne.next: #@ bug
#         elif not ne: 
#             node1.next = None
#         return node2

# solution2, single-variable recursion, cleaner
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#         return self.recursionSwap(head)
    
#     def recursionSwap(self, head):
#         if not head or not head.next:
#             return head
#         ret = head.next
#         temp = head.next.next
#         ne = head.next
#         ne.next = head
#         head.next = self.recursionSwap(temp)
#         return ret
   
    
# solution 3  
# more concise recursion approach
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#         ne = head.next
#         # ne.next = head # #@ error, no, blocked path
#         # head.next = self.swapPairs(head.next.next)
#         ## modification one
#         ## temp = head.next.next
#         ## ne.next = head
#         ## head.next = self.swapPairs(temp)
        
#         ## or
#         head.next = self.swapPairs(head.next.next)
#         ne.next = head
#         return ne
      
    
    
# solution 4
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        node1, node2 = head, head.next
        p = dummy
        while node1 and node2:
