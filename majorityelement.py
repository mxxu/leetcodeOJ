class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        candidate, count = None, 0
        for n in num:
            if candidate is None:
                candidate, count = n, 1
            elif candidate == n:
                count = count + 1
            elif candidate != n:
                count = count - 1

            candidate = None if count <= 0 else candidate
        return candidate

s = Solution()
print s.majorityElement([1,2,3,4,3,3,3])
