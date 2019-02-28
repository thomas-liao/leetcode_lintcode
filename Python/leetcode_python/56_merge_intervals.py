# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


# solution 1, using heap... heap
# hold element, if next one no intersection, add hold to res and hold = next
# if intersection, hold = Interval(hold.start, max(hold.end, cur.end))
# note: at the end, should append remaining hold to res
# class Solution:
#     def merge(self, intervals: List[Interval]) -> List[Interval]:
#         if not intervals or len(intervals) < 2:
#             return intervals
#         heap = []
#         for interval in intervals:
#             heapq.heappush(heap, Element(interval))
#         hold = None
#         res = []
#         while heap:
#             if hold is None:
#                 hold = heapq.heappop(heap).interval
#             cur = heapq.heappop(heap).interval
#             # no intersection
#             if hold.end < cur.start:
#                 res.append(hold)
#                 hold = cur
#             # intersection
#             else:
#                 hold = Interval(hold.start, max(hold.end, cur.end))
#         res.append(hold)
#         return res
        
# class Element:
#     def __init__(self, interval):
#         self.interval = interval
#     def __lt__(self, other):
#         return self.interval.start < other.interval.start
#     def __eq__(self, other):
#         return self.interval.start == other.interval.start
        

    
# Solution 2: simple and straightforward understanding
# sort according to start, dump everything into res
# if intersection, extend, else: just add new element
class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        if not intervals or len(intervals) < 2:
            return intervals
        intervals = sorted(intervals, key = lambda x: x.start)
        res = []
        for interval in intervals:
            if not res:
                res.append(interval)
                continue
            prev = res[-1]
            if prev.end < interval.start:
                res.append(interval)
            else:
                prev.end = max(prev.end, interval.end)
        return res
