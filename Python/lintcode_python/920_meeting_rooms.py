"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        if not intervals or len(intervals) < 2:
            return True
            
        intervals = sorted(intervals, key = lambda x: x.start)
        prev = None
        for interval in intervals:
            if prev is None:
                prev = interval
                continue
            cur = interval
            if prev.end <= cur.start:
                prev = cur
            else:
                return False
        return True
            
            

