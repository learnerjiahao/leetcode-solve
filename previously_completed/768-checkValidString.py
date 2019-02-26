class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        self.stack_s = list()
        list_s = list(s)
        
        def backtrace(now_start):
            if now_start == len(list_s) and len(self.stack_s) == 0:
                return True

            for i in range(now_start, len(list_s)):
                ch = list_s[i]
                if ch == '(':
                    self.stack_s.append(ch)
                if ch == ')':
                    if len(self.stack_s) == 0:
                        return False
                    self.stack_s.pop()
                if ch == '*':
                    for any_ch in ['(', ')', '']:
                        back_stack = [ch for ch in self.stack_s]
                        if any_ch == '' :
                            if backtrace(i+1): return True
                        else:
                            list_s[i] = any_ch
                            if backtrace(i): return True
                        self.stack_s = back_stack
                    return False
                        
            return False
        

if __name__ == "__mian__":
    sol = Solution()
    print(sol.checkValidString('((*)'))