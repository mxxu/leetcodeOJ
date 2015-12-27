class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.sums = []
        for n in nums:
            if not self.sums:
                res = n
            else:
                res = self.sums[-1] + n
            self.sums.append(res)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        bigger = max(i, j)
        smaller = min(i, j)
        if smaller == 0:
            return self.sums[bigger]
        return self.sums[bigger] - self.sums[smaller-1]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)

na = NumArray([-2, 0, 3, -5, 2, -1])
print na.sumRange(0, 2)
print na.sumRange(2, 5)
print na.sumRange(0, 5)