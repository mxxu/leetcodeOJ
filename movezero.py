class Solution(object):

    def moveZeroes(self, nums):

        """

        :type nums: List[int]

        :rtype: void Do not return anything, modify nums in-place instead.

        """

        if not nums:
            return
        n = len(nums)


        i, j = 0, 0
        while i < n and j < n:
            while i < n and nums[i] != 0:
                i += 1

            if i == n:
                return

            j = max(i + 1, j)
            while j < n and nums[j] == 0:
                j += 1

            if j == n:
                return

            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1

s = Solution()
nums = [0, 1, 0, 3, 12]
s.moveZeroes(nums)
print nums
