class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        
        sc = sorted(candidates)
        
        def go(cdts, tgt):
            if not cdts:
                return False, []
            if cdts[0] > tgt:
                return False, []
            if cdts[0] == tgt:
                return True, [[cdts[0]]]
                
            buf = []
            ok, ret = go(cdts, tgt-cdts[0])
            if ok:
                for l in ret:
                    l.insert(0, cdts[0])
                    buf.append(l)
            ok, ret = go(cdts[1:], tgt)
            if ok:
                buf.extend(ret)
            if buf:
                return True, buf
            return False, []
        ok, buf = go(sc, target)
        
        return buf
        
s = Solution()
print s.combinationSum([2,3,6,7], 100)