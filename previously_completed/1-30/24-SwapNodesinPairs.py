# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self) -> str:
        return (str(self.val) + '->' + str(self.next)) if self.next != None else str(self.val)

class Solution:
    def reverseKNodes(self, headNode, K):
        if not headNode:
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


    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fakeHead = ListNode(None)
        fakeHead.next = head

        rethead = self.reverseKNodes(fakeHead, 2)
        while rethead:
            rethead = self.reverseKNodes(rethead, 2)


        return fakeHead.next


if __name__ == '__main__':
    soul = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print(soul.swapPairs(node1))

