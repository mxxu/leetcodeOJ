# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        if fast:
            slow = slow.next
        
        curr, nxt = slow, slow.next
        slow.next = None
        while nxt:
            prev, p = curr, nxt
            curr, nxt = nxt, nxt.next
            p.next = prev
                    
        p = curr
        while p:
            if p.val != head.val:
                return False
            p = p.next
            head = head.next
            
        return True
        
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)
obj = Solution()
print obj.isPalindrome(ListNode(1))