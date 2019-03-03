class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # method 1: two point expand from center
        def helper(left, right):
            sub_res = 0
            while left >= 0 and right < len(s)-1 and s[left] == s[right]:
                sub_res += 1
                left -= 1
                right += 1
            return sub_res
        res = 0
        for i in range(len(s)):
            res += 1
            res += helper(i-1, i+1)
            res += helper(i, i+1)
        return res

