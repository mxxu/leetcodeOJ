import itertools
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
            
        # combs = set()
#         for comb in itertools.permutations(words):
#             combs.add(''.join(comb))
#         # print combs
#         k = len(words) * len(words[0])
#
#         buf = []
#         for i in range(len(s)-k+1):
#             if s[i: i+k] in combs:
#                 buf.append(i)
            
        n = len(words[0])
        wordslen = n * len(words)
        sl = len(s)
        
        # begin, end = 0, 0
        m = {}
        for w in words:
            m[w] = m.get(w, 0) + 1
            
        buf = []
        i = 0
        while i < sl - wordslen + 1:
            d = {}
            j = i
            ok = True
            for j in range(i, i+wordslen, n):
                w = s[j: j+n]
                if w not in m:
                    ok = False
                    break
                    
                d[w] = d.get(w, 0) + 1
                if d[w] > m[w]:
                    ok = False
                    break
            if ok:
                buf.append(i)
            i += 1
        
        # while end < len(s)-n+1:
        #     substr = s[end:end+n]
        #     # print substr, counter, m
        #     if substr not in m:
        #         for i in range(begin, end, 3):
        #             w = s[i:i+3]
        #             if w in m:
        #                 m[w] += 1
        #         begin = end = end + 1
        #         counter = len(words)
        #         continue
        #
        #     while m[substr] <= 0 and begin < end:
        #         ww = s[begin: begin+n]
        #         m[ww] += 1
        #         if m[ww] > 0:
        #             counter += 1
        #         begin += n
        #
        #     if m[substr] > 0:
        #         counter -= 1
        #     m[substr] -= 1
        #
        #     # print '-----', substr, counter, m, begin, end
        #     if counter > 0:
        #         end += n
        #         continue
        #
        #     if end - begin + n == wordslen:
        #         # print begin, end, '......'
        #         if counter == 0:
        #             buf.append(begin)
        #
        #         w = s[begin: begin+n]
        #         m[w] += 1
        #         if m[w] > 0:
        #             counter += 1
        #
        #         begin += n
        #
        #         end += n
            
            # ok = False
#             while begin <= end:
#                 if end - begin + n == wordslen and counter == 0:
#                     buf.append(begin)
#                     ok = True
#
#                 w = s[begin:begin+n]
#                 m[w] += 1
#                 if m[w] > 0:
#                     counter += 1
#
#                 begin += n
#
#             if not ok:
#                 begin = end = end + n
#             else:
#                 begin = end = buf[-1] + n
            
        return buf
        
s = Solution()
s1 = "aaaaaaaa"
words1 = ["aa","aa","aa"]
print s.findSubstring(s1, words1)
st = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
print s.findSubstring(st, words)
#
s2 = "barfoothefoobarman"
words2 = ["foo", "bar"]
print s.findSubstring(s2, words2)

s3 = "wordgoodgoodgoodbestword"
words3 = ["word","good","best","good"]
print s.findSubstring(s3, words3)