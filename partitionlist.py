# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        if not head:
            return head

        tail = head
        n = 1
        while tail.next:
            tail = tail.next
            n += 1

        if n == 1:
            return head

        tailp = tail
        current = head
        prev = None
        newhead = None

        for i in range(n):
            if current.val < x:
                prev = current
                if not newhead:
                    newhead = current
                current = current.next
            else:
                if not prev:
                    tailp.next = current
                    preserve = current.next
                    tailp = current
                    tailp.next = None
                    current = preserve
                else:
                    if tailp != current:
                        prev.next = current.next
                        tailp.next = current
                        tailp = current
                        tailp.next = None
                        current = prev.next

        if not newhead:
            newhead = current

        return newhead

s = Solution()
head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)

h = s.partition(head, 3)
while h:
    print h.val
    h = h.next

head = ListNode(1)
head.next = ListNode(2)
h = s.partition(head, 2)
while h:
    print h.val
    h = h.next
