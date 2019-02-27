class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None or needle is None:
            return -1
        if haystack is not None and needle is not None and len(needle) == 0:
            return 0
        
        h = len(haystack)
        n = len(needle)
        if n > h:
            return -1
        counter = 0
        for i in range(h - n + 1):
            for j in range(n):
                if haystack[i+j] == needle[j]:
                    counter += 1
                else:
                    counter = 0
                    break
            if counter == n:
                return i
        return -1
                
        
