
# # merge sort

# class Solution:
#     """
#     @param A: an integer array
#     @return: nothing
#     """

#     def sortIntegers2(self, A):
#         self.mergeSort(A, 0, len(A) - 1)
#         return A

#     def mergeSort(self, A, left, right):
#         if left >= right:
#             return A
#         if left == right - 1:
#             if A[left] > A[right]:
#                 A[left], A[right] = A[right], A[left]
#             return
#         partition = (left + right) // 2
#         self.mergeSort(A, left, partition)
#         self.mergeSort(A, partition + 1, right)
#         self.merge(A, left, right, partition)
#         return

#     def merge(self, A, left, right, partition):
#         if left >= right:
#             return
#         temp = [0 for _ in range(right-left+1)]
#         A_left = A[left:partition + 1]
#         A_right = A[partition + 1:right+1]

#         idx = l_idx = r_idx = 0
#         while l_idx < len(A_left) and r_idx < len(A_right):
#             if A_left[l_idx] < A_right[r_idx]:
#                 temp[idx] = A_left[l_idx]
#                 l_idx += 1
#             else:
#                 temp[idx] = A_right[r_idx]
#                 r_idx += 1
#             idx += 1

#         if l_idx < len(A_left):
#             # temp.extend(A_left[l_idx:len(A_left)]) # bug
#             temp[idx:] = A_left[l_idx:len(A_left)]
#         else:
#             temp[idx:] = A_right[r_idx:len(A_right)]

#         A[left:right + 1] = temp
#         return




# Solution 1, merge sort
# class Solution:
#     """
#     @param A: an integer array
#     @return: nothing
#     """
#     def sortIntegers2(self, A):
#         if not A:
#             return
#         self.mergeSort(A, 0, len(A) - 1)
        
#     def mergeSort(self, A, left, right):
#         if left < right:
#             mid = (left + right) // 2
#             self.mergeSort(A, left, mid)
#             self.mergeSort(A, mid + 1, right)
#             self.merge(A, left, right, mid)
        
#     def merge(self, A, left, right, mid):
#         if left < right:
#             i, j = left, mid + 1
#             k = 0
#             temp = [0 for _ in range(right - left + 1)]
            
#             while i <= mid and j <= right:
#                 if A[i] < A[j]:
#                     temp[k] = A[i]
#                     i += 1
#                 else:
#                     temp[k] = A[j]
#                     j += 1
#                 k += 1
            
#             while i <= mid:
#                 temp[k] = A[i]
#                 i += 1
#                 k += 1
            
#             while j <= right:
#                 temp[k] = A[j]
#                 j += 1
#                 k += 1
#             for i in range(right - left + 1):
#                 A[i+left] = temp[i]
                
            
        
        
# Solution 2, quick sort
class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        self.quickSort(A, 0, len(A) - 1)
        
    def quickSort(self, A, left, right):
        if right > left: # otherwise maximum recursion exceed
            p = self.partition(A, left, right, (left + right) // 2)
            self.quickSort(A, left, p - 1)
            self.quickSort(A, p + 1, right)

    def partition(self, A, left, right, pivot):
        p_val = A[pivot]
        A[right], A[pivot] = A[pivot], A[right]
        
        idx = left
        # for i in range(left, right - 1) @ wrong
        for i in range(left, right):
            if A[i] < p_val:
                A[idx], A[i] = A[i], A[idx]
                idx += 1
        A[idx], A[right] = A[right], A[idx]
        return idx
