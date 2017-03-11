class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        x = len(nums)
            
        first, first_sum = None, 0
        second, second_sum = None, 0
        for num in nums:
            if num == first:
                first_sum += 1
            elif num == second:
                second_sum += 1
            elif first is None:
                first = num
                first_sum = 1
            elif second is None:
                second = num
                second_sum = 1
            else:
                first_sum -= 1
                second_sum -= 1
                if first_sum == 0:
                    first = None
                if second_sum == 0:
                    second = None
        # print first, first_sum, second, second_sum
        fs, ss = 0, 0
        for n in nums:
            if n == first:
                fs += 1
            elif n == second:
                ss += 1
        # print first, second, fs, ss
        buf = []
        if fs > x/3:
            buf.append(first)
        if ss > x/3:
            buf.append(second)
        return buf
s = Solution()
for nums in [[1,2,3,2], [1,2,3,4,5,6], [2,2], [3,2,3], [], [1,2,2,3,2,1,1,3]]:
    print s.majorityElement(nums)