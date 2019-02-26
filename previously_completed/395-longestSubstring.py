class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        now_map = {}
        for i in range(len(s)):
            if s[i] in now_map.keys():
                now_map[s[i]] += 1
            else:
                now_map[s[i]] = 1
            for j in range(i + 1, len(s)):
                pass
