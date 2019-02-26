# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.ret_longest_path = 1

        def longestDeep(subroot):
            if not subroot: return 0
            right_longestDeep, left_longestDeep = longestDeep(subroot.right), longestDeep(subroot.left)
            self.ret_longest_path = max(self.ret_longest_path, right_longestDeep + left_longestDeep + 1)
            return max(right_longestDeep, left_longestDeep) + 1

        longestDeep(root)
        return self.ret_longest_path - 1
        
if __name__ == "__main__":
    sol = Solution()
    # sol.diameterOfBinaryTree
