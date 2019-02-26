class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        elif len(strs) == 0:
            return ''

        max_pre_len = 0
        while True:
            ch = ''
            for str in strs:
                if max_pre_len >= len(str):
                    return str
                if ch == '':
                    ch = str[max_pre_len]
                elif str[max_pre_len] != ch:
                    return str[0:max_pre_len]
            max_pre_len += 1

        return ''


if __name__ == '__main__':
    soul = Solution()
    print(soul.longestCommonPrefix(["flower","lf","flight"]))