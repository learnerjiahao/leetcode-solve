# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        num_count = {}

        def in_order_traversal(node):
            if not node:
                return
            if node.left:
                in_order_traversal(node.left)
            num_count[node.val] = (1 if node.val not in num_count.keys() else (num_count[node.val] + 1))
            if node.right:
                in_order_traversal(node.right)

        in_order_traversal(root)
        count_num = {}
        for key, count in num_count.items():
            if count not in count_num.keys():
                count_num[count] = [key]
            else:
                count_num[count].append(key)

        max_count = max(count_num.keys())
        return count_num[max_count]
