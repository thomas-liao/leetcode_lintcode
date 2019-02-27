class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        rec = [0 for _ in range(256)]
        for c in s:
            rec[ord(c)] += 1
        for i in range(len(s)):
            c = s[i]
            if rec[ord(c)] == 1:
                return i
        return -1
        
        
