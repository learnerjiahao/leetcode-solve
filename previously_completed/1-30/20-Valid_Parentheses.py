class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses_dict = {'(':')','{':'}','[':']'}
        stack = []
        for i in range(0, len(s)):
            if s[i] in parentheses_dict.keys():
                stack.append(s[i])
            elif s[i] in parentheses_dict.values():
                if len(stack)>0 and parentheses_dict[stack[len(stack)-1]]==s[i]:
                    stack.pop()
                else:
                    return False

        return len(stack)==0





if __name__ == '__main__':
    soul = Solution()
    print(soul.isValid('()[]{}'))