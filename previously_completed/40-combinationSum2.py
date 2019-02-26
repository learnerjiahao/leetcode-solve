class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret_lists = []

        def backtrace(candidates, ret_list, remain):

            if remain == 0:
                ret_lists.append(ret_list)
                return
            if remain < 0:
                return

            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i-1]:
                    continue
                now_len = len(ret_list)
                ret_list.append(candidates[i])
                backtrace(candidates[i + 1:], ret_list, remain - candidates[i])
                ret_list = ret_list[:now_len]

        # first sort candidates from small to large
        candidates.sort()
        backtrace(candidates, [], target)
        return ret_lists



if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum2([2,3,6,7], 7))
    # print(sol.combinationSum([2,3,5], 8))
    num1 = [1,2,3]
    num2 = [1,2,3]
    print(num1 == num2)

    # print([([3] + ])


