class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        mm = len(nums1)
        for i in range(m-1, -1, -1):
            print i+mm-m, i
            nums1[i+mm-m] = nums1[i]

        print nums1

        i, j, k = mm-m, 0, 0
        while i < mm and j < n:
            if nums1[i] < nums2[j]:
                nums1[k] = nums1[i]
                i += 1
                k += 1
            elif nums1[i] > nums2[j]:
                nums1[k] = nums2[j]
                j += 1
                k += 1
            else:
                nums1[k] = nums1[i]
                nums1[k+1] = nums2[j]
                k += 2
                i += 1
                j += 1

        while i < mm:
            nums1[k] = nums1[i]
            i += 1
            k += 1

        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1


s = Solution()
nums1 = [1,3,5,7,9,0,0,0,0]
m = 5
nums2 = [2,4,6,8]
n = 4
s.merge(nums1, m, nums2, n)
print nums1

nums1 = [1, 0]
m = 1
nums2 = [2]
n = 1
s.merge(nums1, m, nums2, n)
print nums1
