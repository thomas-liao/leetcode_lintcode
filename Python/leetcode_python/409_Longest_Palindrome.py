class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        rec = [0 for _ in range(256)]
        for c in s:
            # note: it is ord() instead of ord[], ord is a function call!!
            rec[ord(c)] += 1
        odd_flag = False
        
        res = 0
        for r in rec:
            if r == 0:
                continue
            if not odd_flag and r % 2 == 1:
                odd_flag = True
            res += 2 * (r // 2)
        if odd_flag:
            res += 1
        return res
        
