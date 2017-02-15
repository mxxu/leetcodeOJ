# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return '%s -> %s' % (self.val, self.next)

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
            
        p = head
        for i in range(n):
            p = p.next
            if not p and i == n-1:
                return head.next
            # not p and i < n-1, invalid n, pass
                
        head_bk = head
        while p.next:
            head = head.next
            p = p.next
            
        head.next = head.next.next
        return head_bk
        
s = Solution()
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
print s.removeNthFromEnd(l, 2)