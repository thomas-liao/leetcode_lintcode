class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        pattern = list(pattern)
        str = str.split()
        # @error, missed this causing bug
        if len(pattern) != len(str):
            return False
        # zip will not continue if length are different        
        return len(set(zip(pattern, str))) == len(set(pattern)) == len(set(str))
        
