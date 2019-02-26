class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # def strReverse(s, start, stop):
        #     tmp_str = reversed(s[start: stop])
        #     for ch in tmp_str:
        #         s[start] = ch
        #         start += 1

        res_str = ''

        index = 0

        while len(s) - index >= 2 * k:
            res_str += s[index: index + k: -1]
            res_str += s[index + k: index + 2*k: -1]
            # strReverse(s, index, index + k)
            # strReverse(s, index + k, index + 2*k)
            index += (2 * k)

        if len(s) - index <= 0:
            s = res_str
            return

        if len(s) - index < k:
            res_str += s[index: len(s): -1]
            # strReverse(s, index, len(s))
        else:
            res_str += s[index: index+k: -1]
            # strReverse(s, index, index+k)
        s = res_str


if __name__ == "__main__":
    sol = Solution()
    str = "abcdefg";
    # str.
    sol.reverseStr(str, 2)
    print(str)

