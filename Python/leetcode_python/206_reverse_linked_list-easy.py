# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1, recursion.. kind of ugly, my own version
# class Solution:
#     startNode = None
#     def reverseList(self, head: ListNode) -> ListNode:
#         if head is None or head.next is None:
#             return head
#         self.helper(head)
#         return self.startNode
    
#     def helper(self, head):
#         if head.next is None:
#             self.startNode = head
#             return head
#         ne = self.helper(head.next)
#         ne.next = head
#         head.next = None # missing this , memory limit exceed
#         return head


        



# # solution 2, iterative
# iterative
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if not head:
#             return head
#         prev, cur = None, head
#         # #@ buggy.. before you do the reverse(i.e. cur.next = prev) you need to store its next first
#         # otherwise this information got lost in later stage
#         # while cur:
#         #     cur.next = prev
#         #     prev = cur
#         #     cur = cur.next
#         # return prev #
        
#         while cur:
#             # store next
#             ne = cur.next
#             cur.next = prev
#             prev = cur
#             cur = ne
#         return prev
    
        

# solution 3, iterative - pythonic
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:   
#         if not head or not head.next:
#             return head
#         prev, cur = None, head
#         while cur:
#             cur.next, prev, cur = prev, cur, cur.next
#         return prev
