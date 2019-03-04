# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# method 1, keep tracking of unique element and connect them into a list
# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         # missed corner case
#         if not head or not head.next:
#             return head
#         dummy = ListNode(float('inf'))
#         dummy.next = head 
#         prev = dummy
#         cur = head
        
#         while cur and cur.next:
#             # if cur.val == cur.next.val: @ wrong!
#             # while cur.val == cur.next.val: @ wrong!
#             while cur and cur.next and cur.val == cur.next.val:
#                 cur = cur.next
#             prev.next = cur
#             # missing this one
#             prev = cur
#             cur = cur.next
#         return dummy.next


# solution 2:

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:    
        if not head or not head.next:
            return head
        first, second = head, head.next
        while second:
            if second.val == first.val:
                # remove node
                first.next = second.next
                second = second.next
            else:
                # moving forward together
                first = first.next
                second = second.next
        return head
