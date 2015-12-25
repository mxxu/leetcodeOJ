class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0

        m = len(ratings)
        i = 0
        buf = [1] * m
        while i < m:
            j = i
            while i + 1 < m and ratings[i + 1] <= ratings[i]:
                i += 1

            buf[i] = 1
            for t in range(i-1, j-1, -1):
                if ratings[t] > ratings[t+1]:
                    buf[t] = buf[t+1] + 1
                else:
                    buf[t] = buf[t+1]
            print buf

            j = i
            while i + 1 < m and ratings[i + 1] >= ratings[i]:
                i += 1

            for t in range(j+1, i+1):
                if ratings[t] > ratings[t-1]:
                    buf[t] = buf[t-1] + 1
                else:
                    buf[t] = buf[t-1]
        return sum(buf)

        # buf = [1]
        # for i in range(1, len(ratings)):
        #     if ratings[i] == ratings[i-1]:
        #         buf.append(buf[-1])
        #     elif ratings[i] < ratings[i-1]:
        #         last = buf[-1]
        #         if last > 1:
        #             buf.append(last - 1)
        #         else:
        #             buf[-1] = buf[-1] + 1
        #             buf.append(buf[-1] - 1)
        #             for j in range(i-2, -1, -1):
        #                 if (ratings[j] >= ratings[j+1] and buf[j] < buf[j+1]) or (
        #                     ratings[j] > ratings[j+1] and buf[j] == buf[j+1]):
        #                     buf[j] = buf[j] + 1

        #     else:
        #         buf.append(buf[-1] + 1)
        # return sum(buf)

if __name__ == '__main__':
    sol = Solution()

    ratings = [3, 2, 10, 4, 5]
    print sol.candy(ratings)
