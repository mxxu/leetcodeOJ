class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        maxp, prev = 0, 1

        for i, n in enumerate(A):
            prev = prev * n

            if i == 0:
                maxp = prev
            else:
                maxp = max(maxp, prev)

            if prev == 0:
                prev = 1

        return maxp
