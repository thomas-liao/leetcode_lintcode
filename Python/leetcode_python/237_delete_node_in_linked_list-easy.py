# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # in case it is a tail
        prev = None
        while node and node.next:
            prev = node
            node.val = node.next.val
            node = node.next
        # error: you cannot delete last node simply by
        # setting last_node = None, that doesn't work
        # you want to delete, you have to prev.next = None
        
