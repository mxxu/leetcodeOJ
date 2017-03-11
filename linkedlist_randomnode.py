# Definition for singly-linked list.
import random
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        h = self.head
        n = 0
        t = None
        while h:
            n += 1
            r = random.random()
            if r < 1.0/n:
                t = h.val
                
            h = h.next
        return t


# Your Solution object will be instantiated and called as such:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
obj = Solution(head)
l = []
for _ in range(100):
    param_1 = obj.getRandom()
    l.append(param_1)
    
from collections import Counter
c = Counter(l)
print c
    