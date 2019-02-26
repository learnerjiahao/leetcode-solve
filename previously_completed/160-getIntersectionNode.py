# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        A_ids = set()
        nodeA = headA
        while nodeA:
            A_ids.add(id(nodeA))
            nodeA = nodeA.next

        nodeB = headB
        while nodeB:
            if id(nodeB) in A_ids:
                return nodeB
            nodeB = nodeB.next

        return None



if __name__ == '__main__':
    node1 = ListNode(4)
    node2 = node1
    print(id(node1), id(node2))