# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals: List[Interval], newInterval: Interval) -> List[Interval]:
        if not intervals or not intervals[0]:
            return [newInterval]
        hold = newInterval
        
        # bug! removing while iterating will cause serious bug......
        remove_list = []
        for interval in intervals:
            if self.isIntersect(hold, interval):
                hold = Interval(min(hold.start, interval.start), max(hold.end, interval.end))
                print("hold after merging: ", hold.start, "--", hold.end)
                print("removed interval: ", interval.start, "--", interval.end)
                # intervals.remove(interval)
                remove_list.append(interval)
        for l in remove_list:
            intervals.remove(l)
        intervals.append(hold)

        return sorted(intervals, key = lambda x: x.start)
    
    def isIntersect(self, a, b):
        return not (a.end < b.start or b.end < a.start)
        
