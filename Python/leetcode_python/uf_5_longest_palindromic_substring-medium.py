class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or not s[0]:
            return ""
        n = len(s)
        record = [[False for _ in range(n)] for _ in range(n)]
        # k = 1
        max_ = 1
        ret = s[0]
        
        for i in range(n):
            record[i][i] = True
        # k = 2
        for i in range(n - 1):
            if s[i] == s[i+1]:
                record[i][i+1] = True
                max_ = 2
                ret = s[i:i+2]
        
        for k in range(3, n + 1):
            for idx in range(0, n - k + 1):
                if record[idx+1][idx+k-2] and s[idx] == s[idx + k - 1]:
                    record[idx][idx + k - 1] = True
                    max_ = k
                    ret = s[idx:idx+k]
        return ret
