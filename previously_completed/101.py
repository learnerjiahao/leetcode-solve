# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root or (not root.left and not root.right):
            return True
        if bool(root.left) ^ bool(root.right):
            return False

        # tip:
        def itera_method(root_left, root_right):
            stack_left, stack_right = [
                [root_left, False]], [[root_right, False]]
            while len(stack_left) and len(stack_right):
                # left sub tree
                if not stack_left[-1][1] and stack_left[-1][0].left:
                    stack_left[-1][1] = True
                    stack_left.append([stack_left[-1][0].left, False])
                else:
                    now_travel_left = stack_left.pop()[0]
                    if now_travel_left.right:
                        stack_left.append([now_travel_left.right, False])

                # right sub tree
                if not stack_right[-1][1] and stack_right[-1][0].right:
                    stack_right[-1][1] = True
                    stack_right.append([stack_right[-1][0].right, False])
                else:
                    now_travel_right = stack_right.pop()[0]
                    if now_travel_right.val != now_travel_left.val:
                        return False
                    if now_travel_right.left:
                        stack_right.append([now_travel_right.left, False])

            return (not len(stack_left)) and (not len(stack_right))

        return itera_method(root.left, root.right)






root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
# n1 = TreeNode(3)
# n2 = TreeNode(4)
# n3 = TreeNode(4)
# n4 = TreeNode(3)

root.left = left
root.right = right

# left.left = n1
# right.right = n4

# left.right = n2
# right.left = n3

sol = Solution()
print(sol.isSymmetric(root))
