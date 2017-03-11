# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __str__(self):
        return '%s:%s' % (self.start, self.end)

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        sint = sorted(intervals, key=lambda it: it.start)
        buf = []
        curr = sint[0]
        for it in sint[1:]:
            if curr.end >= it.start:
                curr = Interval(curr.start, max(curr.end, it.end))
            else:
                buf.append(curr)
                curr = it
        buf.append(curr)
        return buf
        
s = Solution()
intervals = [Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)]
print [str(x) for x in s.merge(intervals)]