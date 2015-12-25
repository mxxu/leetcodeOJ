class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        n = len(s)
        if n % 2 != 0:
            return False

        stack = []
        stack.append(s[0])

        for i in range(1, n):
            c = s[i]
            last_c = stack[-1] if stack else None
            if c == '}':
                if last_c != '{':
                    return False
                stack.pop()
            elif c == ']':
                if last_c != '[':
                    return False
                stack.pop()
            elif c == ')':
                if last_c != '(':
                    return False
                stack.pop()
            else:
                stack.append(c)


        return not stack

s = Solution()
print s.isValid('(){}[]')
print s.isValid('({})')
