class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        acnt = 0
        sstat, gstat = {}, {}
        for i in range(len(secret)):
            s, g = secret[i], guess[i]
            if s == g:
                acnt += 1
                continue
            sstat[s] = sstat.get(s, 0) + 1
            gstat[g] = gstat.get(g, 0) + 1
            
        print secret, sstat, guess, gstat
            
        bcnt = 0
        for s, cnt in sstat.iteritems():
            if s in gstat:
                bcnt += min(cnt, gstat[s])
                
        return '%dA%dB' % (acnt, bcnt)
        
s = Solution()
print s.getHint('1807', '7810')
print s.getHint('1123', '0111')