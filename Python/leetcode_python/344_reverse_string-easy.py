class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while (left < right):
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# recursion, doesn't work here because it returns something, not in place
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         if len(s) < 2:
#             return
#         return self.reverseString(s[len(s)//2:]) + self.reverseString(s[:len(s)//2])
