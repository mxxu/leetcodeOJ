class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers) - 1
        while i < j:
            s = numbers[i] + numbers[j]
            if s == target:
                return [i+1, j+1]
                
            if s < target:
                i += 1
            else:
                j -= 1
                
s = Solution()
print s.twoSum([2, 7, 11, 15], 9)