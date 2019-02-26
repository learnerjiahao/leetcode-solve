# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self) -> str:
        return (str(self.val)+'->'+str(self.next)) if self.next!=None else str(self.val)


class Solution:

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dump_node = ListNode(0)
        cur_node = dump_node
        while l1 or l2:
            while l1 and (l2 == None or l1.val <= l2.val):
                cur_node.next = ListNode(l1.val)
                cur_node = cur_node.next
                l1 = l1.next
            while l2 and (l1 == None or l2.val < l1.val):
                cur_node.next = ListNode(l2.val)
                cur_node = cur_node.next
                l2 = l2.next
        return dump_node.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # if the size of lists is equal to 0 or 1
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 0:
            return None
        if len(lists) == 2:
            return self.mergeTwoLists(lists[0], lists[1])

        lists.append(self.mergeTwoLists(lists[0], lists[1]))
        lists.pop(0)
        lists.pop(1)
        return self.mergeKLists(lists)

if __name__ == '__main__':
    soul = Solution()
    list = [1,2,3]
    list.pop(0)
    list.pop(0)
    print(list)
