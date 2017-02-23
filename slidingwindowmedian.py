import bisect
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        buf = sorted(nums[:k-1])
        
        n = len(nums)
        i = k-1
        ret = []
        odd = k % 2 == 1
        while i < n:
            bisect.insort(buf, nums[i])
            if odd:
                mid = buf[k/2] * 1.0
            else:
                mid = (buf[k/2-1] + buf[k/2])/2.0
            ret.append(mid)
            
            prev_idx = bisect.bisect_left(buf, nums[i-k+1])
            buf = buf[:prev_idx] + buf[prev_idx+1:]
            i += 1
        return ret
s = Solution()
nums, k = [1,3,-1,-3,5,3,6,7], 3
print s.medianSlidingWindow(nums, k)