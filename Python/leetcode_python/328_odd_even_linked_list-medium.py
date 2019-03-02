# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# solution 1, my own version, kind of ugly
# class Solution:
#     def oddEvenList(self, head: ListNode) -> ListNode:
#         if not head or not head.next or not head.next.next:
#             return head
#         ret = head
#         n1 = head # for odd nodes
#         n2 = head.next # for even ndoes
#         n2_head = n2
#         n1_tail = n1
#         while n1 and n1.next:
#             temp_n1 = n1.next.next
#             temp_n2 = n2.next.next if n2 and n2.next else None
#             n1.next = temp_n1
#             if temp_n1:
#                 n1_tail = temp_n1
#             n2.next = temp_n2
#             n1 = temp_n1
#             n2 = temp_n2
#         n1_tail.next = n2_head
#         return head

    
    
# solution 2, notice: if we modify odd - > odd.next.next doesn't effect even - > even.next.next
# also, subtly, if we examine while (even and even.next) instead lf while (odd and odd.next), we do # not need to  assign a new variable to store odd tail

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head
        even_stored = head.next
        odd, even = head, head.next
        
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
            
        odd.next = even_stored
        return head
