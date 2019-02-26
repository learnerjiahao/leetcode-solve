class Solution:

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses_dict = {'(':')'}
        stack = []
        for i in range(0, len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == ')':
                if len(stack)>0:
                    stack.pop()
                else:
                    return False
            else:
                return False

        return len(stack)==0

    def longestValidParentheses1(self, s):
        """
        :type s: str
        :rtype: int
        """
        left_parenthes_index, right_parenthes_index = 0, len(s) - 1
        while left_parenthes_index < right_parenthes_index:
            while s[left_parenthes_index] != '(':
                left_parenthes_index += 1
            while s[right_parenthes_index] != ')':
                right_parenthes_index += 1

            # if (right_parenthes_index-left_parenthes_index > 0) \
            #     and ((right_parenthes_index-left_parenthes_index) % 2 == 1) \
            #     and self.isValid(s[right_parenthes_index:left_parenthes_index+1]):


    def longestValidParentheses(self, s):
        ret_longest_parentheses_length = 0
        for left_parenthes_index in range(0, len(s)-1):
            if s[left_parenthes_index] != '(':
                continue
            for right_parenthes_index in range(len(s)-1, left_parenthes_index, -1):
                if s[right_parenthes_index] == ')' \
                        and self.isValid(s[left_parenthes_index:right_parenthes_index+1]) \
                        and ret_longest_parentheses_length < (right_parenthes_index+1-left_parenthes_index):
                    ret_longest_parentheses_length = right_parenthes_index+1-left_parenthes_index
                    break


        return ret_longest_parentheses_length

if __name__ == '__main__':
    sol = Solution()
    sol.longestValidParentheses("(()")