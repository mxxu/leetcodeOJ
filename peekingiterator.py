# Below is the interface for Iterator, which is already defined for you.
#
class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.buf = nums
        self.size = len(nums)
        self.p = 0

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.p < self.size

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        i = self.p
        self.p += 1
        return self.buf[i]

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.cache_next = None
        self.iterator = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.cache_next == None:
            if self.iterator.hasNext():
                self.cache_next = self.iterator.next()
        return self.cache_next

    def next(self):
        """
        :rtype: int
        """
        if self.cache_next != None:
            tmp = self.cache_next
            self.cache_next = None
            return tmp
        
        return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cache_next != None or self.iterator.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
iter = PeekingIterator(Iterator(range(10)))
while iter.hasNext():
    val = iter.peek()   # Get the next element but not advance the iterator.
    # print val
    print iter.next()         # Should return the same value as [val].