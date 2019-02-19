class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        self.quickSort(A, 0, len(A) - 1)
        
    def quickSort(self, A, left, right):
        if right > left: // otherwise maximum recursion exceed
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

