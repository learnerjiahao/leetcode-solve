# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKNodes(self, headNode, K):
        if not headNode:
            return None

        countNode = 0
        nowNode = headNode.next
        while nowNode:
            countNode += 1
            nowNode = nowNode.next
        if countNode < K:
            return None

        firstNode = headNode.next
        if not firstNode:
            return None

        preNode = firstNode
        nowNode = firstNode.next
        if not nowNode:
            return preNode

        countNode = 0

        while countNode < K - 1 and nowNode:
            behindNode = nowNode.next
            nowNode.next = preNode
            preNode = nowNode
            nowNode = behindNode
            countNode += 1

        headNode.next = preNode
        firstNode.next = nowNode

        return firstNode

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        fakeHead = ListNode(None)
        fakeHead.next = head

        rethead = self.reverseKNodes(fakeHead, k)
        while rethead:
            rethead = self.reverseKNodes(rethead, k)

        return fakeHead.next