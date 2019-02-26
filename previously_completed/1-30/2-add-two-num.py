# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        conTag1 = True
        num2 = 0
        conTag2 = True

        nowNode1 = l1
        nowNode2 = l2

        index = 0;

        while conTag1 or conTag2:
            if nowNode1 != None:
                num1 += nowNode1.val * pow(10, index)
                nowNode1 = nowNode1.next
            else:
                conTag1 = False

            if nowNode2 != None:
                num2 += nowNode2.val * pow(10, index)
                nowNode2 = nowNode2.next
            else:
                conTag2 = False

            index += 1

        result_num = num1 + num2

        now_node = ListNode(0)
        rnode = now_node

        while True:
            digit = result_num % 10
            now_node.val = digit
            result_num = result_num // 10
            if result_num == 0:
                break
            now_node.next = ListNode(0)
            now_node = now_node.next

        return rnode


if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(2)
    l2 = ListNode(4)
    print(solution.addTwoNumbers(l1, l2))











