"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        if not intervals or len(intervals) < 2:
            return 1
        intervals = sorted(intervals, key = lambda x: x.start)
        heap = []
        heapq.heappush(heap, Element(intervals[0]))
        for i in range(1, len(intervals)):
            prev = heapq.heappop(heap).interval
            cur = intervals[i]
            if prev.end < cur.start:
                # no conflict, merge into one meeting room timeline
                prev.end = cur.end
                heapq.heappush(heap, Element(prev))
            else:
                # have conflict, need new room
                heapq.heappush(heap, Element(prev))
                heapq.heappush(heap, Element(cur))
        return len(heap)

class Element:
    def __init__(self, interval):
        self.interval = interval
    def __lt__(self, other):
        return self.interval.end < other.interval.end
    def __eq__(self, other):
        return self.interval.end == other.interval.end

