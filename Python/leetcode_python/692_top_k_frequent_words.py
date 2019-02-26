
import collections
import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        if words is None or len(words) == 0:
            return []
        count = collections.Counter(words)
        heap = []
        for word, freq in count.items():
            heapq.heappush(heap, Element(word, freq))
            if len(heap) > k:
                heapq.heappop(heap)
        return [heapq.heappop(heap).word for _ in range(k)][::-1]
                
class Element:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
    def __eq__(self, other):
        return self.freq == other.freq and self.word == other.word


