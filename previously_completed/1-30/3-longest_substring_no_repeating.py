class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mmap = dict()
        loc = 0
        max_len = 0

        rstart = 0
        rend = 0

        while loc < len(s):
            if s[loc] in mmap.keys():
                if len(mmap) > max_len:
                    max_len = len(mmap)
                    rend = loc - 1

                loc = mmap[s[loc]]
                mmap.clear()
            else:
                mmap[s[loc]] = loc

            loc += 1

        if max_len < len(mmap):
            max_len = len(mmap)
            rend = len(s) - 1

        for ri in range(0, max_len):
            print(s[rend - (max_len - ri - 1)])

        return max_len


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring('abbce'))