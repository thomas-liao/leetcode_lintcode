# solution 1, mine, not exactly one pass...
# class Solution:
#     def reverseBetween(self, head, m: int, n: int):
#         if not head or not head.next or m == n:
#             return head

#         dummy = ListNode(0)
#         dummy.next = head
#         runner1 = dummy
#         counter = 0

#         assert m < n
#         while counter < m - 1:
#             runner1 = runner1.next
#             counter += 1
#         runner2 = runner1
#         while counter < n:
#             runner2 = runner2.next
#             counter += 1
#         temp1 = runner1.next  # starting head of list need to be reversed
#         temp2 = runner2.next  # next position of tail of reversed linkedlist
#         # cut
#         runner1.next = runner2.next = None
#         new_head, new_tail = self.reverseAll(temp1)

#         # splice together
#         runner1.next = new_head
#         new_tail.next = temp2
#         return dummy.next

#     def reverseAll(self, head):
#         tail = head
#         prev, cur = None, head
#         while cur:
#             ne = cur.next
#             cur.next = prev
#             prev = cur
#             cur = ne
#         return prev, tail  # new head, new tail


# solution 2, one pass
# class Solution:
#     def reverseBetween(self, head, m: int, n: int):
#         if not head or not head.next or m == n:
#             return head
#         dummy = ListNode(0)
#         dummy.next = head
#         counter = 0
#         runner = dummy
        
#         for i in range(m-1):
#             runner = runner.next
            
#         new_tail = runner.next
#         prev, cur = None, runner.next
#         ne = None # important
        
#         # for i in range(n - m): # wrong... reverse time = n - m + 1, miss-counted new_tail - > None
#         for i in range(n - m + 1):
#             ne = cur.next
#             cur.next = prev
#             prev = cur
#             cur = ne
            
#         new_head = prev
#         new_tail.next = ne # important
#         runner.next = new_head
#         return dummy.next
