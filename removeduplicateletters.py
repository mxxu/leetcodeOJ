class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1
            
        stack = ['0']
        visited = {}
        for c in s:
            counter[c] -= 1
            if visited.get(c, False):
                continue
                
            while c < stack[-1] and counter[stack[-1]]:
                visited[stack[-1]] = False
                stack.pop()
                
            stack.append(c)
            visited[c] = True
        return ''.join(stack[1:])
        
s = Solution()
print s.removeDuplicateLetters('cbacdcbc')