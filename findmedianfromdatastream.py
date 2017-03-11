import bisect
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.size = 0
        self.buf = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        bisect.insort(self.buf, num)
        self.size += 1

    def findMedian(self):
        """
        :rtype: float
        """
        if self.size % 2 == 1:
            return self.buf[self.size/2]
        else:
            return (self.buf[self.size/2-1] + self.buf[self.size/2])/2.0


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
# print obj.findMedian()
for n in [6,10,2,6,5,0,6,3,1,0,0]:
    obj.addNum(n)
    print obj.findMedian()
# obj.addNum(1)
# print obj.findMedian()
# obj.addNum(2)
# print obj.findMedian()
# obj.addNum(3)
# print obj.findMedian()