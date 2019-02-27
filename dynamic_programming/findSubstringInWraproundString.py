class Solution:
    def findSubstringInWraproundString(self, p: 'str') -> 'int':

        # if not len(p):
        #     return 0
        # # 分段
        # res_subs = set()
        # i = 1
        # while i < len(p):
        #     # res_sub = p[i-1]
        #     j = i
        #     # while i < len(p) and (ord(p[i]) - ord(p[i-1]) == 1 or ord(p[i]) - ord(p[i-1]) == 25):
        #     #     res_sub += p[i]
        #     #     i += 1
        #     while j < len(p) and (ord(p[j]) - ord(p[j-1]) == 1 or ord(p[j]) - ord(p[j-1]) == 25):
        #         j += 1
        #     res_sub = p[i-1:j]
        #     res_subs.add(res_sub)
        #     i = j + 1
        #
        # # find unique substring in res_subs
        # substr = set()
        # for str in res_subs:
        dict = {ch:1 for ch in p}
        count = 1
        for i in range(1, len(p)):
            if (ord(p[i]) - ord(p[i-1])) % 26 == 1:
                count += 1
            else:
                count = 1
            dict[p[i]] = max(dict[p[i]], count)

        return sum(dict.values())


        # print(res_subs)


if __name__ == '__main__':
    sol = Solution()
    sol.findSubstringInWraproundString('cabcdzabe')




