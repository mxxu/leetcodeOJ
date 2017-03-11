class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        H = {}
        for n in nums:
            H[n] = H.get(n, 0) + 1
        items = H.items()
        minh = MinHeap(items[:k])
        for kv in items[k:]:
            minh.push(kv)
        # print minh
        return [item[0] for item in minh.buf][::-1]
            
class MinHeap(object):
    def __init__(self, data):
        self.buf = data
        n = len(data)
        for i in range(n/2-1, -1, -1):
            self.rebuild(i, n)
            # print self.buf, '-----', i
        
    def push(self, kv):
        key, value = kv
        if value > self.buf[0][1]:
            self.buf[0] = kv
            self.rebuild(0, len(self.buf))
            
    def rebuild(self, root, k):
        l, r = 2*root + 1, 2*root + 2
        minson = root
        if l < k and self.buf[minson][1] > self.buf[l][1]:
            minson = l
        if r < k and self.buf[minson][1] > self.buf[r][1]:
            minson = r
        if minson == root:
            return
            
        self.buf[minson], self.buf[root] = self.buf[root], self.buf[minson]
        self.rebuild(minson, k)
            
    def __str__(self):
        return ','.join([str(e) for e in self.buf])
        
# h = MinHeap(range(7, 0, -1))
# print str(h)
s = Solution()
print s.topKFrequent([1,1,1,2,2,3], 2)
# print s.topKFrequent([-1, -1], 1)