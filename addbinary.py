class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        m, n = len(a), len(b)

        i, j = m - 1, n - 1
        buf = []
        while i >= 0 and j >= 0:
            if a[i] == '1' and b[j] == '1':
                if carry == 0:
                    buf.append('0')
                else:
                    buf.append('1')
                carry = 1
            elif a[i] == '1' and b[j] == '0' or a[i] == '0' and b[j] == '1':
                if carry == 0:
                    buf.append('1')
                    carry = 0
                else:
                    buf.append('0')
                    carry = 1
            else:
                buf.append(str(carry))
                carry = 0

            i -= 1
            j -= 1

        while i >= 0:
            if a[i] == '1':
                buf.append('1' if carry == 0 else '0')
            else:
                buf.append(str(carry))
                carry = 0

            i -= 1

        while j >= 0:
            if b[j] == '1':
                buf.append('1' if carry == 0 else '0')
            else:
                buf.append(str(carry))
                carry = 0

            j -= 1

        if carry == 1:
            buf.append('1')

        buf.reverse()
        return ''.join(buf)

s = Solution()
print s.addBinary('1', '111')
