class Solution(object):

    def bsearch(self, nums, n):
        i, j = 0, len(nums)-1

        if nums[i] == n:
            return i
        if nums[j] == n:
            return j

        while i <= j:
            mid = i + (j - i)/2
            if nums[mid] == n:
                return mid
            if nums[mid] < n:
                i = mid + 1
            else:
                j = mid - 1

        return -1

    def threeSumClosest(self, nums, target):

        """

        :type nums: List[int]

        :rtype: List[List[int]]

        """

        if not nums:
            return 0

        n = len(nums)
        if n < 3:
            return 0

        sortnums = sorted(nums)

        mindiff = None

        for k in range(n-2):
            e = sortnums[k]
            i, j = k + 1, n - 1

            while i < j:
                if i == k:
                    i += 1
                    continue
                if j == k:
                    j -= 1
                    continue
                s1 = sortnums[i] + sortnums[j] + e

                diff = s1 - target

                if mindiff is None:
                    mindiff = diff
                else:
                    if abs(mindiff) > abs(diff):
                        mindiff = diff

                if diff == 0:
                    return target
                elif diff < 0:
                    i += 1
                else:
                    j -= 1

        return mindiff + target

s = Solution()

nums = [-1, 0, 1, 2, -1, -4]
print s.threeSumClosest(nums, 1)
nums = [-1, 0, 1, 0]
print s.threeSumClosest(nums, 1)

nums = [11,3,13,-14,12,-13,14,-7,-1,14,5,-15,-11,-15,9,11,-6,-11,-15,-5,-3,5,-7,10,11,11,-10,-3,-4,8,-15,-15,-4,6,8,-6,8,7,-6,-8,6,6,-8,11,-1,8,-1,8,13,-1,-11,-5,-11,-3,12,8,-15,-13,-10,-11,3,12,11,14,3,4,-15,-4,-4,-13,-5,9,8,2,-3,-8,-12,12,-14,-14,-12,12,-12,-7,-14,8,8,9,10,13,13,-10,2,9,-10,-9,-10,12,2,1,14,13,-13,8,-8,0,7,-5,-11,0,-12,-8,-11,-8,-8,-9,-15,-15]
print len(nums)
print s.threeSumClosest(nums, 1)


print s.threeSumClosest([-1, 2, 1, -4], 1)
