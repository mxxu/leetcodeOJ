# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode

    def getLen(self, head):
        ret = 0
        while head:
            ret = ret + 1
            head = head.next

        return ret

    def forward(self, head, n):
        while head and n > 0:
            head = head.next
            n = n -1
        return head

    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        lenA = self.getLen(headA)
        lenB = self.getLen(headB)

        new_headA = self.forward(headA, lenA - lenB)
        new_headB = self.forward(headB, lenB - lenA)

        while new_headA and new_headB:
            if new_headA == new_headB:
                return new_headA
            new_headA = new_headA.next
            new_headB = new_headB.next
        return None
