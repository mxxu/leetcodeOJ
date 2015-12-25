class Solution(object):

    def sortColors(self, nums):

        """

        :type nums: List[int]

        :rtype: void Do not return anything, modify nums in-place instead.

        """
        if not nums:
            return

        n = len(nums)

        last_0, new_2 = -1, n

        i = 0
        while i < new_2:
            x = nums[i]
            if x == 0:
                if last_0 == i:
                    i += 1
                    continue
                nums[last_0 + 1], nums[i] = nums[i], nums[last_0 + 1]
                last_0 += 1
            elif x == 2:
                nums[new_2 - 1], nums[i] = nums[i], nums[new_2 - 1]
                new_2 -= 1
            else:
                i += 1

s = Solution()
nums = [2,2, 1,1, 0,0]
s.sortColors(nums)
print nums
