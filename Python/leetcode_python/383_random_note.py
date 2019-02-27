class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not magazine and not ransomNote:
            return True
        rec = [0 for _ in range(256)]
        for c in magazine:
            rec[ord(c)] += 1
        for c in ransomNote:
            rec[ord(c)] -= 1
            if rec[ord(c)] < 0:
                return False
        return True
        
