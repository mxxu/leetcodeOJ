# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        if head.next is None:
            return head

        prev = None
        curr = head
        newhead = None

        while curr:
            rep = False
            while curr.next and curr.next.val == curr.val:
                curr = curr.next
                rep = True

            if not rep:
                if not newhead:
                    newhead = curr
                if not prev:
                    prev = curr
                else:
                    prev.next = curr
                    prev = curr
            curr = curr.next
            if prev:
                prev.next = None


        return newhead


def initlist(elems):
    head, curr = None, None
    for ele in elems:
        if not head:
            head = ListNode(ele)
            curr = head
        else:
            curr.next = ListNode(ele)
            curr = curr.next

    return head

def printlist(l):
    while l:
        print l.val
        l = l.next

    print

s = Solution()
#head = initlist([1,2,3,3,4,4,5])
#nhead = s.deleteDuplicates(head)
#printlist(nhead)
#
#
#head = initlist([1,1,1,2,3])
#nhead = s.deleteDuplicates(head)
#printlist(nhead)
head = initlist([1,2,2])
nhead = s.deleteDuplicates(head)
printlist(nhead)
