# # prac 1
# class Solution(object):
#     def combinationSum3(self, k, n):
#         """
#         :type k: int
#         :type n: int
#         :rtype: List[List[int]]
#         """
#         result = set()
#         self.recursion(k, n, 1, 0, 0, [], result)
#         return list(result)

#     def recursion(self, k, n, start, count, sum_, subset, result):
#         # truncation
#         # bug, cannot put it here, missing chances to find result
#         # if start == 10:
#         #     return
#         if count > k or sum_ > n:
#             return
#         if count == k and sum_ == n:
#             result.add(tuple(sorted(subset)))
#             return
        
#         if start == 10: # ~put it here instead
#             return
#         for i in range(start, 10):
#             subset.append(i)
#             sum_ += i
#             count += 1
#             self.recursion(k, n, i + 1, count, sum_, subset, result)
#             subset.pop()
#             sum_ -= i # cannot miss this one.... 
#             count -= 1 # cannot miss this one... it is not end, the for loop is executing!!!



# prac 2
class Solution(object):
    def combinationSum3(self, k, n):
        result = set()
        self.recursion(k, n, 0, 1, [], result)
        # return result #@ wrong
        # return sorted(list(result))
        # or
        return list(result)
        
    
    def recursion(self, k, n, sum_, start, subset, result):
        if len(subset) > k or sum_ > n:
            return
        if len(subset) == k:
            if sum_ == n:
                result.add(tuple(sorted(subset)))
            return
        for i in range(start, 10):
            subset.append(i)
            sum_ += i
            self.recursion(k, n, sum_, i + 1, subset, result)
            subset.pop()
            sum_ -= i
