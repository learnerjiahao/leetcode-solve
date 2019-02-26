# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self) -> str:
        return (str(self.val)+'->'+str(self.next)) if self.next!=None else str(self.val)


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n <=0:
            return head
        nowNode = head
        count = 0
        while nowNode != None:
            nowNode = nowNode.next
            count += 1
        if n>count:
            return head
        elif n==count:
            return head.next

        nowNode = head
        for i in range(0, count-n-1):
            nowNode = nowNode.next

        nowNode.next = nowNode.next.next

        return head


if __name__ == '__main__':
    soul = Solution()
    head = ListNode(1)
    node1 = ListNode(2)
    head.next = node1
    node2 = ListNode(3)
    node1.next = node2
    node3 = ListNode(4)
    node2.next = node3
    node4 = ListNode(5)
    node3.next = node4
    print(soul.removeNthFromEnd(head, 4))


