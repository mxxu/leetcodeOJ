class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        s = 0
        stack = [height[0]]
        n = len(height)
        for i in range(1, n):
            while i < n and height[i] <= stack[-1]:
                stack.append(height[i])
                i+=1
                
            
        
s = Solution()
a = [0,1,0,2,1,0,1,3,2,1,2,1]
print s.trap(a)