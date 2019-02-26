class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if len(needle) == 0:
            return 0
        if len(needle) > len(haystack):
            return -1

        longest_offset_map = [i+1 for i in range(0, len(needle) - 1)]
        for i in range(0, len(needle)-1):
            for j in range(1, i+1):
                if needle[j:i+1] == needle[0:i+1-j]:
                    longest_offset_map[i] = j
                    break

        print(longest_offset_map)

        index_h = 0
        index_n = 0
        while index_h < len(haystack):
            while index_n < len(needle) and index_h + index_n < len(haystack) and haystack[index_h + index_n] == needle[index_n]:
                index_n += 1
            if index_n == len(needle):
                return index_h
            if index_n == 0:
                index_h += 1
            else:
                index_h = index_h + longest_offset_map[index_n-1]
                index_n = index_n - longest_offset_map[index_n - 1]

        return -1

if __name__ == '__main__':
    soul = Solution()
    # print(soul.strStr("mississippi", "sisi"))
    # print(soul.strStr("hello", "ll"))
    # print(soul.strStr("babba", "bb"))
    # print(soul.strStr("mississippi", "issip"))
    print(soul.strStr("mississippi", "issipi"))
    # print(soul.strStr("mississippi", "pi")) # abcefab  5  7