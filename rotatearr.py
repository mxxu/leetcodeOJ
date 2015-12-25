class Solution(object):

    def rotate(self, nums, k):

        """

        :type nums: List[int]

        :type k: int

        :rtype: void Do not return anything, modify nums in-place instead.

        """

        if not nums or k <= 0:
            return

        n = len(nums)
        k = k % n

        if k <= 0:
            return

        def reverse(l, i, j):
            while i < j:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1

        k = n - k
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)
        reverse(nums, 0, n-1)

s = Solution()

nums = range(1, 10)
print nums
s.rotate(nums, 3)
print nums
