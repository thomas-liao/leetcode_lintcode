# # doesn't work!!
# e.g. input:
# "a, a, a, a, b,b,b,c, c"
# ["a"]

# output:
#     "b,b,b,c"
# Expected: "b
"
# class Solution(object):
#     def mostCommonWord(self, paragraph, banned):
#         """
#         :type paragraph: str
#         :type banned: List[str]
#         :rtype: str
#         """
#         # 1, banned de-duplication
#         # 2, paragraph cleaning: strip("?!.',;) then split(" "), then build p to store unbanned paragraph words
#         # 3, build a dictionary: word_count = {word:count}
#         # 4, return max(word_count, key = lambda k: word_count[k]) #wrong
        
#         #1
#         banned = set(banned)
#         #2
#         # paragraph = paragraph.strip("?!.',;").split(" ") # wrong
#         paragraph = [s.strip("!?',;.") for s in paragraph.lower().split(" ")]
#         p = [w for w in paragraph if w not in banned]
#         #3
#         word_count = {w: 0 for w in p}
#         for w in p:
#             word_count[w] += 1
#         #4
#         # max_count = 0
#         # ret = None
#         # for w in word_count:
#         #     if word_count[w] > max_count:
#         #         max_count = word_count[w]
#         #         ret = w
#         # return ret
#         return max(word_count, key = lambda k: word_count[k])
    


    
    
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        return None
# # def mostCommonWord(self, paragraph, banned):
# #         tokens = [token for token in re.findall(r"([a-zA-Z]+)",  paragraph.lower()) if token not ## in banned]
# #         mostComm = collections.Counter(tokens).most_common(1)
# #         return mostComm[0][0]
    


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set(banned)
        tokens = [token for token in re.findall(r'[a-z]+', paragraph.lower()) if token not in banned]
        ## 1
        # mostComm = collections.Counter(tokens).most_common(1)
        # return mostComm[0][0]
        
        ## 2
        # word_count = {w: 0 for w in tokens}
        # for w in tokens:
        #     word_count[w] += 1
        # return max(word_count, key = lambda k: word_count[k])
        
        #3
        word_count = {w: 0 for w in tokens}
        for w in tokens:
            word_count[w] += 1
        ret = None
        max_count = 0
        for w in word_count.keys():
            if word_count[w] > max_count:
                max_count = word_count[w]
                ret = w
        return ret
        

