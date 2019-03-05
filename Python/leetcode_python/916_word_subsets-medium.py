# Solution 1my solution.. using Counter
from collections import Counter
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        # corner cases
        if not A:
            return []
        if not B:
            return A
        
        union = Counter(B[0])
        for i in range(1, len(B)):
            union |= Counter(B[i]) # important here
        

        res = []
        for word in A:
            check = union - Counter(word) # important here
            if len(check.keys()) == 0: # important here
                res.append(word)
        return res
            
# Solution2, same idea but more advanced
from collections import Counter
from functools import reduce
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        union = reduce(operator.ior, map(Counter, B))
        return [a for a in A if Counter(a) & union == union]
