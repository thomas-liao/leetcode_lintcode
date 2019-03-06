# solution 1, binary search, O(nlogn)
# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
#         if not citations or len(citations) == 0:
#             return 0
        
#         i, j = 0, len(citations) 
        
#         while i + 1 < j:
#             mid = i + (j - i) // 2
#             if self.checkState(citations, mid):
#                 i = mid
#             else:
#                 j = mid
        
#         if self.checkState(citations, j):
#             return j
#         if self.checkState(citations, i):
#             return i
        
#         return 0
        
#     def checkState(self, citations, h):
#         counter = 0
#         for c in citations:
#             if c >= h:
#                 counter += 1
#         if counter >= h:
#             return True
#         return False


     
    
# solution 2, still not very clear how it works
class Solution:
    def hIndex(self, citations):
        if not citations or len(citations) == 0:
            return 0
        citations = sorted(citations)
        l = len(citations)
        for i in range(l):
            if citations[i] >= l - i:
                return l - i
            
        return 0
        
