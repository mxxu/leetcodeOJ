class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        sn1, sn2 = sorted(nums1), sorted(nums2)
        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        buf = []
        while i < m and j < n:
            if sn1[i] == sn2[j]:
                buf.append(sn1[i])
                i += 1
                j += 1
            elif sn1[i] < sn2[j]:
                i += 1
            else:
                j += 1
                
        return buf
        
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
s = Solution()
print s.intersect(nums1, nums2)